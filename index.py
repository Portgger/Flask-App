from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/bye')
def bye():
    return render_template('bye.html')

app.run(debug=True)