from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    request,
    jsonify,
)
from models import db ,Cliente,Proyecto,Mensajes_Contacto
from datetime import date
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'una_clave_secreta_cualquiera'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:muffin@localhost/gruposigna'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'muffinmejor@gmail.com'
app.config['MAIL_PASSWORD'] = 'tjzx mwtt vsxx uthg'
app.config['MAIL_DEFAULT_SENDER'] = 'oddimuffi@gmail.com'
mail = Mail(app)

# Inicializar la base de datos
db.init_app(app)



@app.route('/')
def raiz():
    return redirect(url_for('inicio'))


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


@app.route('/acerca')
def acerca():   
    return render_template('acerca.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/galeria')
def galeria():
    proyectos = Proyecto.query.all()
    clientes = Cliente.query.all()
    
    return render_template('galeria.html', proyectos=proyectos, clientes=clientes)

@app.route('/prueba')
def prueba():
    return render_template('prueba.html')

@app.route('/clientes')
def clientes():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)


@app.route('/proyecto/<int:id_proyecto>')
def proyecto(id_proyecto):
    proyecto = Proyecto.query.get_or_404(id_proyecto)
    return render_template('proyecto.html', proyecto=proyecto)

@app.route('/enviar-formulario', methods=['POST'])
def enviar_formulario():
    nombre = request.form.get('nombre')
    email = request.form.get('email')
    asunto = request.form.get('asunto')
    telefono = request.form.get('telefono')
    mensaje = request.form.get('mensaje')
    
    nuevo_mensaje = Mensajes_Contacto(nombre=nombre, email=email, telefono=telefono,asunto=asunto, mensaje=mensaje)
    db.session.add(nuevo_mensaje)
    db.session.commit() 

    msg = Message(
        subject=f'{asunto}',
        sender=email,
        recipients=['oddimuffi@gmail.com'],
        body=f'Nombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}\nAsunto:{asunto}\nMensaje: {mensaje}')
    mail.send(msg)
    return jsonify({'message': '¡Mensaje enviado con éxito!'})




if __name__ == '__main__':
    app.run(debug=True)
    #serve(app, host="0.0.0.0", port=8080)   
    

    
