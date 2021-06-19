from ..database import db
from .disciplina import DisciplinaModel
from .campus import CampusModel

class CursoModel(db.Model):
    __tablename__='curso'

    id_curso = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    data_fundacao = db.Column(db.Date, nullable=True)
    
    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=True)
    campus = db.relationship('CampusModel', lazy='subquery', uselist=False)

    docentes = db.relationship('DocenteModel', uselist=True, backref=db.backref('curso', uselist=False, lazy='select'))
    
    disciplinas = db.relationship('DisciplinaModel', uselist=True, lazy='select', backref=db.backref('curso', uselist=False, lazy='select'))

    discentes = db.relationship('DiscenteModel', uselist=True, backref=db.backref('curso', uselist=False, lazy='select'))
    
    def serialize(self):
        campus = db.session.query(
            CampusModel.nome
        ).filter_by(id_campus=self.campus_id_campus).first()

        return{
            'id_curso':self.id_curso,
            'nome':self.nome,
            'data_fundacao':self.data_fundacao,
            "campus": campus.nome if campus else "nenhum campus"
        }

    def __repr__(self):
        return '<curso %r>' % self.nome