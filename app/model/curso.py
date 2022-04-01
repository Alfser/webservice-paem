'''
    Módulo com a classe modelo da tabela `curso`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database import db
from .disciplina import DisciplinaModel
from .base_model import BaseHasNameModel
from .campus_instituto import CampusInstitutoModel

from datetime import datetime

class CursoModel(BaseHasNameModel, db.Model):
    '''
        Classe-modelo que representa a tabela `curso` do banco de dados.

        ...

        Atributos
        ---------
        `id_curso : int`
                Identificador do curso.
        `nome : str`
                Nome do curso.
        `data_fundacao : Date(yyyy-mm-dd)`
                Ano de fundação do curso.
        `unidade : str`
                Unidade a qual pertence o curso.
        `cidade : str`
                Cidade a qual o curso é ofertado.
        `grau_academico : string`
                Grau acadêmico do curso(Bacharel, licenciatura...).
        `situacao : str`
                situação do curso.
        `modalidade : str`
                modalidade do curso.
        `convenio : str`
                convênio do curso.
        `ativo : int`
                se o curso está ativo.
        `campus_instituto_id_campus_instituto : int`
                Identificador do campus ou instituto do curso.
        `docentes : list[DocenteModel]`
                Lista de docentes que fazem parte desse curso.
        `disciplinas : list[DisciplinaModel]`
                Lista de disciplinas que pertencem a esse curso.
        `discentes : list[DiscenteModel]`
                Lista de discentes que são desse curso.
        
        Métodos
        -------
        `serialize(): dict`
                Retorna um dicionário com os dados da tabela para API expor como JSON.
        `@classmethod`
        `query_all_names(campus_instituto=None):`
                Consulta os dados da tabela `curso` filtrando por campus ou instituto.
    '''
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
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `curso`.
        '''

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
        '''
            Consulta os dados da tabela `curso` filtrando por campus ou instituto.

            ...

            Parâmetros
            ----------
            `campus_instituto_id_campus_instituto : int`
                    Identificador do campus ou instituto selecionado para o filtro.
        '''

        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_curso.label("id"), 
            campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto
        )
        
    def __repr__(self):
        return '<curso %r>' % self.nome