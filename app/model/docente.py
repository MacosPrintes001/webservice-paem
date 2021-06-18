from ..database import db
from .curso import CursoModel
from .disciplina import DisciplinaModel
from .usuario import UsuarioModel
from .base_model import BaseHasNameModel
from datetime import date

# table to relationship many to many
db.Table('docente_has_disciplina', db.Column('docente_siape', db.String(45), db.ForeignKey('docente.siape'), primary_key=True),
                                    db.Column('disciplina_id_disciplina', db.Integer, db.ForeignKey('disciplina.id_disciplina'), primary_key=True),
                                    db.Column('data', db.Date, nullable=False)
                                )

class DocenteModel(BaseHasNameModel, db.Model):
    __tablename__ = "docente"

    id_docente = db.Column(db.Integer, primary_key=True)
    siape = db.Column(db.String(45), unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    __data_nascimento = db.Column("data_nascimento", db.Date, nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_afastamento = db.Column(db.SmallInteger, nullable=True)
    escolaridade = db.Column(db.String(45), nullable=True)
    situacao = db.Column(db.String(45), nullable=True)

    disciplina = db.relationship('DisciplinaModel', secondary='docente_has_disciplina', lazy='subquery',
                                                        backref=db.backref('docentes', lazy=True))
    
    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, lazy='noload', backref=db.backref('docente', lazy='noload'))

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)
    
    def __init__(self, siape, 
                        nome, 
                        data_nascimento, 
                        escolaridade, 
                        status_covid=None, 
                        status_afastamento=None, 
                        situacao=None, 
                        usuario_id_usuario=None, 
                        curso_id_curso=None,
                        id_docente=None ):

        self.id_docente = id_docente
        self.siape = siape
        self.nome = nome
        self.escolaridade = escolaridade
        self.data_nascimento = data_nascimento
        self.status_covid = status_covid
        self.status_afastamento = status_afastamento
        self.situacao = situacao
        self.usuario_id_usuario = usuario_id_usuario
        self.curso_id_curso = curso_id_curso
    
    @property
    def data_nascimento(self):
        return str(self.__data_nascimento)

    @data_nascimento.setter
    def data_nascimento(self, data):
        if isinstance(data, str):
            day, month, year = data.split('-')
            data = date(day=int(day), month=int(month), year=int(year))
        
        self.__data_nascimento = data


    def serialize(self):

        usuario_dict = self.usuario.serialize()

        return {
            "id_docente":self.id_docente,
            "siape":self.siape,
            "nome":self.nome,
            "data_nascimento":self.data_nascimento,
            "status_covid":self.status_covid,
            "status_afastamento":self.status_afastamento,
            "situacao":self.situacao,
            "usuario_id_usuario":self.usuario_id_usuario,
            "usuario": usuario_dict if usuario_dict else 'nenhum registro',
            "curso_id_curso":self.curso_id_curso,
            "curso": db.session.query(CursoModel.nome).filter_by(id_curso=self.curso_id_curso).first().nome
        }
    
    @classmethod
    def query_all_names(cls):
        return super().query_all_names(cls.nome, cls.id_tecnico)

    def __repr__(self):
        return '<docente %r>' % self.id_direcao
