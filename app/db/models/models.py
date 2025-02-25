# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)

    tareas = relationship("Tarea", back_populates="usuario")

class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    descripcion = Column(String)
    completada = Column(Boolean, default=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    usuario = relationship("Usuario", back_populates="tareas")
