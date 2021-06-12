from ..database import db
from .usuario import UsuarioModel
from .curso import CursoModel


class PortariaModel(db.Model):
    __tablename__ = "portaria"

    id_portaria = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    cpf = db.Column(db.String(15), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=True)
    funcao = db.Column(db.String(45), nullable=True)
    turno_trabalho = db.Column(db.SmallInteger, nullable=False)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', backref=db.backref('portaria', lazy=True))

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)
    curso = db.relationship('CursoModel', backref=db.backref('portaria', lazy=True))

    def __repr__(self):
        return '<portaria %r>' % self.nome
