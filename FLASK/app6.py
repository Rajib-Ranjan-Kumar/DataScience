from flask import Flask,render_template,session,make_response,request
app=Flask(__name__,template_folder='template6')

app.secret_key='SOME KEY'

@app.route('/')
def home():
    return render_template('index.html',message="index page")


@app.route('/setdata')
def setdata():
    session['name']="mike"
    session['value']='80'
    return render_template('index.html',message=f'session set data')

@app.route('/getdata')
def getdata():
    if 'name' in session.keys() and 'value' in session.keys():
     return render_template('index.html',message=f'name={session['name']},value={session['value']}')
    else:
     return render_template('index.html',message=f'session data not found')

@app.route('/cleardata')
def cleardata():
   session.clear()
  # session.pop('name')
   return render_template('index.html',message=f'session data cleared')

@app.route('/set_cookie')
def set_cookie():
   response=make_response(render_template('index.html',message=f'set cookie'))
   response.set_cookie('cookie_name','rajib')
   return response

@app.route('/get_cookie')
def get_cookie():
    if 'cookie_name' in request.cookies.keys():
     cookie_value=request.cookies['cookie_name']
     return render_template('index.html',message=f'cookiedata={cookie_value}')
    else:
     return render_template('index.html',message=f'cokie not found')

@app.route('/clear_cookie')
def clear_cookie():
   if 'cookie_name' in request.cookies.keys():
    response=make_response(render_template('index.html',message=f'clear cookie'))
    response.set_cookie('cookie_name',expires=0)
    return response
   else:
    return render_template('index.html',message=f'cookie not found')

if __name__ == '__main__':
    app.run(debug=True)