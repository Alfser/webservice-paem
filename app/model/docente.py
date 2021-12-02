from ..database import db
from .curso import CursoModel
from .disciplina import DisciplinaModel
from .usuario import UsuarioModel
from .campus_instituto import CampusInstitutoModel
from .base_model import BaseHasSiape, BaseHasUsuarioModel
from datetime import datetime

# table to relationship many to many
db.Table('docente_has_disciplina', db.Column('docente_siape', db.String(45), db.ForeignKey('docente.siape'), primary_key=True),
                                    db.Column('disciplina_id_disciplina', db.Integer, db.ForeignKey('disciplina.id_disciplina'), primary_key=True),
                                    db.Column('data', db.Date, nullable=False)
                                )

class DocenteModel(BaseHasUsuarioModel, BaseHasSiape, db.Model):
    __tablename__ = "docente"

    id_docente = db.Column(db.Integer, primary_key=True)
    siape = db.Column(db.String(45), unique=True, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    __data_nascimento = db.Column("data_nascimento", db.Date, nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_afastamento = db.Column(db.SmallInteger, nullable=True)
    escolaridade = db.Column(db.String(45), nullable=True)
    situacao = db.Column(db.String(45), nullable=True)
    sexo = db.Column(db.String(2), nullable=True)
    quantidade_pessoas = db.Column(db.Integer, nullable=True)
    quantidade_vacinas = db.Column(db.Integer, nullable=True)
    fabricante = db.Column(db.String(45), nullable=True)
    justificativa = db.Column(db.Text, nullable=True)
    carteirinha_vacinacao = db.Column(db.Text, nullable=True)

    disciplinas = db.relationship('DisciplinaModel', secondary='docente_has_disciplina', lazy='select',
                                                        backref=db.backref('docentes', lazy=True))
    
    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', cascade="all, delete", uselist=False, lazy='select')

    campus_instituto_id_campus_instituto = db.Column(db.Integer, db.ForeignKey('campus_instituto.id_campus_instituto'), nullable=True)
    campus_instituto = db.relationship('CampusInstitutoModel', uselist=False, lazy='select')

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)
    
    @property
    def data_nascimento(self):
        return str(self.__data_nascimento)

    @data_nascimento.setter
    def data_nascimento(self, data):
        if isinstance(data, str) and data.find("-")!=-1:
            data = datetime.strptime(data, "%Y-%m-%d")
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
            
            campus_instituto = db.session.query(
                CampusInstitutoModel.nome
            ).filter_by(id_campus_instituto=self.campus_instituto_id_campus_instituto).first()
            
            return {
                "id_docente":self.id_docente,
                "siape":self.siape,
                "nome":self.nome,
                "data_nascimento":self.data_nascimento,
                "status_covid":self.status_covid,
                "status_afastamento":self.status_afastamento,
                "situacao":self.situacao,
                "sexo": self.sexo,
                "carteirinha_vacinacao":self.carteirinha_vacinacao,
                "quantidade_pessoas": self.quantidade_pessoas,
                "quantidade_vacinas": self.quantidade_vacinas,
                "fabricantes": self.fabricante,
                "justificativa": self.justificativa,
                "usuario_id_usuario":self.usuario_id_usuario,
                "usuario": usuario_dict if usuario_dict else None,
                "curso_id_curso":self.curso_id_curso,
                "curso": curso.nome if curso else None,
                "campus_instituto_id_campus_instituto":self.campus_instituto_id_campus_instituto,
                "campus_instituto":campus_instituto.nome if campus_instituto else None
            }
    
    @classmethod
    def get_vacinacao(cls, siape_docente):
        docente = cls.find_by_siape(
            cls.id_docente,
            cls.nome,
            cls.fabricante,
            cls.status_covid,
            cls.quantidade_vacinas,
            cls.justificativa,
            cls.carteirinha_vacinacao,
            siape=siape_docente
        )

        if docente:
            return {
                "id_docente":docente.id_docente,
                "nome":docente.nome,
                "carteirinha_vacinacao":docente.carteirinha_vacinacao,
                "fabricante":docente.fabricante,
                "status_covid":docente.status_covid,
                "quantidade_vacinas":docente.quantidade_vacinas,
                "justificativa": docente.justificativa
            }
        return None
        
    @classmethod
    def query_all_names(cls):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_docente.label("id"),
            cls.siape.label("other_id")
        )

    def __repr__(self):
        return '<docente %r>' % self.id_direcao
