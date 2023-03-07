
import requests

# Replace with your API key
api_key = 'K89089545688957'
url_api = 'https://api.ocr.space/parse/image'

# Set the file path to upload
file_path = r"C:\Users\umaRf\OneDrive\Desktop\Transfer\Muhammad Khan (2).pdf"

# Set language parameter if needed
language = 'eng'

# Set other parameters if needed
is_overlay_required = False

# Set the HTTP headers for the POST request
headers = {'apikey': api_key}

# Set the payload for the POST request
payload = {
    'language': language,
    'isOverlayRequired': is_overlay_required,
}

# Upload the file and get the response
with open(file_path, 'rb') as f:
    response = requests.post(url_api, headers=headers, data=payload, files={'image': f})

# Parse the response JSON
response_json = response.json()

# Print the response JSON
print(response_json)