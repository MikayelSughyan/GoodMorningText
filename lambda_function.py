from openai import OpenAI
from twilio.rest import Client
from dotenv import load_dotenv
import os

def lambda_handler(event, context):
    load_dotenv()
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are the boyfriend in a a 6 month relationship with Emily, skilled in nice good morning texts."},
        {"role": "user", "content": "Write a new, fresh good morning text to Emily."}
    ]
    )

    messageToSend = completion.choices[0].message.content

    twilioClient = Client(os.environ['TWILIO_SID'], os.environ['TWILIO_AUTH_TOKEN'])

    message = twilioClient.messages.create(
            body=messageToSend, 
            from_ = os.environ['TWILIO_PHONE_NUMBER'],
            to = os.environ['RECIPIENT_PHONE_NUMBER']
        )

def main():
    lambda_handler()

if __name__ == "__main__":
    main()

