
from .curso import CursoModel
from .usuario import UsuarioModel
from .campus_instituto import CampusInstitutoModel
from .base_model import BaseHasUsuarioModel 
from datetime import date
from ..database import db
from app.model import usuario

class DiscenteModel(BaseHasUsuarioModel, db.Model):
    __tablename__='discente'

    id_discente = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(45), unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    entrada = db.Column(db.String(6), nullable=True)
    carteirinha_vacinacao = db.Column(db.LargeBinary, nullable=True)
    __data_nascimento = db.Column('data_nascimento', db.Date, nullable=True)
    ano_de_ingresso = db.Column(db.Integer, nullable=True)
    sexo = db.Column(db.String(2), nullable=True)
    quantidade_pessoas = db.Column(db.Integer, nullable=True)
    quantidade_vacinas = db.Column(db.Integer, nullable=True)
    fabricante = db.Column(db.String(45), nullable=True)
    justificativa = db.Column(db.Text, nullable=True)
    semestre = db.Column(db.Integer, nullable=True)
    endereco = db.Column(db.String(45), nullable=True)
    grupo_risco = db.Column(db.SmallInteger, nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_permissao = db.Column(db.SmallInteger, nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, lazy='select')

    campus_instituto_id_campus_instituto = db.Column(db.Integer, db.ForeignKey('campus_instituto.id_campus_instituto'), nullable=True)
    campus = db.relationship('CampusInstitutoModel', uselist=False, lazy='select')

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)

    solicitacoes_acesso = db.relationship('SolicitacaoAcessoModel', uselist=False, lazy='select')

    @classmethod
    def find_by_matricula(cls, matricula):
       return cls.query.filter_by(matricula=matricula).first()
    
    @classmethod
    def update_by_matricula(cls, matricula, dict):
       cls.query.filter_by(matricula=matricula).update(dict)
       cls.save()
    
    @property
    def data_nascimento(self):
        return str(self.__data_nascimento)

    @data_nascimento.setter
    def data_nascimento(self, data):
        if isinstance(data, str) and data.find("-")!=-1:
            day, month, year = data.split('-')
            data = date(day=int(day), month=int(month), year=int(year))

        self.__data_nascimento = data

    @classmethod
    def get_vacinacao(cls, matricula_discente):
        discente = cls.find_by_matricula(matricula_discente)

        if discente:
            return {
                "id_discente":discente.id_discente,
                "nome":discente.nome,
                "carteirinha_vacinacao":discente.carteirinha_vacinacao,
                "fabricante":discente.fabricante,
                "status_covid":discente.status_covid,
                "quantidade_vacinas":discente.quantidade_vacinas,
                "justificativa": discente.justificativa
            }
        
        return None

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
            
            campus_instituto = db.session.query(
                CampusInstitutoModel.nome
            ).filter_by(id_campus_instituto=self.campus_instituto_id_campus_instituto).first()

            return {
                "id_discente": self.id_discente, 
                "nome": self.nome,
                "matricula": self.matricula,
                "entrada": self.entrada,
                "data_nascimento": self.data_nascimento,
                "ano_de_ingresso": self.ano_de_ingresso,
                "sexo": self.sexo,
                "carteirinha_vacinacao":self.carteirinha_vacinacao,
                "quantidade_pessoas": self.quantidade_pessoas,
                "quantidade_vacinas": self.quantidade_vacinas,
                "fabricantes": self.fabricante,
                "justificativa": self.justificativa,
                "semestre": self.semestre,
                "endereco": self.endereco,
                "grupo_risco": self.grupo_risco,
                "status_covid": self.status_covid,
                "status_permissao": self.status_permissao,
                "usuario": usuario_dict if usuario_dict else None,
                "curso_id_curso": self.curso_id_curso,
                "curso": curso.nome if curso else None,
                "campus_instituto_id_campus_instituto": self.campus_instituto_id_campus_instituto,
                "campus_instituto": campus_instituto.nome if campus_instituto else None
            }
    
    

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_discente.label("id"),
            cls.matricula.label("other_id")
        )
    
    def __repr__(self):
        return '<discente %r>' % self.login