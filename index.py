from flask import Flask, render_template,request,redirect
from flask_mail import Mail,Message
from boto.s3.connection import S3Connection

#import config
import os

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'mail.rcrmateriales.com.mx'
app.config['MAIL_PORT'] = 26
app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
#app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
MAIL_USERNAME = os.environ['MAIL_USERNAME']
MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD


mail = Mail(app)

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

@app.route('/contacto',methods=["GET","POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        empresa = request.form["empresa"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]
        datos_contacto = "Nombre: "+ nombre+ "\nEmpresa: " + empresa + "\nTeléfono: " + telefono + "\nCorreo electrónico: " + email + "\nMensaje: " + mensaje
        #msg = Message(subject="Información de contacto",recipients=['rcrproyectos.admon@gmail.com'],body=datos_contacto,sender=config.MAIL_USERNAME)
        msg = Message(subject="Información de contacto",recipients=['rcrproyectos.admon@gmail.com'],body=datos_contacto,sender=MAIL_USERNAME)
        mail.send(msg)
        return redirect("/datosEnviados")
    else:
        return render_template('/contacto.html')

@app.route("/datosEnviados")
def datosEnviados():
    return render_template("datosEnviados.html")


@app.route('/aviso_de_privacidad')
def privacidad():
    return render_template('/privacidad.html')

if __name__ == '__main__':
    app.run()