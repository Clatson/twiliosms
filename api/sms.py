import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

app = Flask(__name__)

# Load Twilio credentials from environment variables
TWILIO_SID = os.getenv('ACdb4c1c9d1e3b15282f909ea1545991c5')
TWILIO_AUTH_TOKEN = os.getenv('faf71ce4b022272970e5a1a580978be4')
TWILIO_PHONE_NUMBER = os.getenv('+18174382668')

# Initialize Twilio client
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

@app.route('/', methods=['POST'])
def sms_reply():
    # Get the message the user sent to your Twilio number
    incoming_msg = request.form.get('Body').strip().lower()

    # Create a Twilio response object
    response = MessagingResponse()

    # Respond based on the incoming message
    if 'hello' in incoming_msg:
        response.message("Hi there! How can I help you?")
    elif 'help' in incoming_msg:
        response.message("Sure! What do you need help with?")
    elif 'bye' in incoming_msg:
        response.message("Goodbye! Have a great day!")
    else:
        response.message("Sorry, I didn't understand that. Please type 'help' for assistance.")

    return str(response)

@app.route('/send-sms', methods=['POST'])
def send_sms():
    to = request.form.get('to')  # The recipient's phone number
    message_body = request.form.get('message')  # The message to send

    # Send the SMS via Twilio
    client.messages.create(
        body=message_body,
        from_=TWILIO_PHONE_NUMBER,
        to=to
    )

    return "Message sent!"

if __name__ == '__main__':
    app.run(debug=True)
