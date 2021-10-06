## Setup
```
pip3 install virtualenv
virtualenv venv -p python3
source venv/bin/activate
```

## Flask
```
pip freeze | grep Flask
```


## Request

http://127.0.0.1:8000/?name="Pluralsight"

```
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name="Treehouse"):
    name = request.args.get('name',name)
    return "Hello from {}".format(name)


app.run(
    debug=True,
    port=8000)
```

## clean request with no request module
```
from flask import Flask


app = Flask(__name__)

#
# @app.route('/')
# def index():
#     return "Hello from Treehouse"


@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
    return "Hello from {}".format(name)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1,num2):
    return "{} + {} = {}".format(num1,num2,num1 + num2)

app.run(
    debug=True,
    port=8000)

```


```
from flask import Flask

app = Flask(__name__)

@app.route('/multiply')
@app.route('/multiply/<int:arg1>/<int:arg2>')
def multiply(arg1 = 5, arg2 = 5):
    return str(arg1 * arg2)

```