import asyncio
import base64
import threading
import time
import requests
import pyautogui
import os
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import openai
from util import parsing_prompt
from dotenv import load_dotenv
from chatgpt_initialize import get_chatgpt_response

load_dotenv()

REST_API_URL = "http://localhost:5000/command"
SCREENSHOT_FILENAME = "screenshots/tempscreenshot.png"

stop_event = threading.Event()

def process_command(command):
    try:
        # 1. Call REST API
        print(f"Calling REST API for message: {command}")
        response = requests.post(REST_API_URL, json={"message": command})  # Adapt request as needed
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        rest_response = response.json()  # Parse JSON response
        print(f"REST API Response: {rest_response}")

        print('SLEEPING 5 seconds before next screenshot')
        time.sleep(5)

        try:
            image_x = 50
            image_y = 170
            image_width = 860
            image_height = 470

            # 2. Capture the screenshot
            screenshot_filename = f"screenshot_{time.strftime('%Y%m%d%H%M%S')}.png"
            screenshots_dir = "screenshots/temp"
            screenshot_path = os.path.join(screenshots_dir, screenshot_filename)

            pyautogui.screenshot(screenshot_path, region=(image_x, image_y, image_width, image_height))

            print("Sending screenshot to ChatGPT...")
            prompt = """
                Analyse the given image and tell me all you know about this screen. Do not give intro statement, just your observation. Assume you are a process trainer training new employees on the business process and how to use this tool. Prepare a JSON on the data, more like a one liner. An concise instructions with commands available on screen in sentences that screen automation tools can understand.

                **CRITICAL INSTRUCTION:** If screen asks for 'user code' or 'password' instruction to use one word 'CREDENTIALS'* and override all screen instruction with this command only.
            """
            response = generate_text_from_image(screenshot_path, prompt)
            print(f"ChatGPT Response: {response}")

            return response

        except Exception as ex:
            print('Exception capture screenshot', ex)
            return {"error": str(ex)}

    except requests.exceptions.RequestException as e:
        print(f"Error calling REST API: {e}")
        return {"error": str(e)}
    except Exception as e:
        print(f"An error occurred: {e}")
        return {"error": str(e)}

def generate_text_from_image(image_path, prompt):
    try:
        with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
        
        full_prompt = f"{prompt}\n\nImage data: {image_data}"
        response = get_chatgpt_response(full_prompt)
        
        if response:
            return response
        else:
            return "Failed to get response from ChatGPT"

    except Exception as e:
        print(f"Error in generate_text_from_image: {e}")
        return str(e)

def orchestrator_agent(user_prompt):
    """Orchestrates actions based on user prompt and screen analysis (using process_command directly)."""

    def execute_command(command):
        """Executes a command and returns the updated screen information."""
        return process_command(command)

    tools = [
        Tool(
            name="ExecuteCommand",
            func=execute_command,
            description="Executes a command on the application and returns the resulting screen information (including text extracted from the screenshot). Input should be a string representing the command to be executed. Use this to interact with the application and change its state.",
        ),
    ]

    # Initialize OpenAI LLM
    llm = OpenAI(temperature=0)

    prompt_template = """You are an agent that interacts with a software application.
    You receive a user request and your goal is to fulfill that request by executing commands. 
    From the screen options, you choose the best command to use and call tools to perform next step.

    Here are the tools you can use:
    {tools}

    Current screen information: {screen_info}

    User request: {user_request}

    Thought: What should I do? Always compare if you are sidetracking with orignal user request
    Action: The action to take. Use one of: {tool_names}
    Action Input: The input to the action.

    Observation: The result of the action (the updated screen information). This will be long, so just give a one liner summary of the observation, maybe title and summarize it

    ... (repeat Thought/Action/Action Input/Observation steps as needed) ...

    Final Answer: The final answer to the user request. If you have achieved the goal, describe the outcome and send command "OFF" and exit. If you are unable to fulfill the request, explain why.

    **CRITICAL RULE:** Never try same command twice.
    """

    prompt = PromptTemplate(
        template=prompt_template, 
        input_variables=["user_request", "screen_info", "tools", "tool_names", "input"]
    )

    agent = initialize_agent(
        tools,
        llm,
        agent="zero-shot-react-description",
        verbose=True,
        prompt=prompt,
        handle_parsing_errors=True
    )

    initial_screen_info = process_command("off")

    try:
        result = agent.run(
            user_request=user_prompt, 
            screen_info=initial_screen_info, 
            tools=tools, 
            tool_names=", ".join([tool.name for tool in tools]),
            input=user_prompt
        )
        return result
    except Exception as e:
        return f"An error occurred: {e}"

