from flask import Flask, render_template, request
from flask_mail import Mail, Message
import json

app = Flask(__name__)

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['email'],
    MAIL_PASSWORD=params['password']
)
mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    msg = Message(subject='Contact Form Portfolio',
                  sender=email,
                  recipients=[params['email']])
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)
    # text = 'Message sent successfully! Go back'
    # return text
    return render_template('success.html')

    # return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
