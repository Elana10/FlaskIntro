# Put your app in here.
from operations import add,sub,mult,div
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def do_add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = add(a,b)
    return str(result)

@app.route('/sub')
def do_sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def do_mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = mult(a,b)
    return str(result)

@app.route('/div')
def do_div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = div(a,b)
    return str(result)

operators ={
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route("/math/<oper>")
def do_math(oper):
    a = int(request.args['a'])
    b = int(request.args['b'])
    result = operators[oper](a,b)
    return str(result)