from flask import Flask, render_template, request
from functions.functions import gerarResposta
from markdown import markdown

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/resumo', methods=['POST'])
def gerar_resumo():
    idioma = request.form.get('idioma')
    formalidade = request.form.get('formalidade')
    texto = request.form.get('texto')

    resposta = gerarResposta(formalidade=formalidade, idioma=idioma, texto=texto)
    resposta = markdown(resposta)

    return render_template('index.html', resumo = resposta)

if __name__ == '__main__':
    app.run()