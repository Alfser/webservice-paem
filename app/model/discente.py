
from .curso import CursoModel
from .usuario import UsuarioModel
from .campus import CampusModel
from .base_model import BaseHasUsuarioModel 
from ..database import db
from app.model import usuario

class DiscenteModel(BaseHasUsuarioModel, db.Model):
    __tablename__='discente'

    id_discente = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(45), unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    entrada = db.Column(db.String(6), nullable=True)
    semestre = db.Column(db.Integer, nullable=True)
    endereco = db.Column(db.String(45), nullable=True)
    grupo_risco = db.Column(db.SmallInteger, nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_permissao = db.Column(db.SmallInteger, nullable=True) # if is covid or not

    # TODO: add status_alerta

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, lazy='select')

    campus_id_campus = db.Column(db.Integer, db.ForeignKey('campus.id_campus'), nullable=True)
    campus = db.relationship('CampusModel', uselist=False, lazy='select')

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)

    solicitacoes_acesso = db.relationship('SolicitacaoAcessoModel', uselist=False, lazy='select')

    def serialize(self):

        try:
            usuario_dict = self.usuario.serialize()
        except AttributeError as msg:
            print("usuário não cadastrado")
            usuario_dict = None
        
        finally:

            curso = db.session.query(
                CursoModel.nome
            ).filter_by(id_curso=self.curso_id_curso).first()
            
            campus = db.session.query(
                CampusModel.nome
            ).filter_by(id_campus=self.campus_id_campus).first()

            return {
                "id_discente": self.id_discente, 
                "nome": self.nome,
                "matricula": self.matricula,
                "entrada":self.entrada,
                "semestre":self.semestre,
                "endereco":self.endereco,
                "grupo_risco":self.grupo_risco,
                "status_covid":self.status_covid,
                "status_permissao":self.status_permissao,
                "usuario": usuario_dict if usuario_dict else "null",
                "curso": curso.nome if curso else "null",
                "campus_id_campus":self.campus_id_campus,
                "campus": campus.nome if campus else "null"
            }
    
    @classmethod
    def find_by_matricula(cls, matricula):
       return cls.query.filter_by(matricula=matricula).first()
    
    @classmethod
    def update_by_matricula(cls, matricula, dict):
       cls.query.filter_by(matricula=matricula).update(dict)
       cls.save()

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_discente.label("id"),
            cls.matricula.label("other_id")
        )
    
    def __repr__(self):
        return '<discente %r>' % self.login