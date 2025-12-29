from flask import Flask,request,make_response
app=Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello world</h1>"

@app.route('/greeting',methods=['GET','POST','PUT'])
def greeting():
    if request.method=='GET':
        return f"it is get method"
    elif request.method=='POST':
        return f"it is post method"
    elif request.method=='PUT':
        return f"it is put method"
   
    return f"it is not executed"



    return "<h1>Hello rajib .How are you?</h1>"

# @app.route('/greet/<name>')
# def greet(name):
#     return f"<h1>Hello {name} .How are you?</h1>"

@app.route('/add/<num1>/<num2>')
def add(num1,num2):
    a=int(num1)
    b=int(num2)
    return f"{num1}+{num1}={a+b}"

# @app.route('/greet')
# def greet():
#     return str(request.args)

@app.route('/greet')
def greet():
    if 'name'in request.args and 'lname' in request.args:
        name=request.args.get('name')
        lname=request.args.get('lname')
        return f"Hello {name} {lname}"
    else:
        return f"passing argument fail"
        
@app.route('/response')
def response():
    response=make_response()

if __name__=="__main__":
    app.run(debug=True)