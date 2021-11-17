from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

animais = [
    
    {'id':1,'animal':'leão','classificacao':'mamífero'},
    {'id':2,'animal':'sapo','classificacao':'anfíbio'}
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
    if animais != []:
        ultimo = animais[-1]
        ultimo_id = ultimo['id']
        id_novo = ultimo_id + 1
    else:
        id_novo=1 

    animal = request.form['animal']
    classificacao = request.form['classificacao']
    animais_dict = {'id':id_novo,'animal':animal,'classificacao':classificacao}
    animais.append(animais_dict)

    return redirect('https://5000-pink-cobra-hb6xkmbn.ws-us18.gitpod.io/')

@app.route('/delete', methods=['POST'])
def delete():
    id = request.form['id']
    id_int = int(id)
    for i in animais:
        if i['id'] == id_int:
            animais.remove(i)
            

    
    return redirect('https://5000-pink-cobra-hb6xkmbn.ws-us18.gitpod.io/')

app.run(debug=True)