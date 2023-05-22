# How To Run
to run this script you will need to create a python virtual environment and install requirements.txt

### Steps:
- Create a virtual environment `python -m venv virtual`
- Open environment `source virtual\bin\activate` or `virtual\Scripts\activate`
- run `python app.py`

### API Endpoints


POST `/api/extract_data`

    {'url': https://chat.whatsapp.com/JgNcXT9kdmb0Dw13XE331X'}
    
    [
        {"name":"MFX premium\ud83c\udfc1\ud83d\udcb0","profile_picture_url":"https://pps.whatsapp.net/v/t61.24694-24/345749483_786824916446928_8934328290416048859_n.jpg?ccb=11-4&oh=01_AdQP8KurtSR6LNsJu9SIQxyQxNIPUbb7waotKZV1eu8tDA&oe=6478568A"}
    ]
    
GET `/api/data`

    [
        {"name":"MFX premium\ud83c\udfc1\ud83d\udcb0","profile_picture_url":"https://pps.whatsapp.net/v/t61.24694-24/345749483_786824916446928_8934328290416048859_n.jpg?ccb=11-4&oh=01_AdQP8KurtSR6LNsJu9SIQxyQxNIPUbb7waotKZV1eu8tDA&oe=6478568A"}
    ]