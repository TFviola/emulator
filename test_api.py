import requests
import json

def test_screen_api(screen_code):
    try:
        response = requests.get(f'http://localhost:5000/api/screen/{screen_code}')
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Pretty print the JSON response
        print(f"\nTesting screen: {screen_code}")
        print("Status Code:", response.status_code)
        print("Response:")
        print(json.dumps(response.json(), indent=2))
        
    except requests.exceptions.RequestException as e:
        print(f"Error testing {screen_code}: {e}")

if __name__ == "__main__":
    # Test different screens
    screens = [
        "ELIGIBILITY_MAIN_MENU",
        "PATIENT_SEARCH_SELECTION",
        "PATIENT_DETAILS",
        "SEARCH_PATIENT_DETAILS",
        "REVIEW_DETAILS"
    ]
    
    for screen in screens:
        test_screen_api(screen) 