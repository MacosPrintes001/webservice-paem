from ..database import db
from .base_model import PessoaModel
from .campus import CampusModel
from datetime import time


class RecursoCampusModel(PessoaModel, db.Model):
    __tablename__ = "recurso_campus"

    id_recurso_campus = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    __inicio_horario_funcionamento = db.Column('inicio_horario_funcionamento', db.Time, nullable=True)
    __fim_horario_funcionamento = db.Column('fim_nicio_horario_funcionamento', db.Time, nullable=True)
    # quantidade_horas = db.Column(db.Integer, nullable=True) # nova coluna
    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=False)
    campus = db.relationship('CampusModel', backref=db.backref('recursos_campus', lazy=True))
    
    def __init__(self,
            nome,
            capacidade,
            descricao,
            inicio_horario_funcionamento,
            fim_horario_funcionamento,
            campus_id_campus,
            id_recurso_campus=None
                                    ):
        
        self.id_recurso_campus = id_recurso_campus
        self.nome = nome
        self.capacidade = capacidade
        self.descricao = descricao
        self.inicio_horario_funciomaneto = inicio_horario_funcionamento
        self.fim_horario_funcionamento = fim_horario_funcionamento
        self.campus_id_campus = campus_id_campus
        
        

    def serialize(self):
        return {
            'id_recuso_campus': self.id_recurso_campus, 
            'nome': self.nome,
            'capacidade': self.capacidade,
            'descricao':self.descricao,
            'inicio_horario_funcionamento':self.inicio_horario_funcionamento,
            'fim_horario_funcionamento':self.fim_horario_funcionamento,
            'campus_id_campus':self.campus_id_campus
        }
    
    @property                    
    def inicio_horario_funcionamento(self):
        return str(self.__inicio_horario_funcionamento)
    
    @inicio_horario_funcionamento.setter
    def inicio_horario_funcionamento(self, inicio_horario_funcionamento):
        
        if isinstance(inicio_horario_funcionamento, str):
            hour_inicio, minute_inicio, second_inicio = inicio_horario_funcionamento.split(':')
            self.__inicio_horario_funcionamento = time(
                hour=int(hour_inicio), 
                minute=int(minute_inicio), 
                second=int(second_inicio)
            )

        self.__inicio_horario_funcionamento = inicio_horario_funcionamento

    @property
    def fim_horario_funcionamento(self):
        return str(self.__fim_horario_funcionamento)

    @fim_horario_funcionamento.setter
    def fim_horario_funcionamento(self, fim_horario_funcionamento):
        
        if isinstance(fim_horario_funcionamento, str):
            hour_fim, minute_fim, sec_fim = fim_horario_funcionamento.split(':')
            self.__fim_horario_funcionamento = time(
                hour=int(hour_fim),
                minute=int(minute_fim),
                second=int(sec_fim)
            )

        self.__fim_horario_funcionamento = fim_horario_funcionamento
        
    def __repr__(self):
        return '<recurso_campus %r>' % self.nome