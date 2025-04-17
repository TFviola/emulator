from enum import Enum
from logger import Logger
from util.mock_emulator_data import switched_off, login, main_menu, first_workflow_queue, record_details, claim_details, select_options, workflow_images

class ScreenNames(Enum):
    OFF = "off"
    LOGIN = "login"
    MAIN_MENU = "main_menu"
    FIRST_WORKFLOW_QUEUE = "first_workflow_queue"
    RECORD_DETAILS = "record_details"
    CLAIM_DETAILS = "claim_details"
    SELECT_OPTIONS = "select_options"
    WORKFLOW_IMAGES = "workflow_images"

screens = {
    ScreenNames.OFF: {
        "image_url": "off.jpg",
        "navigations": {
            "start": ScreenNames.LOGIN
        },
        "extra_data": switched_off
    },
    ScreenNames.LOGIN: {
        "image_url": "login.jpg",
        "navigations": {
            "1": ScreenNames.MAIN_MENU,
            "9": ScreenNames.OFF
        },
        "extra_data": login
    },
    ScreenNames.MAIN_MENU: {
        "image_url": "main-menu.jpg",
        "navigations": {
            "1": ScreenNames.FIRST_WORKFLOW_QUEUE,
            "2": ScreenNames.MAIN_MENU,
            "3": ScreenNames.MAIN_MENU,
            "4": ScreenNames.MAIN_MENU,
            "5": ScreenNames.MAIN_MENU,
            "back": ScreenNames.LOGIN
        },
        "extra_data": main_menu
    },
    ScreenNames.FIRST_WORKFLOW_QUEUE: {
        "image_url": "first_workflow_queue.jpg",
        "navigations": {
            "1": ScreenNames.RECORD_DETAILS,
            "2": ScreenNames.FIRST_WORKFLOW_QUEUE,
            "3": ScreenNames.FIRST_WORKFLOW_QUEUE,
            "4": ScreenNames.FIRST_WORKFLOW_QUEUE,
            "5": ScreenNames.FIRST_WORKFLOW_QUEUE,
            "back": ScreenNames.MAIN_MENU
        },
        "extra_data": first_workflow_queue
    },
    ScreenNames.RECORD_DETAILS: {
        "image_url": "record_details.jpg",
        "navigations": {
            "a": ScreenNames.RECORD_DETAILS,
            "b": ScreenNames.RECORD_DETAILS,
            "c": ScreenNames.RECORD_DETAILS,
            "d": ScreenNames.CLAIM_DETAILS,
            "e": ScreenNames.RECORD_DETAILS,
            "f": ScreenNames.RECORD_DETAILS,
            "g": ScreenNames.RECORD_DETAILS,
            "h": ScreenNames.RECORD_DETAILS,
            "i": ScreenNames.RECORD_DETAILS,
            "j": ScreenNames.RECORD_DETAILS,
            "k": ScreenNames.RECORD_DETAILS,
            "l": ScreenNames.RECORD_DETAILS,
            "m": ScreenNames.RECORD_DETAILS,
            "n": ScreenNames.RECORD_DETAILS,
            "o": ScreenNames.RECORD_DETAILS,
            "back": ScreenNames.FIRST_WORKFLOW_QUEUE
        },
        "extra_data": record_details
    },
    ScreenNames.CLAIM_DETAILS: {
        "image_url": "claim_details.jpg",
        "navigations": {
            "m": ScreenNames.CLAIM_DETAILS,
            "p": ScreenNames.CLAIM_DETAILS,
            "r": ScreenNames.CLAIM_DETAILS,
            "f": ScreenNames.CLAIM_DETAILS,
            "v": ScreenNames.SELECT_OPTIONS,
            "o": ScreenNames.CLAIM_DETAILS,
            "back": ScreenNames.RECORD_DETAILS
        },
        "extra_data": None  # Will be populated from claim_details based on ID
    },
    ScreenNames.SELECT_OPTIONS: {
        "image_url": "select_options.jpg",
        "navigations": {
            "s": ScreenNames.SELECT_OPTIONS,
            "g": ScreenNames.SELECT_OPTIONS,
            "e": ScreenNames.SELECT_OPTIONS,
            "b": ScreenNames.SELECT_OPTIONS,
            "p": ScreenNames.SELECT_OPTIONS,
            "r": ScreenNames.SELECT_OPTIONS,
            "i": ScreenNames.WORKFLOW_IMAGES,
            "l": ScreenNames.SELECT_OPTIONS,
            "h": ScreenNames.SELECT_OPTIONS,
            "n": ScreenNames.SELECT_OPTIONS,
            "a": ScreenNames.SELECT_OPTIONS,
            "v": ScreenNames.SELECT_OPTIONS,
            "u": ScreenNames.SELECT_OPTIONS,
            "y": ScreenNames.SELECT_OPTIONS,
            "back": ScreenNames.CLAIM_DETAILS
        },
        "extra_data": select_options
    },
    ScreenNames.WORKFLOW_IMAGES: {
        "image_url": "workflow_images.jpg",
        "navigations": {
            "a": ScreenNames.WORKFLOW_IMAGES,
            "back": ScreenNames.SELECT_OPTIONS
        },
        "extra_data": workflow_images
    }
}

class Screens:
    def __init__(self):
        self.screens = screens
        self.current_screen = ScreenNames.OFF
        self.logger = Logger()
        self.claim_data_id = 1
        self.live_data_parsing = False

    def set_claim_data_id(self, id):
        self.claim_data_id = id

    def set_live_data_parsing(self, value):
        self.live_data_parsing = value

    def geturl(self, filename):
        return f'static/screenshots/{filename}'

    def navigate_to(self, screen_name):
        if screen_name in self.screens:
            self.current_screen = screen_name
            screen_data = self.screens[screen_name]
            
            # Handle claim details data based on ID
            extra_data = screen_data["extra_data"]
            if screen_name == ScreenNames.CLAIM_DETAILS:
                extra_data = claim_details
            
            return {
                "image_url": f"static/screenshots/{screen_data['image_url']}",
                "navigation_options": list(screen_data["navigations"].keys()),
                "screen_data": extra_data,
                "claim_data_id": self.claim_data_id,
                "is_live_data_parsing": self.live_data_parsing,
                "current_screen": screen_name.value
            }
        return None

    def process_navigation(self, key):
        current_screen_data = self.screens[self.current_screen]
        if key.lower() in current_screen_data["navigations"]:
            next_screen = current_screen_data["navigations"][key.lower()]
            return self.navigate_to(next_screen)
        return self.navigate_to(self.current_screen)

    def handle_input(self, input_str):
        input_str = str(input_str).strip()
        
        # Handle data ID changes
        if input_str.startswith('data '):
            try:
                new_id = int(input_str.split()[1])
                self.set_claim_data_id(new_id)
                return self.navigate_to(self.current_screen)
            except:
                pass

        # Handle live data parsing changes
        if input_str.startswith('livedata '):
            try:
                new_value = bool(int(input_str.split()[1]))
                self.set_live_data_parsing(new_value)
                return self.navigate_to(self.current_screen)
            except:
                pass

        input_str = input_str.lower()
        
        if input_str == "off":
            return self.navigate_to(ScreenNames.OFF)
        elif input_str == "start" or self.current_screen is None:
            return self.navigate_to(ScreenNames.LOGIN)

        current_screen_data = self.screens[self.current_screen]
        if input_str in current_screen_data["navigations"]:
            next_screen = current_screen_data["navigations"][input_str]
            return self.navigate_to(next_screen)
                
        print("Received invalid keystroke:", input_str)
        return self.navigate_to(self.current_screen)
