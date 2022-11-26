from flask import Flask
import pandas as pd


app = Flask(__name__)


@app.route("/")
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
