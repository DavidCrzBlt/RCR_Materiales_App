from flask import Flask, render_template,request,redirect,url_for
from flask_mail import Mail,Message
from flask_fontawesome import FontAwesome
from flask_sqlalchemy import SQLAlchemy

# import config
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://exjwhnrqjluzoj:503ce0b10272188be53d2f63c7c3b9a92d7f08388ddea677b386e4b19a1d663a@ec2-34-227-120-79.compute-1.amazonaws.com:5432/d5l2rgul20fhub'

fa = FontAwesome(app)
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = 'mail.rcrmateriales.com.mx'
app.config['MAIL_PORT'] = 26
app.config['MAIL_USE_SSL'] = False

# MAIL_USERNAME = config.MAIL_USERNAME
# MAIL_PASSWORD = config.MAIL_PASSWORD

MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']

app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD

mail = Mail(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self,username,email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/promociones')
def promociones():
    return render_template('promociones.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contacto',methods=["GET","POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        empresa = request.form["empresa"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]
        datos_contacto = "Nombre: "+ nombre+ "\nEmpresa: " + empresa + "\nTeléfono: " + telefono + "\nCorreo electrónico: " + email + "\nMensaje: " + mensaje
        
        msg = Message(subject="Información de contacto",recipients=['rcrproyectos.admon@gmail.com'],body=datos_contacto,sender=MAIL_USERNAME)
        mail.send(msg)
        return redirect("/datosEnviados")
    else:
        return render_template('contacto.html')

@app.route("/datosEnviados")
def datosEnviados():
    return render_template("datosEnviados.html")

@app.route('/aviso_de_privacidad')
def privacidad():
    return render_template('privacidad.html')

@app.route('/pruebas')
def pruebas():
    p = User.query.filter_by(username='admin').first()
    return render_template('pruebas.html',prueba=p)

if __name__ == '__main__':
    app.run()