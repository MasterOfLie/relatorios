from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
import pytz

db = SQLAlchemy()
brasilia_tz = pytz.timezone('America/Araguaina')
class Tramite(db.Model):
    __tablename__ = 'tramite'
    id = db.Column(db.Integer, primary_key=True)
    origem = db.Column(db.String(100))
    destino = db.Column(db.String(100))
    horario = db.Column(db.DateTime, default=datetime.now(brasilia_tz))
    tempo_atendimento = db.Column(db.Integer)
    status = db.Column(db.String(20))
    processo = db.Column(db.String(100))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario', back_populates='tramitess') 
    servico_id = db.Column(db.Integer, db.ForeignKey('servico.id'))
    servico = db.relationship('Servico', backref='tramites')

class Telefone(db.Model):
    __tablename__ = 'telefone'
    id = db.Column(db.Integer, primary_key=True)
    horario = db.Column(db.DateTime, default=datetime.now(brasilia_tz))
    tempo_atendimento = db.Column(db.Integer)
    status = db.Column(db.String(20))
    servico_id = db.Column(db.Integer, db.ForeignKey('servico.id'))  
    servico = db.relationship('Servico', backref='telefones')
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    usuario = db.relationship('Usuario', back_populates='telefones')  
    

class Servico(db.Model):
    __tablename__ = 'servico'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    secretaria = db.Column(db.Integer, db.ForeignKey('secretaria.id'))

class Secretaria(db.Model):
    __tablename__ = 'secretaria'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

class Reparticao(db.Model):
    __tablename__ = 'reparticao'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    administrador = db.Column(db.Boolean, default=False)
    tramitess = db.relationship('Tramite', back_populates='usuario', lazy=True)
    telefones = db.relationship('Telefone', back_populates='usuario', lazy=True)
