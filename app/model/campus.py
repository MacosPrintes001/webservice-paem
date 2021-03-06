# Table structure for table `campus`
from ..database import db
from .base_model import BaseHasNameModel

from datetime import date


class CampusModel(BaseHasNameModel, db.Model):
    __tablename__ = "campus"

    id_campus = db.Column(db.Integer, primary_key=True)
    __ano_fundacao = db.Column('ano_fundacao', db.Date, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    
    direcao_id_direcao = db.Column(db.Integer, db.ForeignKey('direcao.id_direcao'), nullable=True)
    direcao = db.relationship('DirecaoModel', uselist=False, lazy='select')

    @property
    def ano_fundacao(self):
        return str(self.__ano_fundacao)

    @ano_fundacao.setter
    def ano_fundacao(self, data):
        if isinstance(data, str):
            day, month, year = data.split('-')
            data = date(day=int(day), month=int(month), year=int(year))

        self.__ano_fundacao = data

    def serialize(self):
        
        try:
            docente_dict = self.direcao.docente.serialize()
        except AttributeError as msg:
            print("warning: nenhum docente na direção cadastrado neste campus.")
            docente_dict = None
        finally:
            return {
                "nome":self.nome,
                "ano_fundacao":self.ano_fundacao,
                "id_campus":self.id_campus,
                'direcao_id_direcao': self.direcao_id_direcao,
                "direcao": docente_dict if docente_dict else 'null' 
            }

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(cls.nome.label("nome"), cls.id_campus.label("id"))

    def __repr__(self):
        return '<campus %r>' % self.nome