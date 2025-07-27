import requests
from datetime import datetime

urls = [
    "https://candidate-screeneerpro.streamlit.app/",
    "https://screenerpro.streamlit.app/"
]

for url in urls:
    try:
        res = requests.get(url)
        print(f"[{datetime.now()}] Pinged {url} - Status: {res.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] Error pinging {url}: {e}")
