import requests

API_KEY ="S332dbec92fbec5e1f966ec2580f03898"

def get_weather(city="Chennai"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    return {
        "temperature": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "pressure": res["main"]["pressure"]
    }
