from flask import Flask, flash, render_template, session, redirect, request, url_for
from dotenv import load_dotenv
from twilio.rest import Client
from wtforms import form
import os

from pathlib import Path

env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)


twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
twilio_accnt_sid = os.getenv(' TWILIO_ACC_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(twilio_accnt_sid, twilio_auth_token)
print(twilio_accnt_sid)
print(twilio_auth_token)
print(twilio_phone_number)


app = Flask(__name__)
app.secret_key = "super secret key"


def send_message(to, body):
    msg = client.messages.create(
        body=body,
        from_=twilio_phone_number,
        to=to
    )
    messages = []
    messages.append(msg)
    return messages


def get_messages():
    my_texts = []
    messages_history = client.messages.list(from_=twilio_phone_number)
    print(messages_history)
    for messages in messages_history:
        my_texts.append(messages)
        print("--------------____--------------------------------  > ", len(my_texts))
        return messages


def del_messages():
    target = client.messages().delete()
    flash("Hi, all messages are deleted")


@app.route('/')
def helloJay():
    messages = get_messages()
    return render_template('textIT.html', messages=messages)


@app.route("/sendmessage", methods=["POST", "GET"])
def result():
    messages = get_messages()
    print(len(messages))
    if request.method == "POST":
        sender = request.form["sender"]
        my_message = request.form["the_message"]
        phone_number = request.form["target_number"]
        body = f'{sender} says: {my_message}. '
        send_message(phone_number, body)
        flash("Message sent!")

        return render_template("textIT.html", result=phone_number, messages=messages)


@app.route("/history")
def history():
    counter = session.get('counter', 0)
    counter += 1
    session['counter'] = counter
    the_senders_name = request.form["sender"]
    the_senders_no = request.form["target_number"]
    message = '{} : {} , has messaged {} {} times.'.format(
        the_senders_name, the_senders_no, request.values.get('To'), counter)
    return render_template("maintemp.html", message=str(message))


@app.route("/mine", methods=["GET"])
def get_text():
    messages = get_messages()

    print("______-------------------------------------")
    print(type(messages))
    for mes in messages.body:
        print(mes)

    return render_template("maintemp.html", messages=messages)


if __name__ == '__main__':
    app.run(debug=True)
