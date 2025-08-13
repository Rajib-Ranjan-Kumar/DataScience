from flask import Flask

#creating a flask instance which will webserver gateway interface
app=Flask(__name__)

@app.route("/")#"/" denotes it is home page 
def rajib():
    return "hello rajib"
@app.route("/index")
def index():
    return "index page is updated "

#creating entry point of the program
if __name__=='__main__':
    app.run(debug=True)