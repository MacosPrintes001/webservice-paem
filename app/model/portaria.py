from ..database import db
from .usuario import UsuarioModel
from .curso import CursoModel
from .base_model import BaseHasNameModel


class PortariaModel(BaseHasNameModel, db.Model):
    __tablename__ = "portaria"

    id_portaria = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=True)
    funcao = db.Column(db.String(45), nullable=True)
    turno_trabalho = db.Column(db.SmallInteger, nullable=False)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', lazy='subquery')

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)
    curso = db.relationship('CursoModel', lazy="noload")

    def __init__(self, 
            nome, 
            data_nascimento, 
            funcao, 
            turno_trabalho,
            usuario_id_usuario=None,
            curso_id_curso=None, 
            id_portaria=None):
        
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.funcao = funcao
        self.turno_trabalho = turno_trabalho
        self.usuario_id_usuario = usuario_id_usuario
        self.curso_id_curso = curso_id_curso
        self.id_portaria = id_portaria

    def serialize(self):

        try:
            usuario_dict = self.usuario.serialize()
        except AttributeError as msg:
            print("Usuário não cadastrado.")
            usuario_dict = None

        finally:
            curso = db.session.query(
                CursoModel.nome
            ).filter_by(id_curso=self.curso_id_curso).first()
            
            return {
                "nome": self.nome,
                "data_nascimento": self.data_nascimento,
                "funcao": self.funcao,
                "turno_trabalho": self.turno_trabalho,
                "usuario_id_usuario": self.usuario_id_usuario,
                "usuario": usuario_dict if usuario_dict else 'nenhum registro',
                "curso_id_curso": self.curso_id_curso,
                "curso": curso.nome if curso else "nenhum curso",
                "id_portaria": self.id_portaria
            }
    
    @classmethod
    def query_all_names(cls):
        return super().query_all_names(cls.nome, cls.id_portaria)

    def __repr__(self):
        return '<portaria %r>' % self.nome
