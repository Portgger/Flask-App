from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

animais = [
    {'animal':'leão','classificacao':'mamífero'},
    {'animal':'sapo','classificacao':'anfíbio'}
]

@app.route('/')
def index():
    return render_template('index.html',lista=animais)

@app.route('/css')
def css():
    return render_template('style.css')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    animal = request.form['animal']
    classificacao = request.form['classificacao']
    animais_dict = {'animal':animal,'classificacao':classificacao}
    animais.append(animais_dict)

    return redirect('https://5000-amethyst-impala-ytw4jdcs.ws-us18.gitpod.io/')

app.run(debug=True)