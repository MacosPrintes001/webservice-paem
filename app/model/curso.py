from ..database import db
from .disciplina import DisciplinaModel


class CursoModel(db.Model):
    __tablename__='curso'

    id_curso = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    data_fundacao = db.Column(db.Date, nullable=True)
    
    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=False)
    
    docentes = db.relationship('DocenteModel', backref=db.backref('curso', uselist=False, lazy='select'))
    
    disciplinas = db.relationship('DisciplinaModel', backref=db.backref('curso', uselist=False, lazy='select'))

    discentes = db.relationship('DiscenteModel', backref=db.backref('curso', uselist=False, lazy='select'))

    def __init__(self, nome, data_fundacao, campus_id_campus, id_curso=None):
        self.nome = nome
        self.data_fundacao = data_fundacao
        self.campus_id_campus = campus_id_campus
        self.id_curso = id_curso

    def serialize(self):
        return{
            'id_curso':self.id_curso,
            'nome':self.nome,
            'data_fundacao':self.data_fundacao,
        }

    def __repr__(self):
        return '<curso %r>' % self.nome