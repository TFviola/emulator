import asyncio
import base64
import json
import threading
import time
from flask import jsonify
import requests

stop_event = threading.Event()

class EmulatorClient:
    def __init__(self):
        self.REST_API_URL = "http://localhost:5000/api"
        self.current_screen = None
        self.typed_text = ""

    def get_screen(self, screen_code):
        """Get screen information by screen code"""
        try:
            response = requests.get(f"{self.REST_API_URL}/screen/{screen_code}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error getting screen: {e}")
            return {"error": str(e)}

    def navigate(self, screen_code, navigation_key):
        """Navigate using screen code and navigation key"""
        try:
            response = requests.post(f"{self.REST_API_URL}/navigate", 
                json={
                    "screen_code": screen_code,
                    "navigation_key": navigation_key
                })
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error navigating: {e}")
            return {"error": str(e)}

    def type_text(self, screen_code, text):
        """Simulate typing text on screen"""
        try:
            response = requests.post(f"{self.REST_API_URL}/type", 
                json={
                    "screen_code": screen_code,
                    "text": text
                })
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error typing text: {e}")
            return {"error": str(e)}

    def process_command(self, command):
        """Process various commands including navigation and typing"""
        try:
            # Check if it's a navigation command
            if command.startswith("NAV:"):
                _, screen_code, nav_key = command.split(":")
                return self.navigate(screen_code, nav_key)
            # Check if it's a typing command
            elif command.startswith("TYPE:"):
                _, screen_code, text = command.split(":")
                return self.type_text(screen_code, text)
            # Default to screen request
            else:
                return self.get_screen(command)
        except Exception as e:
            print(f"Error processing command: {e}")
            return {"error": str(e)}

    def analyze_screen(self, screen_code):
        """Get detailed screen analysis"""
        try:
            response = requests.get(f"{self.REST_API_URL}/analyze/{screen_code}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error analyzing screen: {e}")
            return {"error": str(e)}
