from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "¡Bienvenido a mi aplicación Flask!"

@app.route('/crearcookie')
def crear_cookie():
    response = make_response("Cookie generada. Redireccionando...")
    response.set_cookie('mi_cookie', 'valor_de_la_cookie')
    return redirect(url_for('verificar_cookie'))

@app.route('/verificarcookie')
def verificar_cookie():
    if 'mi_cookie' in request.cookies:
        return redirect(url_for('cookie_valida'))
    else:
        return redirect(url_for('cookie_invalida'))

@app.route('/cookievalida')
def cookie_valida():
    return "Estamos bien, la cookie es válida."

@app.route('/cookieinvalida')
def cookie_invalida():
    return "Algo salió mal, no se encontró la cookie."

if __name__ == '__main__':
    app.run(debug=True) 