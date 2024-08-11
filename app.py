from flask import Flask, render_template

app = Flask(__name__)
posts = [
    {
        'author': 'Nader',
        'body': 'Beautiful day in Python.',
        'date': 'April',
    }
]
@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about')
def about_page():
    return render_template('route.html')

if __name__ == '__main__':
    app.run(debug=True)