from ..database import db
from .disciplina import DisciplinaModel
from .base_model import BaseHasNameModel
from .campus_instituto import CampusInstitutoModel

from datetime import datetime

class CursoModel(BaseHasNameModel, db.Model):
    __tablename__='curso'

    id_curso = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    __data_fundacao = db.Column("data_fundacao", db.Date, nullable=True)
    unidade = db.Column(db.String(45), nullable=True)
    cidade = db.Column(db.String(45), nullable=True)
    grau_academico = db.Column(db.String(45), nullable=True)
    situacao = db.Column(db.String(45), nullable=True)
    modalidade = db.Column(db.String(45), nullable=True)
    convenio = db.Column(db.String(45), nullable=True)
    ativo = db.Column(db.SmallInteger, nullable=True)
    
    campus_instituto_id_campus_instituto = db.Column(db.Integer, db.ForeignKey('campus_instituto.id_campus_instituto'), nullable=True)
    campus_instituto = db.relationship('CampusInstitutoModel', lazy='select', uselist=False)

    docentes = db.relationship('DocenteModel', uselist=True, backref=db.backref('curso', uselist=False, lazy='select'))
    
    disciplinas = db.relationship('DisciplinaModel', uselist=True, lazy='select', backref=db.backref('curso', uselist=False, lazy='select'))

    discentes = db.relationship('DiscenteModel', uselist=True, backref=db.backref('curso', uselist=False, lazy='select'))
    
    @property
    def data_fundacao(self):
        return str(self.__data_fundacao)
    
    @data_fundacao.setter
    def data_fundacao(self, data):
        if isinstance(data, str) and data.find("-")!=-1:
            data = datetime.strptime(data, "%Y-%m-%d")
        self.__data_fundacao = data
        
    def serialize(self):
        campus_instituto = db.session.query(
            CampusInstitutoModel.nome
        ).filter_by(id_campus_instituto=self.campus_instituto_id_campus_instituto).first()

        return {
            "id_curso":self.id_curso,
            "nome":self.nome,
            "data_fundacao":self.data_fundacao,
            "campus_instituto_id_campus_instituto":self.campus_instituto_id_campus_instituto,
            "campus_instituto": campus_instituto.nome if campus_instituto else None,
            "unidade":self.unidade,
            "cidade":self.cidade,
            "grau_academico":self.grau_academico,
            "situacao":self.situacao,
            "modalidade":self.modalidade,
            "convenio":self.convenio,
            "ativo":self.ativo
        }

    @classmethod
    def query_all_names(cls, campus_instituto_id_campus_instituto):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_curso.label("id"), 
            campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto
        )
        
    def __repr__(self):
        return '<curso %r>' % self.nome