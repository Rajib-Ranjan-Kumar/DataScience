from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/form',methods=['GET','POST'])
def form():
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method =='POST':
        name=request.form['name']
        return f"Hello {name}"
    return render_template('form.html')

@app.route('/sucess/<int:score>')
def sucess(score):
    if score>40:
        res="Pass"
    else :
        res="Fail"
    return render_template('result.html',result=res)

if __name__=='__main__':
    app.run(debug=True)