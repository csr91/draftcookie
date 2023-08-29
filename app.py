from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    welcome_message = """
    ¡Bienvenido a mi aplicación Flask!<br><br>
    Aquí tienes algunas URLs disponibles en la aplicación:<br>
    - <a href="/crearcookie">Crear una cookie</a><br>
    - <a href="/verificarcookie">Verificar la existencia de la cookie</a><br>
    - <a href="/cookievalida">Cookie válida</a><br>
    - <a href="/cookieinvalida">Cookie inválida</a><br>
    """
    return welcome_message

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
