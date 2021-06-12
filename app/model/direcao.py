from ..database.db import db
from .docente import DocenteModel


class DirecaoModel(db.Model):
    __tablename__ = "direcao"

    id_direcao = db.Column(db.Integer, primary_key=True)
    data_entrada = db.Column(db.Date, nullable=False)
    data_saida = db.Column(db.Date, nullable=False) # new column
    # TODO: add column status_ativo
    
    docente_id_docente = db.Column(db.Integer, db.ForeignKey('docente.id_docente'), nullable=True)
    docente = db.relationship('DocenteModel', backref=db.backref('direcao', lazy=True))

    def __repr__(self):
        return '<direcao %r>' % self.id_direcao
