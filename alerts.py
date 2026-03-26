from twilio.rest import Client

ACCOUNT_SID = "YOUR_TWILIO_SID"
AUTH_TOKEN = "YOUR_TWILIO_TOKEN"

def send_alert():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(
        body="🚨 HIGH RISK ALERT! Take immediate action!",
        from_="+1234567890",
        to="+91XXXXXXXXXX"
    )