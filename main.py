# This file has 3 systems running all in async thread
# 1. Websocket server
# 2. Flask for REST API
# 3. User Input command

import asyncio
import json
import threading
import time
from waitress import serve
from flask import Flask, jsonify, render_template, request, url_for, send_from_directory
import websockets
import requests
import os

from util.screens import Screens, ScreenNames
from util.screen_analyzer import ScreenAnalyzer

# since we ran 3 threads, they all listen to this stop_event
# when it is set, they all decided to stop and close their task, graceful shutdown
stop_event = threading.Event()

app = Flask(__name__, static_url_path='', static_folder='static')
connected_clients = set()
message_queue = asyncio.Queue()  # Use asyncio.Queue for async operations
queue_has_items = asyncio.Event() # Event to signal when the queue is not empty


# # we are using url_for which requires app_context
# # for app_context to work for static a SERVER_NAME needs to be set
# app.config['SERVER_NAME'] = 'localhost:5000'

# # storing a variable for local thread only because wssserver, flask all run in their own thread
# # the variable should be available in their thread
# app_context = threading.local()

SCREENS = Screens()
ANALYZER = ScreenAnalyzer()

## REST API ENDPOINTS
@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

@app.route('/command', methods=['POST'])
def receive_data():
    print('inside /command API endpoint')
    data = request.get_json()
    print(f"Received data from REST API: {data}")

    response = SCREENS.handle_input(data["message"])
    
    _jsonify = jsonify(response)
    message_queue.put_nowait(_jsonify.get_json())
    queue_has_items.set() # Signal that there are items in the queue
    return _jsonify

@app.route('/static/screenshots/<path:filename>')
def serve_screenshot(filename):
    return send_from_directory('static/screenshots', filename)

