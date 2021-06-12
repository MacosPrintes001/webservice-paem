from ..database import db
from .discente import DiscenteModel


db.Table(
        'disciplina_has_discente',
        db.Column('disciplina_id_disciplina', db.Integer, db.ForeignKey('disciplina.id_disciplina'), primary_key=True), 
        db.Column('discente_id_discente', db.Integer, db.ForeignKey('discente.id_discente'), primary_key=True),
        db.Column('data', db.Date, nullable=False)
)

class DisciplinaModel(db.Model):
    __tablename__='disciplina'

    id_disciplina = db.Column(db.Integer, primary_key=True)
    codigo_sigaa = db.Column(db.String(45), nullable=True)
    semestre = db.Column(db.Integer, nullable=True)

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)

    discentes = db.relationship('DiscenteModel', secondary='disciplina_has_discente',  backref=db.backref('disciplinas', lazy=True))

    def __repr__(self):
        return '<disciplina %r>' % self.login

    
