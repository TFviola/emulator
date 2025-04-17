import asyncio
import threading

from emulator_client import EmulatorClient

stop_event = threading.Event()
client = EmulatorClient()

async def main():
    while not stop_event.is_set():
        command = input("Enter command (or 'x' to exit): ")
        if command.lower() == 'x':
            stop_event.set()
            break

        user_intent = command
        result = client.process_command(user_intent)
        print("Agent Output:", result)

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