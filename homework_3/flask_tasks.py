import csv
from http import HTTPStatus

import requests
from faker import Faker
from flask import Flask, Response
from webargs import validate, fields
from webargs.flaskparser import use_kwargs

app = Flask(__name__)


@app.route("/")
def sources():
    return "<p>Sources:<br>1. /generate_students<br>2. /bitcoin_rate</p>"


@app.route("/generate_students")
@use_kwargs(
    {
        "count": fields.Int(
            missing=5,
            validate=[validate.Range(min=1, max=1000)]
        ),
    },
    location="query"
)
def generate_students(count):
    fake = Faker()
    students_info = list()
    # generate students info
    for _ in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password()
        birthday = fake.date_of_birth()
        students_info.append([first_name, last_name, email, password, birthday])
    # create csv with info
    with open('students_info.csv', 'w', newline='') as csvfile:
        fieldnames = ["first_name", "last_name", "email", "password", "birthday"]
        writer = csv.DictWriter(csvfile, dialect="excel", fieldnames=fieldnames)
        writer.writeheader()
        for student_info in students_info:
            writer.writerow({'first_name': student_info[0], 'last_name': student_info[1], "email": student_info[2],
                             "password": student_info[3], "birthday": student_info[4]})
    return (f"<p>Name: {student_info[0]}, Surname: {student_info[1]}, Email: {student_info[2]}, Password:"
            f" {student_info[3]}, Birthday: {student_info[4]}</p> <br>" for student_info in students_info)


@app.route("/bitcoin_rate")
@use_kwargs(
    {
        "currency": fields.Str(
            missing="USD",
        ),
    },
    location="query"
)
def get_bitcoin_value(currency):
    rates_url = f"https://bitpay.com/api/rates/{currency}"
    rates_result = requests.get(rates_url, {})
    if rates_result.status_code not in (HTTPStatus.OK, ):
        return Response(
            "ERROR: Something went wrong.",
            status=rates_result.status_code
        )
    rates_result = rates_result.json()
    currencies_url = "https://bitpay.com/currencies"
    currencies_result = requests.get(currencies_url, {})
    if currencies_result.status_code not in (HTTPStatus.OK,):
        return Response(
            "ERROR: Something went wrong.",
            status=currencies_result.status_code
        )
    currencies_result = currencies_result.json()
    rate = rates_result.get("rate", "?")
    symbol = currency
    for entry in currencies_result.get("data", {}):
        if currency == entry.get("code", {}):
            symbol = entry.get("symbol", currency)
            break
    return f"The bitcoin rate is {rate}{symbol}"


app.run(port=5001, debug=True)
