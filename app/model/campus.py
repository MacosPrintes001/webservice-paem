# Table structure for table `campus`
from ..database import db
from .curso import CursoModel
from .direcao import DirecaoModel
from .base_model import BaseHasNameModel

from datetime import date


class CampusModel(BaseHasNameModel, db.Model):
    __tablename__ = "campus"

    id_campus = db.Column(db.Integer, primary_key=True)
    __ano_fundacao = db.Column('ano_fundacao', db.Date, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    
    direcao_id_direcao = db.Column(db.Integer, db.ForeignKey('direcao.id_direcao'), nullable=True)
    direcao = db.relationship('DirecaoModel', uselist=False, lazy='subquery', backref=db.backref('campus', lazy='subquery'))

    campus = db.relationship('CursoModel', lazy='subquery', uselist=False)

    @property
    def ano_fundacao(self):
        return str(self.__ano_fundacao)

    @ano_fundacao.setter
    def ano_fundacao(self, data):
        if isinstance(data, str):
            day, month, year = data.split('-')
            data = date(day=int(day), month=int(month), year=int(year))

        self.__ano_fundacao = data

    def __init__(self, nome, ano_fundacao, id_campus=None, direcao_id_direcao=None):
        self.nome = nome
        self.ano_fundacao = ano_fundacao
        self.id_campus = id_campus
        self.direcao_id_direcao = direcao_id_direcao,
        


    def serialize(self):

        docente_dict = self.direcao.docente.serialize()

        return {
            "nome":self.nome,
            "ano_fundacao":self.ano_fundacao,
            "id_campus":self.id_campus,
            'direcao_id_direcao': self.direcao_id_direcao,
            "direcao": docente_dict if docente_dict else 'nenhum registro' 
        }

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(cls.nome.label("nome"), cls.id_campus.label("id"))

    def __repr__(self):
        return '<campus %r>' % self.nome