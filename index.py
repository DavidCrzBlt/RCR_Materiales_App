from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/home.html')

@app.route('/productos')
def productos():
    return render_template('/productos.html')

@app.route('/promociones')
def promociones():
    return render_template('/promociones.html')

@app.route('/blog')
def blog():
    return render_template('/blog.html')

@app.route('/contacto')
def contacto():
    return render_template('/contacto.html')

@app.route('/aviso_de_privacidad')
def privacidad():
    return render_template('/privacidad.html')

if __name__ == '__main__':
    app.run()