import requests
from faker import Faker
from flask import Flask, render_template, request
from markupsafe import escape

from parameters_manager import ParametersManager

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('hello.html')


@app.route('/requirements')
def read_txt():
    path = 'requirements.txt'
    with open(path, 'r') as file:
        content = file.read()
    return render_template('requirements.html', content=content)


@app.route('/users/generate')
def show_users():
    fake = Faker()
    x = []
    quantity = escape(request.args.get('q', 0))
    if not quantity.isdigit() or int(quantity) < 0:
        return "Введіть додатнє число"
    int_quantity = int(quantity)
    quantity = int_quantity if int_quantity > 0 else 100
    for _ in range(quantity):
        user = {
            'name': fake.name(),
            'email': fake.email()
        }
        x.append(user)

    return render_template('users.html', users=x)


@app.route('/mean')
def read_parameters():
    parameters_manager = ParametersManager()
    result = parameters_manager.read()
    return result


@app.route('/space')
def get_cosmonauts():
    url = 'http://api.open-notify.org/astros.json'
    get_request = requests.get(url)
    if get_request.status_code == 200:
        res = get_request.json()
        number = res.get("number")
        content = number
        return render_template('space.html', content=content)
    else:
        return None


if __name__ == '__main__':
    app.run()
