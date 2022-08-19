from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_fontawesome import FontAwesome
from flask_sqlalchemy import SQLAlchemy

# import config
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://syphkmrewwlkjo:aeb55fe714669b0bd500a138a49a2172b2d105918b05828f94a5699436567083@ec2-44-193-178-122.compute-1.amazonaws.com:5432/dbe61uips2p98l'
app.config['SECRET_KEY'] = "random string"

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

db = SQLAlchemy(app)

class products(db.Model):
   id = db.Column('product_id', db.Integer, primary_key=True)
   code = db.Column(db.String(50),unique=True)
   product_name = db.Column(db.String(255))
   price = db.Column(db.Numeric)
   discount = db.Column(db.Integer)
   category = db.Column(db.String(255))

def __init__(self,code,product_name,price,discount,category):
   self.code = code
   self.product_name = product_name
   self.price = price
   self.discount = discount
   self.category = category

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/promociones')
def promociones():
    return render_template('promociones.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/contacto', methods=["GET", "POST"])
def contacto():
    if request.method == "POST":
        nombre = request.form["nombre"]
        empresa = request.form["empresa"]
        telefono = request.form["telefono"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]
        datos_contacto = "Nombre: " + nombre + "\nEmpresa: " + empresa + "\nTeléfono: " + telefono + "\nCorreo electrónico: " + email + "\nMensaje: " + mensaje

        msg = Message(subject="Información de contacto", recipients=[
                      'rcrproyectos.admon@gmail.com'], body=datos_contacto, sender=MAIL_USERNAME)
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


@app.route('/newData', methods=["GET","POST"])
def newData():
    if request.method == "POST":

        product = products(code=request.form["code"],product_name=request.form["product_name"],price=request.form["price"],discount = request.form["discount"],category = request.form["category"])

        db.session.add(product)
        db.session.commit()

        flash('Record was succesfullt added')
        return redirect(url_for('productos'))
        
    return render_template('newData.html')

@app.route('/productos',methods = ["GET","POST"])
def productos():
    if request.method == "POST":
        return render_template('productos.html',productos = products.query.filter_by(category = request.form["search_category"]).all())
    else:
        return render_template('productos.html',productos = products.query.fetchone())

if __name__ == '__main__':
    db.create_all()
    app.run()