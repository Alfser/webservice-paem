'''
    Módulo com a classe modelo da tabela `direcao`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database.db import db
from .docente import DocenteModel
from datetime import datetime

class DirecaoModel(db.Model):
    '''
        Classe modelo que mapeia a tabela `direcao`, onde descreve quem esteve ou está na direção do campus.

        ...

        Atributos
        ---------
        `id_direcao : int`    
                Identificador da direção.
        `data_entrada : Date(yyyy-mm-dd)`
                Data de entrada na direção do campus.
        `data_saida : Date(yyyy-mm-dd)`
                Data de saída da direção do campus.
        `status_ativo` : INT | None
                Se está ativo na direção do campus.
        `docente_id_docente` : int| None
                Identificador do docente que está ma direção do campus.
        `docente : DocenteModel`
                Dados do docente que está na direção do campus.

        Métodos
        -------
        serialize() : dict
                Retorna um dicionário com os dados da tabela para API expor como JSON.
    '''
    
    __tablename__ = "direcao"

    id_direcao = db.Column(db.Integer, primary_key=True)
    __data_entrada = db.Column("data_entrada", db.Date, nullable=False)
    __data_saida = db.Column("data_saida", db.Date, nullable=False)
    status_ativo = db.Column(db.SmallInteger, nullable=True)
    
    docente_id_docente = db.Column(db.Integer, db.ForeignKey('docente.id_docente'), nullable=True)
    docente = db.relationship('DocenteModel', uselist=False, lazy='select')

    @property
    def data_entrada(self):
        return str(self.__data_entrada)

    @data_entrada.setter
    def data_entrada(self, data):
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Erro: A data deve ser enviada no formato 'YYYY-mm-dd'")    
        self.__data_entrada = data

    @property
    def data_saida(self):
        return str(self.__data_saida)

    @data_saida.setter
    def data_saida(self, data):
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Erro: A data deve ser enviada no formato 'YYYY-mm-dd'")    
        self.__data_saida = data

    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `direcao`.
        '''
        docente = db.session.query(
            DocenteModel.nome
        ).filter_by(id_docente=self.docente_id_docente).first()
        return {
            "id_direcao": self.id_direcao,
            "data_entrada": self.data_entrada,
            "data_saida": self.data_saida,
            "status": self.status_ativo,
            "docente": docente.nome if docente else None
        }

    def __repr__(self):
        return '<direcao %r>' % self.id_direcao
