from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefono = db.Column(db.String(15), nullable=False)
    fecha_registro = db.Column(db.Date)
    direccion = db.Column(db.String(200), nullable=True)
    proyectos = db.relationship('Proyecto', backref='cliente', lazy=True)

class Proyecto(db.Model):
    __tablename__ = 'proyectos'
    id_proyecto = db.Column(db.Integer, primary_key=True)
    nombre_proyecto = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    imagen_path = db.Column(db.String(255), nullable=True)
    #materiales = db.Column(db.String(200), nullable=True)
    estado = db.Column(db.String(50), nullable=False)
    #pintura = db.Column(db.String(50), nullable=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_entrega = db.Column(db.Date, nullable=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id_cliente'), nullable=False)
    id_servicio = db.Column(db.Integer, db.ForeignKey('servicios.id_servicio'), nullable=False)
    
class Servicio(db.Model):
    __tablename__ = 'servicios'
    id_servicio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    
class Materiales(db.Model):
    __tablename__ = 'materiales'
    id_material = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    cantidad = db.Column(db.Integer, nullable=False)
    proyecto_id = db.Column(db.Integer, db.ForeignKey('proyectos.id_proyecto'), nullable=False)

class Materiales_Proyecto(db.Model):
    __tablename__ = 'materiales_proyecto'
    id_material = db.Column(db.Integer, db.ForeignKey('materiales.id_material'), primary_key=True)
    id_proyecto = db.Column(db.Integer, db.ForeignKey('proyectos.id_proyecto'), primary_key=True)
    
class Mensajes_Contacto(db.Model):
    __tablename__ = 'mensajes_contacto'
    id_mensaje = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(50), nullable=True)
    asunto = db.Column(db.String(100), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)
    fecha_envio = db.Column(db.DateTime, default=db.func.current_timestamp())
