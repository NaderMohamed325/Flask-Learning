

---

# Flask Web Application Tutorial

This tutorial will guide you through creating a simple web application using Flask.

## Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

## Step 1: Install Flask

First, you need to install Flask. Open your terminal and run:

```bash
pip install Flask
```

## Step 2: Create Your Flask Application

Create a new Python file (e.g., `app.py`) and add the following code:

```python
from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
@app.route('/home')
def home():
    # Render the home.html template
    return render_template('home.html')

# Define the route for the about page
@app.route('/about')
def about_page():
    # Render the route.html template
    return render_template('route.html')

# Run the application if this file is executed directly
if __name__ == '__main__':
    # Enable debug mode for development
    app.run(debug=True)
```

## Step 3: Create HTML Templates

Create a `templates` folder in your project directory. Inside this folder, create `home.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Home Page</h1>
    <hr>
    <!-- External link to YouTube -->
    <a href="https://youtube.com" target="_blank" title="Youtube">
        Youtube
    </a>
    <hr>
    <!-- Loop through posts (to be passed from the route) -->
    {% for post in posts %}
        <h2>By: {{ post.author }}</h2>
        <h3>File: {{ post.title }}</h3>
        <p>On: {{ post.date }}</p>
    {% endfor %}
</body>
</html>
```

Note: You'll need to create a similar `route.html` for the about page.

## Step 4: Run Your Flask Application

To run your application, open your terminal, navigate to your project directory, and run:

```bash
python app.py
```

Your application will start, and you can access it at `http://127.0.0.1:5000/`.

## Understanding the Code

### Flask Application (`app.py`)

1. We import necessary modules from Flask.
2. We create a Flask application instance.
3. We define routes using the `@app.route()` decorator. Multiple routes can point to the same function.
4. Our route functions use `render_template()` to display HTML pages.
5. We use `if __name__ == '__main__':` to ensure the app only runs if the script is executed directly.
6. `debug=True` enables debug mode, which is helpful during development.

### HTML Template (`home.html`)

1. We create a basic HTML structure.
2. We use Jinja2 templating (part of Flask) to create a loop with `{% for post in posts %}`.
3. Inside the loop, we display post information using `{{ }}` syntax.

## Next Steps

1. Create the `route.html` template for the about page.
2. Pass data to your templates from your route functions.
3. Add more routes and templates as needed for your application.
4. Explore Flask's documentation to learn about forms, databases, and more advanced features.

Remember to always run Flask in development mode with debugging disabled when deploying to production.

---

T
