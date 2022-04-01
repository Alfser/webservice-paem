'''
    Módulo com a classe modelo da tabela `coordenacao`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database import db
from .curso import CursoModel
from .docente import DocenteModel


class CoordenacaoModel(db.Model):
    '''
        Classe-modelo para a tabela `coodenacao` que é destina ao coodenador de cada curso.

        ...

        Atrinutos
        ---------
        `id_coordenacao : int`
        `data_entrada : Date(yyyy-mm-dd)| None`
        `data_saida : Date(yyyy-mm-dd)| None`
        `status_ativo : int | None`
        `curso_id_curso : int`
        `curso : list[CursoModel]`
        `docente_id_docente : int`
        `docente : list[DocenteModel]`

        Métodos
        -------
        serialize() : dict
                Retorna um dicionário com os dados da tabela para API expor como JSON.
    '''
    __tablename__ = "coordenacao"
    
    id_coordenacao = db.Column(db.Integer, primary_key=True)
    data_entrada = db.Column(db.Date, nullable=True)
    data_saida = db.Column(db.Time, nullable=True)
    status_ativo = db.Column(db.SmallInteger, nullable=True)
    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=False)
    curso = db.relationship('CursoModel', uselist=False, lazy='select')

    docente_id_docente = db.Column(db.Integer, db.ForeignKey('docente.id_docente'), nullable=False)
    docente = db.relationship('DocenteModel', uselist=False, lazy='select')

    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `coodenador`.
        '''
        return {
            "id_coodenador":self.id_coordenacao,
            "data_entrada":self.data_entrada,
            "data_saída":self.data_saida,
            "status_ativo":self.status_ativo,
            "curso_id_curso":self.curso_id_curso,
            "curso":self.curso,
            "docente_id_docente":self.docente_id_docente,
            "docente":self.docente
        }

    def __repr__(self):
        return '<coordenacao %r>' % self.nome
