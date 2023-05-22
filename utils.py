import os
import requests
from bs4 import BeautifulSoup
import json
import re

def extract_group_info(url):
    try:
        
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        group_name = soup.find('h3', class_='_9vd5 _9scr').get_text()
        group_avatar = soup.find('img', class_='_9vx6')['src']

        return {'name': group_name, 'group_profile': group_avatar}
    except Exception as e:
        print(str(e))


def append_to_json_file(file_path, data):
    # Check if the file exists
    file_exists = os.path.isfile(file_path)

    if not file_exists:
        # Create a new file and write the data
        with open(file_path, 'w') as file:
            json.dump([data], file, indent=4)
    else:
        # Read the existing data from the file
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

        # Append the new data to the existing data
        existing_data.append(data)

        # Write the updated data back to the file
        with open(file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)


def is_valid_whatsapp_group_url(url):
    # Regular expression pattern to match WhatsApp group URLs
    pattern = r'^https?://chat.whatsapp.com/([A-Za-z0-9-]+)$'

    # Match the URL against the pattern
    match = re.match(pattern, url)

    return match 

# Provide the URL of the WhatsApp groups page
url = 'https://chat.whatsapp.com/JgNcXT9kdmb0Dw13XE331X'  


