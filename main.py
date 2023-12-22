from flask import Flask,render_template,request

import db
app = Flask(__name__)
 
@app.route('/')
def main():
    return render_template('test1.html')
 
@app.route('/add_book', methods = ['POST', 'GET'])
def add_book():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
      db.connect= request.form[name]
      return render_template('test1.html',form_data = form_data)
 
 
app.run(host='127.0.0.1', port=5000)