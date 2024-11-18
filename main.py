import os
import csv
import re
import requests
from PIL import Image
import pytesseract

API_KEY = '5ef96dd7a7c048bdb4767a911ce12407'  # Replace with your API key
API_URL = 'https://api.opencagedata.com/geocode/v1/json'  # OpenCage Geocoding API

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

def extract_lat_lon_from_text(text):
    lat_lon_pattern = re.compile(r'(\d+\.\d+)[^\d]*(\d+\.\d+)')
    match = lat_lon_pattern.search(text)

    if match:
        lat, lon = match.groups()
        return float(lat), float(lon)
    return None, None

def reverse_geocode(lat, lon):
    if lat is None or lon is None:
        print(f"Invalid coordinates: lat={lat}, lon={lon}")
        return "Invalid Coordinates"

    # OpenCage API request
    params = {
        'q': f"{lat},{lon}",
        'key': API_KEY,
        'language': 'en'
    }

    try:
        response = requests.get(API_URL, params=params)

        data = response.json()

        if response.status_code == 200 and data['results']:
            return data['results'][0]['formatted']
        else:
            print(f"Error fetching address: {data.get('status', {}).get('message', 'Unknown error')}")
            return "No Address Found"
    except Exception as e:
        print(f"Error during geocoding: {e}")
    return "Unknown Location"

def extract_gps_and_save_to_csv(image_folder, output_csv):
    folder_name = os.path.basename(image_folder)  # Get folder name for description
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['WKT', 'name', 'description'])  # CSV Header

        for image_name in os.listdir(image_folder):
            if image_name.lower().endswith(('jpg', 'jpeg', 'png')):
                image_path = os.path.join(image_folder, image_name)
                print(f"Processing image: {image_path}")

                image = Image.open(image_path)
                text = pytesseract.image_to_string(image)

                lat, lon = extract_lat_lon_from_text(text)

                if lat and lon:
                    location_name = reverse_geocode(lat, lon)

                    wkt_point = f"POINT ({lon} {lat})"

                    writer.writerow([wkt_point, location_name, folder_name])
                    print(f"Coordinates for {image_name}: {lat}, {lon}, Location: {location_name}")
                else:
                    print(f"No valid GPS data found in text for image: {image_name}")

image_folder = 'CARTER_ROAD'  # Replace with your folder
output_csv = 'output.csv'

extract_gps_and_save_to_csv(image_folder, output_csv)
