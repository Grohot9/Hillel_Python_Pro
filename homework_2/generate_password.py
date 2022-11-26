from flask import Flask
import random as rnd
import string


app = Flask(__name__)


@app.route("/")
def generate_password() -> str:
    """
    from 10 to 20 chars
    upper and lower case
    """
    password_length = rnd.randint(10, 20)
    available_characters = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)
    password = "".join([rnd.choice(available) for available in available_characters])
    for _ in range(password_length - len(available_characters)):
        password += str(rnd.choice(rnd.choice(available_characters)))
    return password


app.run(port=5001, debug=False)