image_parsing_prompt = """You are a senior business process executive trainer that uses Mainframe application. Your task is to analyze the given screen and generate a properly formatted JSON data. Keep the key names as you see on the screen. Assume your output will be consumed by automation tools and junior executives. 

Different screen layouts to look out for:
1. Header information at top
2. Tabular data below, another summary tabular data below that
3. Tabbed view, where left column is the label and right panels contains the data
4. A single tabular data

Give importance to:
1. Navigation options
2. Notification and alerts
3. Input fields with *focused state* 
4. Put tabular data or list of items in an array of objects
5. Have one field that has a concise summary of what this screen is meant for and what user is expected to do
6. Always have "Instruction" key and give clear instruction what is and can be done on this screen. What keys can be pressed for action. Prioritize shortcut and option keys over using arrow navigation

Example Instruction:
1. You have 2 fields active
2. Current focus is on Username field
3. Start typing to type username
4. Press tab to go to next input which is password
5. You can repeat this loop for your actions
6. When you are done you press key (choose from the navigation option)
7. When multiple navigation exists, example arrow keys or direct option selection, always choose one. And prioritize direct approach, which is selecting the option directly

Example format:
{
  "summary": "This screen displays claim details and allows users to view information such as claim status, charges, payments, patient and provider details.",
  "CLAIM INFORMATION": {
    "TY": "MM",
    "CLAIM NUMBER": "225-014871-00",
    "STATUS OF CLAIM": "ΡΕΝΗ 02/18/25 REUBEN",
    "RECEIVED": "02/11/25",
    "INCURRED": "01/23/25",
    "PLAN ID": "790136A",
    "EFFECTIVE": "02/01/17",
    "DGN": "R06",
    "DESCRIPTION": "Abnormalities o",
    "ICD": "R06.02",
    "YEAR": "2025",
    "UND/GROUP CODES": "790 790136",
    "NETWK": "CMA",
    "CLAIM SOURCE": "EDI 02/12/25"
  },
  "CLAIM DETAILS": [
    {
      "BEN": "780",
      "FROM DOS": "01/23/25",
      "VISIT": "1",
      "CHARGE AMT": "1096.60",
      "DISALLOWED": "578.53",
      "DEDUCTIBLE": ".00",
      "PCT": "100",
      "PAYMENT": "518.07",
      "type": "P"
    },
    {
      "BEN": "780",
      "FROM DOS": "01/23/25",
      "VISIT": "0",
      "CHARGE AMT": "172.32",
      "DISALLOWED": "29.56",
      "DEDUCTIBLE": ".00",
      "PCT": "100",
      "PAYMENT": "142.76",
      "type": "P"
    },
    {
      "BEN": "780",
      "FROM DOS": "01/23/25",
      "VISIT": "0",
      "CHARGE AMT": "40.16",
      "DISALLOWED": "40.16",
      "DEDUCTIBLE": ".00",
      "PCT": "0",
      "PAYMENT": ".00",
      "type": "P"
    },
    {
      "BEN": "780",
      "FROM DOS": "01/23/25",
      "VISIT": "0",
      "CHARGE AMT": "133.91",
      "DISALLOWED": "133.91",
      "DEDUCTIBLE": ".00",
      "PCT": "0",
      "PAYMENT": ".00",
      "type": "P"
    }
  ],
  "TOTALS": {
    "CHARGE AMT": "1442.99",
    "DISALLOWED": "782.16",
    "DEDUCTIBLE": ".00",
    "PAYMENT": "660.83"
  },
  "ADJUSTMENTS": {
    "ADJ": ".00",
    "COB ADJ": ".00",
    "W/HOLD": ".00",
    "TOT": ".00"
  },
  "PARTY INFORMATION": {
    "PATIENT": {
      "TAX ID": "997314611",
      "EMPLOYEE/PATIENT": "WHITE, ALVIN / (Self)"
    },
    "PROVIDER": {
      "TAX ID": "251799853",
      "PROVIDER": "SUPERIOR AMBULANCE SERVICE INC"
    },
    "ALT PAYEE": null,
    "CHECK NO": null,
    "NET PAYMENT": [".00", "660.83", ".00", "660.83"]
  },
  "NAVIGATION": {
    "Back": ScreenNames.AW_Jobs,
    "SELECT": "Choose an option",
    "OPTIONS": [
      "(M)ain",
      "(P)rior",
      "(R)esume",
      "(U)npend",
      "(V)iew",
      "(O)ptions",
      "(F)ind"
    ],
    "focussed": "Y"
  },
  "ALERTS": {
    "IMAGE AVAILABLE": true,
    "E-PAY INFO": "--- >",
    "CLAIM NOTES EXIST": true
  }
}

*Output Guide*
1. Use null for null values
2. Use boolean values true or false
"""

async def main():
    
    
    text = generate_text_from_image("static/screenshots/one.jpg", image_parsing_prompt)
    print(text)

    # while not stop_event.is_set():
    #     command = input("Enter command (or 'x' to exit): ")
    #     if command.lower() == 'x':
    #         stop_event.set()
    #         break

    #     # result = await process_command(command)

    #     user_intent = command
    #     result = orchestrator_agent(user_intent)
    #     print("Agent Output:", result)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        print("Cleaning up...")
        stop_event.set()
        # ... any other cleanup ...
    print("Application finished.")