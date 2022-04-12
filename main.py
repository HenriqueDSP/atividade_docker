from flask import Flask, request, render_template
from regras.controle_de_dados import salvar_dados, recupera_registros
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        dados = request.form
        salvar_dados(dados)    
    return render_template('cadastro.html')

@app.route('/registros', methods=['get'])
def registro():
    dados = recupera_registros()
    return render_template('registros.html', dados=dados)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)