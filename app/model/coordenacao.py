from ..database import db
from .curso import CursoModel
from .docente import DocenteModel


class CoordenacaoModel(db.Model):
    __tablename__ = "coordenacao"

    id_coordenacao = db.Column(db.Integer, primary_key=True)
    data_entrada = db.Column(db.Date, nullable=True)
    data_saida = db.Column(db.Time, nullable=True)
    status_ativo = db.Column(db.SmallInteger, nullable=True)
    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=False)
    curso = db.relationship('CursoModel', uselist=False, lazy='select')

    docente_id_docente = db.Column(db.Integer, db.ForeignKey('docente.id_docente'), nullable=False)
    docente = db.relationship('DocenteModel', uselist=False, lazy='select')

    def __repr__(self):
        return '<coordenacao %r>' % self.nome
