from enum import Enum
import json
from logger import Logger
from util.mock_emulator_data import (
    eligibility_main_menu,
    patient_search_selection,
    patient_details,
    search_patient_details,
    review_details
)

class ScreenNames(Enum):
    ELIGIBILITY_MAIN_MENU = "eligibility_main_menu"
    PATIENT_SEARCH_SELECTION = "patient_search_selection"
    PATIENT_DETAILS = "patient_details"
    SEARCH_PATIENT_DETAILS = "search_patient_details"
    REVIEW_DETAILS = "review_details"

screens = {
    ScreenNames.ELIGIBILITY_MAIN_MENU: {
        "image_url": "eligibility_main_menu.jpg",
        "navigations": {
            "1": ScreenNames.ELIGIBILITY_MAIN_MENU,
            "2": ScreenNames.PATIENT_SEARCH_SELECTION,
            "3": ScreenNames.ELIGIBILITY_MAIN_MENU,
            "4": ScreenNames.ELIGIBILITY_MAIN_MENU,
            "5": ScreenNames.ELIGIBILITY_MAIN_MENU,
            "6": ScreenNames.ELIGIBILITY_MAIN_MENU,
            "7": ScreenNames.ELIGIBILITY_MAIN_MENU,
            "8": ScreenNames.ELIGIBILITY_MAIN_MENU,
            "9": ScreenNames.ELIGIBILITY_MAIN_MENU
        },
        "mock_data": eligibility_main_menu
    },
    ScreenNames.PATIENT_SEARCH_SELECTION: {
        "image_url": "patient_search_selection.jpg",
        "navigations": {
            "Credentials": ScreenNames.PATIENT_DETAILS,
            "back": ScreenNames.ELIGIBILITY_MAIN_MENU
        },
        "mock_data": patient_search_selection
    },
    ScreenNames.PATIENT_DETAILS: {
        "image_url": "patient_details.jpg",
        "navigations": {
            "F3": ScreenNames.SEARCH_PATIENT_DETAILS,
            "back": ScreenNames.PATIENT_SEARCH_SELECTION
        },
        "mock_data": patient_details
    },
    ScreenNames.SEARCH_PATIENT_DETAILS: {
        "image_url": "search_patient_details.jpg",
        "navigations": {
            "F3": ScreenNames.REVIEW_DETAILS,
            "back": ScreenNames.PATIENT_DETAILS
        },
        "mock_data": search_patient_details
    },
    ScreenNames.REVIEW_DETAILS: {
        "image_url": "review_details.jpg",
        "navigations": {
            "back": ScreenNames.SEARCH_PATIENT_DETAILS
        },
        "mock_data": review_details
    }
}

class Screens:
    def __init__(self):
        self.screens = screens
        self.current_screen = ScreenNames.ELIGIBILITY_MAIN_MENU
        self.logger = Logger()
        self.claim_data_id = 1
        self.live_data_parsing = False

    def set_claim_data_id(self, id):
        self.claim_data_id = id

    def set_live_data_parsing(self, value):
        self.live_data_parsing = value

    def geturl(self, filename):
        return f'static/screenshots/{filename}'

    def get_screen_data(self, screen_name):
        """Get the JSON data for a specific screen"""
        if screen_name in self.screens:
            screen_data = self.screens[screen_name]
            try:
                # Parse the JSON string from mock_data
                mock_data = json.loads(screen_data["mock_data"])
                return {
                    "image_url": f"static/screenshots/{screen_data['image_url']}",
                    "navigation_options": list(screen_data["navigations"].keys()),
                    "screen_data": mock_data,
                    "claim_data_id": self.claim_data_id,
                    "is_live_data_parsing": self.live_data_parsing,
                    "current_screen": screen_name.value,
                    "screen": screen_name.value
                }
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON for screen {screen_name}: {e}")
                return None
        return None

    def navigate_to(self, screen_name):
        if screen_name in self.screens:
            self.current_screen = screen_name
            return self.get_screen_data(screen_name)
        return None

    def handle_input(self, input_str):
        if not input_str:
            return self.get_screen_data(self.current_screen)

        input_str = str(input_str).strip()
        
        # Handle special commands
        if input_str == "off" or input_str == "start":
            return self.navigate_to(ScreenNames.ELIGIBILITY_MAIN_MENU)
            
        # Handle data ID changes
        if input_str.startswith('data '):
            try:
                new_id = int(input_str.split()[1])
                self.set_claim_data_id(new_id)
                return self.get_screen_data(self.current_screen)
            except:
                pass

        # Handle live data parsing changes
        if input_str.startswith('livedata '):
            try:
                new_value = bool(int(input_str.split()[1]))
                self.set_live_data_parsing(new_value)
                return self.get_screen_data(self.current_screen)
            except:
                pass

        # Normalize command
        if input_str.upper() == 'F3':
            input_str = 'F3'
        elif input_str.lower() == 'back':
            input_str = 'back'

        # Get current screen's valid navigation options
        current_screen_data = self.screens[self.current_screen]
        valid_commands = current_screen_data["navigations"]

        # Check if command is valid for current screen
        if input_str in valid_commands:
            next_screen = valid_commands[input_str]
            return self.navigate_to(next_screen)
        
        # If command is invalid, log it and stay on current screen
        print(f"Invalid command '{input_str}' for screen '{self.current_screen.value}'")
        return self.get_screen_data(self.current_screen)
