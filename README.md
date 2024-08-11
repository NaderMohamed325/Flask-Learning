

---

# Flask Tutorial 

- **First, install Flask:**

  ```bash
  pip install Flask
  ```

- **Use this code to create a web server:**

  ```python
  from flask import Flask

  app = Flask(__name__)

  @app.route('/')
  def home_page():
      return '<h2>Home Page</h2>'

  if __name__ == '__main__':
      app.run()
  ```

- **To run the code, you can write in the terminal:**

  ```bash
  export FLASK_APP=app.py
  export FLASK_ENV=development
  flask run
  ```

  Replace `app.py` with the name of your Python file if it's different. For Windows, use `set` instead of `export`:

  ```bash
  $ set FLASK_APP=app.py
  $ set FLASK_ENV=development
  $ flask run
  ```

---

This will start your Flask development server, and you can access your application at `http://127.0.0.1:5000/`.

- **for better experience you can add Debug option to prevent running the code each time you modify the code**
```python
  if __name__ == '__main__':
      app.run(debug=True)
```
Then you write
```bash
$ python Project_name.py

$ Flask run
```