@app.route('/api/screen/<screen_code>')
def get_screen(screen_code):
    try:
        # Convert screen_code to ScreenNames enum
        screen_enum = ScreenNames[screen_code]
        screen_data = SCREENS.screens.get(screen_enum)
        if screen_data:
            return jsonify({
                "image_url": screen_data["image_url"],
                "navigation_options": list(screen_data["navigations"].keys()),
                "screen_data": screen_data["extra_data"]
            })
        return jsonify({"error": "Screen not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/navigate', methods=['POST'])
def navigate():
    try:
        data = request.json
        screen_code = data.get('screen_code')
        navigation_key = data.get('navigation_key')
        
        # Convert screen_code to ScreenNames enum
        current_screen = ScreenNames[screen_code]
        screen_data = SCREENS.screens.get(current_screen)
        
        if navigation_key in screen_data["navigations"]:
            next_screen = screen_data["navigations"][navigation_key]
            next_screen_data = SCREENS.navigate_to(next_screen)
            return jsonify(next_screen_data)
        
        return jsonify({"error": "Invalid navigation key"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/type', methods=['POST'])
def type_text():
    try:
        data = request.json
        screen_code = data.get('screen_code')
        text = data.get('text')
        
        # Get the current screen
        current_screen = ScreenNames[screen_code]
        screen_data = SCREENS.screens.get(current_screen)
        
        # Return the same screen with updated text
        return jsonify({
            "image_url": screen_data["image_url"],
            "navigation_options": list(screen_data["navigations"].keys()),
            "screen_data": screen_data["extra_data"],
            "typed_text": text
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/analyse_screen', methods=['POST'])
def analyze_screen():
    print('inside /analyse_screen API endpoint')
    # data = request.get_json()
    # print(f"Received data from REST API: {data}")

    # response = SCREENS.handle_input(data["message"])
    
    # _jsonify = jsonify(response)

    response = ANALYZER.take_screenshot_and_analyze()
    _jsonify = jsonify(response)
    # message_queue.put_nowait(_jsonify.get_json())
    # queue_has_items.set()
    return _jsonify

## REST API SERVER THREAD - INITIALIZE
def flask_thread_function():
    # global app
    # with app.app_context():
    #     app_context.app = app

    server = serve(app, host='0.0.0.0', port=5000, threads=1, _quiet=True)
    print("Flask thread started @ http://localhost:5000")

    while not stop_event.is_set():
        time.sleep(0.1)  # Important: Check the stop event periodically
    
    server.close()
    
    print("Flask thread stopped.")

## WEBSOCKET SERVER THREAD - INITIALIZE
async def websocket_server():
    async with websockets.serve(handler, "localhost", 8765): # Using 'async with' is very important for proper cleanup
        print("WebSocket server started @ ws://localhost:8765")
        while not stop_event.is_set():
            await asyncio.sleep(0.1) # Check stop event periodically
        print("WebSocket server stopped.")

## WEBSOCKET - EVENT HANDLER
async def handler(websocket):
        
    connected_clients.add(websocket)
    try:
        
        # app_state["current_screen"] = screens.handle_input("start")

        # initial_message = { **app_state["current_screen"]}
        initial = SCREENS.handle_input("off")
        await websocket.send(json.dumps(initial))

        while True:  # Run indefinitely
            message = await websocket.recv() # Wait indefinitely for message
            print(f"Received from WebSocket: {message}")

            # if message.startswith("$sn "):
            #     message = message[2:]
            #     message = message.strip()

            #     print('you asked me to take snapshot and analyze')

            # await websocket.send(json.dumps({ **app_state["current_screen"] })) 
            response = SCREENS.handle_input(message)
            # print(response)
            await websocket.send(json.dumps(response)) 

    except websockets.exceptions.ConnectionClosedOK:
        print("WebSocket client disconnected.")
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        if websocket in connected_clients:
            connected_clients.remove(websocket)

        # on new connection
        # await websocket.send(json.dumps({"image_url": "static/screenshots/off.jpg"}))
        # using app_context here because we want to use the url_for which needs the app context
        # with app.app_context():
        #     await websocket.send(json.dumps({"image_url": url_for('static', filename=f'screenshots/off.jpg') }))
        # await websocket.send(json.dumps({"image_url": get_image_url('off.jpg') }))

        # while True:
        #     try:
        #         message = await websocket.recv()
        #         print(f"Received: {message}")
        #         await websocket.send(json.dumps(SCREENS.getimage('off.jpg')))
        #     except websockets.exceptions.ConnectionClosedOK: # Handle client disconnections gracefully
        #         break
        #     except Exception as e:
        #         print(f"WebSocket error: {e}")
        #         break

## MESSAGE QUEUE MONITOR AND EVENT HANDLER
async def process_messages_queue():
    while True:
        await queue_has_items.wait()  # Wait for the event to be set
        queue_has_items.clear()      # Reset the event
        while not message_queue.empty(): # Process all messages in queue
            message = message_queue.get_nowait()
            for client in connected_clients:
                try:
                    await client.send(json.dumps(message))
                except Exception as e:
                    print(f"Error sending to client: {e}")
            message_queue.task_done()


## ASYNC IO THREAD - RUNS MULTIPLE THREAD IN ASYNC
def run_asyncio_loop():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) # Fix for windows
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        # Create and run both tasks concurrently
        tasks = asyncio.gather(websocket_server(), process_messages_queue())
        loop.run_until_complete(tasks)  # Run both until completion or stop_event is set
    finally:
        loop.close()

## MAIN APPLICATION
async def main():

    flask_thread = threading.Thread(target=flask_thread_function)
    flask_thread.daemon = True
    flask_thread.start()

    websocket_thread = threading.Thread(target=run_asyncio_loop)
    websocket_thread.daemon = True
    websocket_thread.start()


    while True:
        print("\n1.Type 'data 1' to change claim (1-2). Active data ID:", SCREENS.claim_data_id)
        print("2.Type 'livedata 1' to change live data parsing (0=Off, 1=On). Active live data parsing:", SCREENS.live_data_parsing)
        user_input = input("Type x to quit (Flask runs in background): ")

        if user_input == 'x':
            stop_event.set()
            print("Signaled Flask thread to stop. It will exit when ready.") # Informative message
            break

        elif user_input.startswith("data "):
            message = user_input[5:]
            SCREENS.set_claim_data_id(message)
            print('Data id set to: ', message)

        elif user_input.startswith("livedata "):
            message = user_input[9:]
            SCREENS.set_live_data_parsing(message)
            print('Live data parsing set to: ', message, '0=Off, 1=On')

        elif user_input.startswith("w "):
            message = user_input[2:]
            for client in connected_clients:
                await client.send(json.dumps({"message": message}))
                print(f"Sent to websocket clients: {message}")

        elif user_input.startswith("r "):
            message = user_input[2:]
            try:
                response = requests.post('http://localhost:5000/command', json={"message": message})
                print(f"REST API response: {response.json()}")
            except requests.exceptions.RequestException as e:
                print(f"Error sending to REST API: {e}")
        else:
            print(f"Local command: {user_input}")

if __name__ == "__main__":
    asyncio.run(main())