from ..database import db
from .disciplina import DisciplinaModel
from .usuario import UsuarioModel


# table to relationship many to many
db.Table('docente_has_disciplina', db.Column('docente_siape', db.String(45), db.ForeignKey('docente.siape'), primary_key=True),
                                    db.Column('disciplina_id_disciplina', db.Integer, db.ForeignKey('disciplina.id_disciplina'), primary_key=True),
                                    db.Column('data', db.Date, nullable=False)
                                )

class DocenteModel(db.Model):
    __tablename__ = "docente"

    id_docente = db.Column(db.Integer, primary_key=True)
    siape = db.Column(db.String(45), unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_afastamento = db.Column(db.SmallInteger, nullable=True)
    escolaridade = db.Column(db.String(45), nullable=True)
    situacao = db.Column(db.String(45), nullable=True)

    disciplina = db.relationship('DisciplinaModel', secondary='docente_has_disciplina', lazy='subquery',
                                                        backref=db.backref('docentes', lazy=True))
    
    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, backref=db.backref('docente', lazy=True))

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)
    
    def __init__(self, siape, 
                        nome, 
                        data_nascimento, 
                        escolaridade, 
                        status_covid=None, 
                        status_afastamento=None, 
                        situacao=None, 
                        usuario_id_usuario=None, 
                        curso_id_curso=None
                                            ):

        self.siape = siape
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.status_covid = status_covid
        self.status_afastamento = status_afastamento
        self.situacao = situacao
        self.usuario_id_usuario
        self.curso_id_curso = curso_id_curso


    def __repr__(self):
        return '<docente %r>' % self.id_direcao
