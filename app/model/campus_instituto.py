'''
    Módulo com a classe modelo da tabela `campus_instituto`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''

from ..database import db
from .base_model import BaseHasNameModel

from datetime import datetime

class CampusInstitutoModel(BaseHasNameModel, db.Model):
    '''
       Classe modelo para a tabela campus_instituto do banco de dados.

       ...

       Atributos
       ---------
       `id_campus_instituto : int`
                Identificador do campus ou instituto.
       `ano_fundacao : str (yyyy-mm-dd)`
                Ano da fundação do campus ou instituto.
       `nome : str`
                Nome do campus ou instituto.
       `abertura_total : int`
                Se o campus ou instituto tem abertura total, ou seja, se o campus ou instituto permite ou não a entrada sem ter tomado a vacina contra a Covid-19.
       `direcao_id_direcao : int`
                Identificador da tabela direcao
       `direcao : list[DirecaoModel]`
                Lista com as direção(s) dos crusos do campus ou institutos.
        
        Métodos
        -------
        `serialize(): dict`
                Retorna um dicionário com os dados da tabela para API expor como JSON.
        `@classmethod`
        `query_all_names(campus_instituto=None):`
                Consulta os dados da tabela descrita pelo objeto-modelo filtrando por campus ou instituto, se for diferente de `None`
    '''

    __tablename__ = "campus_instituto"

    id_campus_instituto = db.Column(db.Integer, primary_key=True)
    __ano_fundacao = db.Column('ano_fundacao', db.Date, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    abertura_total = db.Column(db.SmallInteger, nullable=False)

    direcao_id_direcao = db.Column(db.Integer, db.ForeignKey('direcao.id_direcao'), nullable=True)
    direcao = db.relationship('DirecaoModel', uselist=False, lazy='select')

    @property
    def ano_fundacao(self):
        return str(self.__ano_fundacao)

    @ano_fundacao.setter
    def ano_fundacao(self, data):
        if isinstance(data, str) and data.find("-")!=-1:
            try:
                data = datetime.strptime(data, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Erro: A data deve ser enviada no formato 'YYYY-mm-dd'")    


        self.__ano_fundacao = data

    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela, identificada pelo objeto-modelo, para API expor como JSON.

            Retorno
            -------
            dicionário `dict` com os dados da tabela `campus_instituto`.
        '''
        
        try:
            docente_dict = self.direcao.docente.serialize()
        except AttributeError as msg:
            docente_dict = None
        finally:
            return {
                "id_campus_instituto":self.id_campus_instituto,
                "nome":self.nome,
                "abertura_total":self.abertura_total,
                "ano_fundacao":self.ano_fundacao,
                'direcao_id_direcao': self.direcao_id_direcao,
                "direcao": docente_dict if docente_dict else None 
            }

    @classmethod
    def query_all_names(cls, campus_instituto=None):
        '''
            Consulta os dados da tabela descrita pelo objeto-modelo filtrando por campus ou instituto, se for diferente de `None`

            Parâmetros
            ----------
            `campus_instituto : int | None`
                    Identificador do campus ou instituto.
                    
            Retorna
            -------
            Uma `list` com objetos do tipo `CampusInstitutoModel`
        '''
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_campus_instituto.label("id"), 
            campus_instituto_id_campus_instituto=campus_instituto
        )

    def __repr__(self):
        return '<campus %r>' % self.nome