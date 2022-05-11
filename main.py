from flask import Flask, request, render_template
from regras.controle_de_dados import salvar_dados, recupera_registros
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/cadastro_de_alunos', methods=['GET', 'POST'])
def cadastro_de_alunos():
    if request.method == 'POST':
        dados = request.form
        salvar_dados(dados)    
    return render_template('cadastro_de_alunos.html')

@app.route('/registros_de_alunos', methods=['GET'])
def registros_de_alunos():
    dados = recupera_registros()
    print(dados)
    return render_template('registro_dos_alunos.html', dados=dados)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)