from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    
    titulo = 'Gestão de usuarios'
    usuarios = [
        {"nome":"Guilherme","membro_ativo":True,
        "nome":"Silvia","membro_ativo":False,
        "nome":"Vitoria","membro_ativo":True,
        "nome":"Leticia","membro_ativo":False,
    }]
    return render_template('template\\index.html')


app.run(debug=True)