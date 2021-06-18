from ..database.db import db
from .docente import DocenteModel
from datetime import date

class DirecaoModel(db.Model):
    __tablename__ = "direcao"

    id_direcao = db.Column(db.Integer, primary_key=True)
    __data_entrada = db.Column("data_entrada", db.Date, nullable=False)
    __data_saida = db.Column("data_saida", db.Date, nullable=False)
    status_ativo = db.Column(db.SmallInteger, nullable=True)
    
    docente_id_docente = db.Column(db.Integer, db.ForeignKey('docente.id_docente'), nullable=True)
    docente = db.relationship('DocenteModel', uselist=False, lazy='subquery')

    def __init__(self, data_entrada, data_saida, status_ativo, id_direcao=None):
        self.id_direcao = id_direcao
        self.data_entrada = data_entrada
        self.data_saida = data_saida
        self.status_ativo = status_ativo

    @property
    def data_entrada(self):
        return str(self.__data_entrada)

    @data_entrada.setter
    def data_entrada(self, data):
        if isinstance(data, str):
            day, month, year = data.split('-')
            data = date(day=int(day), month=int(month), year=int(year))
            self.__data_entrada = data

    @property
    def data_saida(self):
        return str(self.__data_saida)

    @data_saida.setter
    def data_saida(self, data):
        if isinstance(data, str):
            day, month, year = data.split('-')
            data = date(day=int(day), month=int(month), year=int(year))
            self.__data_saida = data

    def serialize(self):
        return {
            "id_direcao": self.id_direcao,
            "data_entrada": self.data_entrada,
            "data_saida": self.data_saida,
            "status": self.status_ativo,
            "docente": db.session.query(DocenteModel.nome).filter_by(id_docente=self.docente_id_docente).first().nome,
        }

    def __repr__(self):
        return '<direcao %r>' % self.id_direcao
