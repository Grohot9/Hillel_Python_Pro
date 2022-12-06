import random
import string

import pandas as pd
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def hello_mykhailo():
    return "<p>Hello, Mykhailo!</p>"


@app.route("/generate_password")
def generate_password() -> str:
    """
    from 10 to 20 chars
    upper and lower case
    """
    password_length = random.randint(10, 20)
    available_characters = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)
    password = "".join([random.choice(available) for available in available_characters])
    password += "".join(random.choices(random.choice(available_characters),
                                       k=password_length - len(available_characters)))
    return password


@app.route("/avarage_statistics")
def calculate_average(filename="hw.csv"):
    """
    csv file with students
    1.calculate average high
    2.calculate average weight
    """
    df = pd.read_csv(filename)
    average_high = df.mean()[1]
    average_weight = df.mean()[2]
    return f"<p>1. Average High: {average_high}<br>2. Average Weight: {average_weight}</p>"


app.run(port=5001, debug=False)
