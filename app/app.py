from flask import Flask, request, make_response, render_template_string
from datetime import datetime

app = Flask(__name__)

author = 'Tsoi Valera'


@app.route('/', methods=['GET'])
def index():
    """Передать в name=<script>alert('АТАКА XSS')</script>"""
    html = '''
    <html>
        <body>
            <h3>Введите имя:</h3>
            <form method="POST" action="/hello">
                <input type="text" name="name" required placeholder="Введите имя">
                <button type="submit">Отправить</button>
            </form>
        </body>
    </html>
    '''
    return render_template_string(html)


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
