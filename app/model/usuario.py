from ..database import db
from .base_model import BaseHasNameModel

from passlib.apps import custom_app_context as pwd_context


class UsuarioModel(BaseHasNameModel, db.Model):
    __tablename__='usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(45), unique=True, nullable=False)
    cpf = db.Column(db.String(15), unique=True, nullable=True)
    _senha = db.Column('senha', db.Text, nullable=False)
    email = db.Column(db.String(45), nullable=False)
    tipo = db.Column(db.Integer, nullable=False)

    
    def __init__(self, login, senha, email, cpf, tipo, id_usuario=None):
        self.login = login
        self.email = email
        self.cpf = cpf
        self.tipo = tipo
        self.senha = senha
        self.id_usuario = id_usuario

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, password):
        self._senha = pwd_context.hash(password)
    
    def verify_password(self, password):
        ''' Verify password hashed '''
        return pwd_context.verify(password, self.senha)

    def serialize(self):
        return {'id_usuario': self.id_usuario, 
                'login': self.login,
                'cpf': self.cpf,
                'email':self.email,
                'tipo':self.tipo,
        }

    @classmethod
    def find_by_login(cls, login):
       return cls.query.filter_by(login=login).first()

    @classmethod
    def find_by_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf)

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(cls.login.label("nome"), cls.id_usuario.label("id"))

    def __repr__(self):
        return '<usuario %r>' % self.login