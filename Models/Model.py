from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
import Models.declarative_base as db
from sqlalchemy.orm import relationship


class Usuarios(db.Base):
    __tablename__ = 'usuarios'
    id_usuario = Column(Integer, primary_key=True)
    usuario = Column(String)
    contrasena = Column(String)
    nombre = Column(String)
    cedula = Column(String)
    rol = Column(Integer)
    id_negocio = Column(Integer)

    # gastos = relationship('Gasto', cascade='all, delete, delete-orphan')
    # viajeros = relationship('Viajero', secondary='actividad_viajero')


class Roles(db.Base):
    __tablename__ = 'roles'
    id_rol = Column(Integer, primary_key=True)
    rol = Column(String)


class Negocio(db.Base):
    __tablename__ = 'negocio'
    id_negocio = Column(Integer, primary_key=True)
    nombre = Column(String)

    # actividades = relationship('Actividad', secondary='actividad_viajero')
    # gastos = relationship('Gasto', cascade='all, delete, delete-orphan')


class Producto(db.Base):
    __tablename__ = 'producto'
    id_producto = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    precio = Column(Float)
    id_negocio = Column(Integer)

    # actividad = Column(Integer, ForeignKey('actividad.id'), nullable=False)
    # viajero_id = Column(Integer, ForeignKey('viajero.id'), nullable=False)
    # viajero = relationship('Viajero')