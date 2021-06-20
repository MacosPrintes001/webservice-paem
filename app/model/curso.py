from ..database import db
from .disciplina import DisciplinaModel
from .base_model import BaseHasNameModel
from .campus import CampusModel

from datetime import date

class CursoModel(BaseHasNameModel, db.Model):
    __tablename__='curso'

    id_curso = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    __data_fundacao = db.Column("data_fundacao", db.Date, nullable=True)
    
    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=True)
    campus = db.relationship('CampusModel', lazy='subquery', uselist=False)

    docentes = db.relationship('DocenteModel', uselist=True, backref=db.backref('curso', uselist=False, lazy='select'))
    
    disciplinas = db.relationship('DisciplinaModel', uselist=True, lazy='select', backref=db.backref('curso', uselist=False, lazy='select'))

    discentes = db.relationship('DiscenteModel', uselist=True, backref=db.backref('curso', uselist=False, lazy='select'))
    
    @property
    def data_fundacao(self):
        return str(self.__data_fundacao)
    
    @data_fundacao.setter
    def data_fundacao(self, data):
        if isinstance(data, str):
            day, month, year = data.split('-')
            data = date(day=int(day), month=int(month), year=int(year))
        
        self.__data_fundacao = data
        
    def serialize(self):
        campus = db.session.query(
            CampusModel.nome
        ).filter_by(id_campus=self.campus_id_campus).first()

        return {
            'id_curso':self.id_curso,
            'nome':self.nome,
            'data_fundacao':self.data_fundacao,
            "campus": campus.nome if campus else "null"
        }

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(cls.nome.label("nome"), cls.id_curso.label("id"))
        
    def __repr__(self):
        return '<curso %r>' % self.nome