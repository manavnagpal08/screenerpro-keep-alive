import requests
from datetime import datetime

url = "https://candidate-screeneerpro.streamlit.app/"

try:
    res = requests.get(url)
    print(f"[{datetime.now()}] Pinged ScreenerPro - Status {res.status_code}")
except Exception as e:
    print(f"[{datetime.now()}] Error: {e}")
