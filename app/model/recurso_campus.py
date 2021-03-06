from ..database import db
from .base_model import BaseModel
from .campus import BaseHasNameModel, CampusModel
from datetime import time


class RecursoCampusModel(BaseHasNameModel, db.Model):
    __tablename__ = "recurso_campus"

    id_recurso_campus = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    __inicio_horario_funcionamento = db.Column('inicio_horario_funcionamento', db.Time, nullable=True)
    __fim_horario_funcionamento = db.Column('fim_nicio_horario_funcionamento', db.Time, nullable=True)
    quantidade_horas = db.Column(db.Integer, nullable=True)
    
    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=True)
    campus = db.relationship('CampusModel', backref=db.backref('recursos_campus', lazy='select'))
            
    def serialize(self):

        campus = db.session.query(
            CampusModel.nome
        ).filter_by(id_campus=self.campus_id_campus).first() # query name of campus
        
        return {
            'id_recuso_campus': self.id_recurso_campus, 
            'nome': self.nome,
            'capacidade': self.capacidade,
            'descricao':self.descricao,
            'inicio_horario_funcionamento':self.inicio_horario_funcionamento,
            'fim_horario_funcionamento':self.fim_horario_funcionamento,
            'quantidade_horas': self.quantidade_horas,
            'campus_id_campus':self.campus_id_campus,
            'campus': campus.nome if campus else "null"
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
    
    @classmethod
    def query_all_names(cls):
        return super().query_all_names(cls.nome.label("nome"), cls.id_recurso_campus.label("id"))

    def __repr__(self):
        return '<recurso_campus %r>' % self.nome