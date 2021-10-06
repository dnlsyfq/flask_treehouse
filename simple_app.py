from flask import Flask
from flask import render_template

app = Flask(__name__)

#
# @app.route('/')
# def index():
#     return "Hello from Treehouse"


@app.route('/')
@app.route('/<name>')
def index(name="Treehouse"):
    # return "Hello from {}".format(name)
    return render_template("index.html",name=name)


@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):

    # method 1
    # return "{} + {} = {}".format(num1,num2,num1 + num2)

    # method 2 without template
    # return """
    # <!doctype html>
    #     <head><title>Adding!</title></head>
    #     <body>
    #         <h1>{} + {} = {} </h1>
    #     </body>
    # </html>
    # """.format(num1, num2, num1 + num2)

    # method 3 with template
    # return render_template("add.html", num1=num1, num2=num2)

    # method 4 with template
    context = {'num1':num1, 'num2':num2}
    return render_template("add.html", **context)


app.run(
    debug=True,
    port=8000)
