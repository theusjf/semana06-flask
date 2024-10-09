from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return (
        '<h1>Avaliação contínua: Aula 030</h1>'
        '<ul>'
            '<li><a href="/">Home</a></li>'
            '<li><a href="/user/<name>/<pt>/<inst>">Identificação</a></li>'
            '<li><a href="/contextorequisicao">Contexto da Requisição</a></li>'
        '</ul>'
    )

@app.route('/user/<name>/<pt>/<inst>')
def identificacao(name, pt, inst):
    return (
        '<h1>Avaliação contínua: Aula 030</h1>'
        '<h2>Aluno: {}</h2>'
        '<h2>Prontuário: {}</h2>'
        '<h2>Instituição: {}</h2>'
        '<a href="/">Voltar</a>'
    ).format(name, pt, inst)

@app.route('/contextorequisicao')
def contextorequisicao():
    user_agent = request.headers.get('User-Agent')
    remote_ip = request.remote_addr
    host = request.host

    return (
        '<h1>Avaliação contínua: Aula 030</h1>'
        '<h2>Seu navegador é: {}</h2>'
        '<h2>O IP do computador remoto é: {}</h2>'
        '<h2>O host da aplicação é: {}</h2>'
        '<a href="/">Voltar</a>'
    ).format(user_agent, remote_ip, host)
