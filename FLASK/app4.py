from flask import Flask,render_template,request
import pandas as pd

app=Flask(__name__,template_folder='template4')

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    if request.method=='POST':
         username=""
         password=""
         if 'username' in request.form.keys():
           username=request.form.get('username')

         if 'password' in request.form.keys():
           password=request.form.get('password')

         if password =="raj" and username =='raj':
            return f"Your name:{username}\nYour password:{password}"
         else:
          return f"{password+username}"
   


@app.route('/file',methods=['POST'])
def file():
   file=request.files['file']
   if file.content_type=='text/plain':
      return file.read().decode()
   elif file.content_type in [
    'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.ms-excel'
]:
      df=pd.read_excel(file)
      return df.to_html()
   else:
      return f"file not match"

if __name__=="__main__":
    app.run(debug=True)
