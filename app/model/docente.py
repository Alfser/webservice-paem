from ..database import db
from .curso import CursoModel
from .disciplina import DisciplinaModel
from .usuario import UsuarioModel
from .campus import CampusModel
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

    disciplinas = db.relationship('DisciplinaModel', secondary='docente_has_disciplina', lazy='select',
                                                        backref=db.backref('docentes', lazy=True))
    
    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, lazy='select')

    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=True)
    campus = db.relationship('CampusModel', uselist=False, lazy='select')

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)
    
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

        try:    
            usuario_dict = self.usuario.serialize()
        
        except AttributeError as msg:
            print("usuario não cadastrado.")
            usuario_dict = None
        
        finally:
            curso = db.session.query(
                CursoModel.nome
            ).filter_by(id_curso=self.curso_id_curso).first()
            
            campus = db.session.query(
                CampusModel.nome
            ).filter_by(id_campus=self.campus_id_campus).first()
            
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
                "curso": curso.nome if curso else "nenhum curso",
                "campus_id_campus":self.campus_id_campus,
                "campus": campus.nome if campus else "nenhum campus"
            }
    
    @classmethod
    def query_all_names(cls):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_docente.label("id"),
            cls.siape.label("other_id")
        )

    def __repr__(self):
        return '<docente %r>' % self.id_direcao
