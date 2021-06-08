# Flask Basic Routing Example

### How to run

```bash
$ python example.py
```

### References

- [Flask-QuickStart](<https://flask.palletsprojects.com/en/2.0.x/quickstart/>)
- [Flask-Class Flask](<https://flask.palletsprojects.com/en/2.0.x/api/?highlight=flask#flask.Flask>)
- [GitHub-flask/scr/flask/app.py](<https://github.com/pallets/flask/blob/main/src/flask/app.py>)

## 0. Flask application Object

- 아래와 같이 `Flask` instance를 생성하는 것에서 시작한다.

```python
from flask import Flask, jsonify

app = Flask(__name__)
```

- `Flask` 객체는 첫 번째 파라미터로 module/package 이름을 받는다(`import_name`).
- Flask Application은 이를 기준으로 Resource를 찾고 Debugging을 수행한다.
- 단일 module로 구성되어 있는 Application이라면 위와 같이 `__name__`을 전달하는 것으로 충분하다. 

### Flask.route() method

- Flask에서는 Routing을 Decorator 형식으로 적용한다.
- Flask.route() method의 Source Code는 아래와 같다.

```python
# define on the Scaffold class, the parent of Flask class
def route(self, rule: str, **options: t.Any) -> t.Callable:
		"""Decorate a view function to register it with the given URL
		rule and options. Calls :meth:`add_url_rule`, which has more
		details about the implementation.
		.. code-block:: python
			@app.route("/")
			def index():
				return "Hello, World!"
		See :ref:`url-route-registrations`.
		The endpoint name for the route defaults to the name of the view
		function if the ``endpoint`` parameter isn't passed.
		The ``methods`` parameter defaults to ``["GET"]``. ``HEAD`` and
		``OPTIONS`` are added automatically.
		:param rule: The URL rule string.
		:param options: Extra options passed to the
			:class:`~werkzeug.routing.Rule` object.
		"""

		def decorator(f: t.Callable) -> t.Callable:
			endpoint = options.pop("endpoint", None)
			self.add_url_rule(rule, endpoint, f, **options)
			return f

		return decorator
```

## 1. Basic Routing Format

```python
@app.route("/define/routing/path")
def function_name():
    return "<h1> this is response <\h1>"
```

## 2. Get variable section on URL

```python
# Pass variable
@app.route("/user/<username>")
def user(username):
    return f"<h1> The User name is {username} </h1>"

# Specify variable type with converter
@app.route("/id/<int:user_id>")
def get_user_id(user_id):
    is_int = isinstance(user_id, int)
    return f"<h1> The type of user id is int: {is_int} </h1>"
```

### Request & Response

```html
# Request to: localhost:8080/user/enfow

HTTP/1.0 200 OK
Content-Length: 33
Content-Type: text/html; charset=utf-8
Date: Tue, 08 Jun 2021 11:58:32 GMT
Server: Werkzeug/2.0.1 Python/3.8.2

<h1> The User name is enfow </h1>
```

```bash
# Request to: localhost:8080/id/10

HTTP/1.0 200 OK
Content-Length: 43
Content-Type: text/html; charset=utf-8
Date: Tue, 08 Jun 2021 11:58:38 GMT
Server: Werkzeug/2.0.1 Python/3.8.2

<h1> The type of user id is int: True </h1>
```

## 3. Return JSON response 

```python
@app.route("/json")
def get_json():
    user_dict = {
        "1" : "enfow",
        "2" : "curt",
    }
    return jsonify(user_dict)
```

### Request & Response

```bash
# Request to: localhost:8080/json

HTTP/1.0 200 OK
Content-Length: 35
Content-Type: application/json
Date: Tue, 08 Jun 2021 11:59:53 GMT
Server: Werkzeug/2.0.1 Python/3.8.2

{
    "1": "enfow",
    "2": "curt"
}
```
