import base64
import json
import os
import time
from flask import jsonify
import pyautogui
from chatgpt_initialize import get_chatgpt_response

class ScreenAnalyzer:
    def __init__(self, config=None):
        configuration = {
            "output_format": {
                "verbose": True,
                "text_mode": True
            },
            "screenshot_region": {
                "image_x": 50,
                "image_y": 170,
                "image_width": 860,
                "image_height": 470,
            }
        }

        if not config is None:
            self.configuration = {
                **configuration,
                **config
            }
        else:
            self.configuration = configuration

        self.prompts = {
"json_mode": """
You are a senior business process executive trainer that uses Mainframe application. Your task is to generate a properly formatted text data that has the label : value matched. Keep  the labels as you see on the screen. Assume your output will be consumed by automation tools and junior executives.

Give importance to:
1. navigation options
2. Notification and alerts
3. Input fields with *focussed state*
4. Put tabular data in groups and order them properly
5. Have one field that has a concise summary (just a sentence) of what this screen is meant for and what user is expected to do.
""",

"text_mode": """
You are a senior business process executive trainer that uses Mainframe application. Your task is to generate a properly formatted JSON data that has the values matched. Keep  the labels as you see on the screen. Assume your output will be consumed by automation tools and junior executives.

Give importance to:
1. navigation options
2. Notification and alerts
3. Input fields with *focussed state*
4. Put tabular data in groups and order them properly
5. Have one field that has a concise summary (just a sentence) of what this screen is meant for and what user is expected to do.
"""
        }

    def take_screenshot_and_analyze(self):
        try:
            imgcfg = self.configuration["screenshot_region"]
            image_x = imgcfg["image_x"]
            image_y = imgcfg["image_y"]
            image_width = imgcfg["image_width"]
            image_height = imgcfg["image_height"]

            ocfg = self.configuration["output_format"]
            verbose = ocfg["verbose"]
            text_mode = ocfg["text_mode"]

            prompt = self.prompts["json_mode"]
            if text_mode == True:
                prompt = self.prompts["text_mode"]

            if verbose == True:
                prompt = f"{prompt}\nAdd a short concise description for navigation options"

            # Capture the screenshot
            screenshot_filename = f"screenshot_{time.strftime('%Y%m%d%H%M%S')}.png"
            screenshots_dir = "temp"
            screenshot_path = os.path.join(screenshots_dir, screenshot_filename)

            pyautogui.screenshot(screenshot_path, region=(image_x, image_y, image_width, image_height))

            print("Sending screenshot to ChatGPT...")
            response = self.generate_text_from_image(screenshot_path, prompt)
            return response

        except Exception as ex:
            print('Exception capture screenshot', ex)
            return {"error": str(ex)}

    def generate_text_from_image(self, image_path, prompt, model_name="gpt-3.5-turbo"):
        try:
            with open(image_path, "rb") as image_file:
                image_data = base64.b64encode(image_file.read()).decode('utf-8')
            
            full_prompt = f"{prompt}\n\nImage data: {image_data}"
            response = get_chatgpt_response(full_prompt)
            
            if response:
                try:
                    return json.loads(response)
                except:
                    return {"text": response}
            else:
                return {"error": "Failed to get response from ChatGPT"}

        except Exception as e:
            print(f"Error in generate_text_from_image: {e}")
            return {"error": str(e)}