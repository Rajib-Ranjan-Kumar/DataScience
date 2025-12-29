from flask import Flask,request,make_response,render_template
app=Flask(__name__,template_folder='templates3')

@app.route('/')
def index():
    myvalue='rajib'
    result=10+40
    list=[100,30,40,50,55,60,70]
    return render_template('index.html',myvalue=myvalue,result=result,list=list)

@app.route("/greet")
def greet():
  
    return render_template('greet.html')

@app.route('/filter')
def filter():
    somevalue="other"
    myvalue='rajib'
    result=10+40
    list=[100,30,40,50,55,60,70]
    return render_template('index.html',somevalue=somevalue,myvalue=myvalue,result=result,list=list)

@app.template_filter('reverse_string')
def Reverse_String(s):
    return s[::-1]

@app.template_filter('alternate')
def Alternate(s):

    return [c.upper() if i%2==0 else c.lower() for i,c in enumerate(s)]

if __name__=="__main__":
    app.run(debug=True)