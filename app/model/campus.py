# Table structure for table `campus`
from ..database import db
from .direcao import DirecaoModel


class CampusModel(db.Model):
    __tablename__ = "campus"

    id_campus = db.Column(db.Integer, primary_key=True)
    ano_fundacao = db.Column(db.Date, nullable=True)
    nome = db.Column(db.String(45), nullable=False)
    
    direcao_id_direcao = db.Column(db.Integer, db.ForeignKey('direcao.id_direcao'), nullable=True)
    direcao = db.relationship('DirecaoModel', uselist=False, backref=db.backref('campus', lazy=True))

    def __init__(self, nome, ano_fundacao, id_campus=None, direcao_id_direcao=None):
        
        self.nome = nome
        self.ano_fundacao = ano_fundacao
        self.id_campus = id_campus
        self.direcao_id_direcao = direcao_id_direcao

    def __repr__(self):
        return '<campus %r>' % self.nome


    
