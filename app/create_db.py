from app import app
from models import db, Cliente,Mensajes_Contacto
from datetime import date

with app.app_context():
    db.create_all()
    print("Base de datos creada y tablas inicializadas.")


    nuevo_cliente = Cliente(
        nombre="Juan Perez",
        email="lolo@ejemplo.com",
        telefono="123456789",
        fecha_registro=date.today()
    )
    
    nuevo_mensaje = Mensajes_Contacto(
        nombre="Juan Perez",
        email="ejemplo",
        telefono="123456789",
        asunto="Consulta",
        mensaje="Este es un mensaje de prueba"
    )
    
    #insertar datos
    db.session.add(nuevo_cliente)
    db.session.add(nuevo_mensaje)
    #confirmar cambios
    db.session.commit()


    clientes = Cliente.query.all()
    for c in clientes:
        print("Cliente agregado:", c.nombre, c.email, c.telefono, c.fecha_registro)
        
    mensajes = Mensajes_Contacto.query.all()
    for m in mensajes:
        print("Mensaje agregado:", m.nombre, m.email, m.telefono, m.asunto, m.mensaje, m.fecha_envio)
    print("Datos de prueba insertados correctamente.")
    print("Base de datos y tablas creadas exitosamente.")
    
    
    