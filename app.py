from back import add_data
from flask import Flask, render_template, url_for,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tools',methods = ['POST', 'GET'])
def tools():
    if request.method == 'POST':
        user = request.form['user']
        country=request.form['country']
        email=request.form['email']
        add_data(user,country,email)
        #print(user,country,email)
        return render_template('daud.html')
    else:
        return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)