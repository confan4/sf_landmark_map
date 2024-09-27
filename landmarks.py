import requests
from urllib.parse import quote

def get_sf_landmarks():
    landmarks = [
        "Golden Gate Bridge",
        "Alcatraz Island",
        "Fisherman's Wharf",
        "Chinatown",
        "Lombard Street",
        "Ghirardelli Square",
        "Palace of Fine Arts",
        "Coit Tower",
        "Transamerica Pyramid",
        "San Francisco Museum of Modern Art"
    ]

    landmark_data = []

    for landmark in landmarks:
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{quote(landmark)}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            landmark_data.append({
                "name": data["title"],
                "description": data["extract"],
                "coordinates": get_coordinates(data["title"])
            })

    return landmark_data

def get_coordinates(landmark):
    # This is a simplified version. In a real application, you'd use a geocoding service
    # or fetch the coordinates from Wikipedia's API.
    coordinates = {
        "Golden Gate Bridge": [37.8199, -122.4783],
        "Alcatraz Island": [37.8270, -122.4230],
        "Fisherman's Wharf": [37.8080, -122.4177],
        "Chinatown": [37.7941, -122.4078],
        "Lombard Street": [37.8021, -122.4187],
        "Ghirardelli Square": [37.8056, -122.4222],
        "Palace of Fine Arts": [37.8029, -122.4484],
        "Coit Tower": [37.8024, -122.4058],
        "Transamerica Pyramid": [37.7952, -122.4028],
        "San Francisco Museum of Modern Art": [37.7858, -122.4008]
    }
    return coordinates.get(landmark, [37.7749, -122.4194])  # Default to SF center if not found

