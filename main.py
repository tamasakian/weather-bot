import requests
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
from config import *

TARGET_HOURS = {6, 9, 12, 15, 18, 21}

def get_weather():
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "lat": LATITUDE,
        "lon": LONGITUDE,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ja"
    }
    res = requests.get(url, params=params)
    data = res.json()
    lines = []
    for item in data["list"]:
        dt = datetime.fromtimestamp(item["dt"])
        if dt.hour in TARGET_HOURS:
            temp = item["main"]["temp"]
            description = item["weather"][0]["description"]
            lines.append(f"{dt.strftime('%H時')}：{description}、{temp:.1f}度")
        if len(lines) == 6:
            break
    return "\n".join(lines)

def send_email(message):
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = "天気情報"
    msg["From"] = FROM_EMAIL
    msg["To"] = TO_EMAIL
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    weather_info = get_weather()
    send_email(weather_info)