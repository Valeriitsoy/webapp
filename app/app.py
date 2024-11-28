from flask import Flask, request, make_response
from datetime import datetime

app = Flask(__name__)

author = 'Tsoi Valera'


@app.route('/date', methods=['GET'])
def get_date():
    current_date = datetime.now().strftime('%d.%m.%Y')
    response = make_response(current_date)
    response.headers['X-Author'] = author
    return response


@app.route('/hello', methods=['POST'])
def say_hello():
    name = request.form.get('name')
    if not name:
        response = make_response("Missing name parameter", 400)
        response.headers['X-Author'] = author
        return response

    response = make_response(f'<html><body> <h3>Hello, {name}!</h3> </body></html>')
    response.set_cookie('name', name)
    response.headers['X-Author'] = author
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")
