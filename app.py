from flask import Flask

app = Flask(__name__)


@app.route('/')

@app.route('/home')
def home_page():  # put application's code here
    return '<h2>Home Page</h2>'

def hello_world():  # put application's code here
    return '<h2>Hello Niggas</h2>'


@app.route('/about')
def about_page():  # put application's code here
    return '<h2>About Page</h2>'


if __name__ == '__main__':
    app.run(debug=True)
