'''
    Módulo com a classe modelo da tabela `portaria`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database import db
from .usuario import UsuarioModel
from .base_model import BaseHasUsuarioModel, BaseHasSiape

from datetime import datetime

class PortariaModel(BaseHasUsuarioModel, BaseHasSiape, db.Model):
    '''
        Classe-modelo que mapeia a tabela `portaria`, que por sua vez é responsável pelo cadastreo do usuário do porteiro.

        ...

        Atributos
        ---------
        `id_portaria : int`
                Identificador do cadatro portiro. 
        `nome : str`
                Nome do porteiro.
        `data_nascimento : Date(yyyy-mm-dd)` | None
        `funcao : str | None`
                Função do porteiro.
        `turno_trabalho : int`
                Turno de trabalho do porteiro.
        `usuario_id_usuario : int | None`
                Identificador do usuário do porteiro. 
        `usuario : UsuarioModel`
            Dados do usuário do porteiro.
        `campus_instituto_id_campus_instituto : int | None`
                Campus ou instituto do porteiro.
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto do porteiro.
        Métodos
        -------
        `serialize(): dict`
            Retorna um dicionário com os dados da tabela para API expor como JSON.
        
    '''

    __tablename__ = "portaria"

    id_portaria = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    __data_nascimento = db.Column('data_nascimento',db.Date, nullable=True)
    funcao = db.Column(db.String(45), nullable=True)
    turno_trabalho = db.Column(db.SmallInteger, nullable=False)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel',cascade="all, delete", lazy='select')

    campus_instituto_id_campus_instituto = db.Column(db.Integer, db.ForeignKey('campus_instituto.id_campus_instituto'), nullable=True)
    campus_instituto = db.relationship('CampusInstitutoModel', lazy="select")

    @property
    def data_nascimento(self):
        return str(self.__data_nascimento)

    @data_nascimento.setter
    def data_nascimento(self, data):
        if isinstance(data, str) and data.find("-")!=-1:
            
            try:
                data = datetime.strptime(data, "%Y-%m-%d")
            except:
                raise ValueError("A data deve ser enviada no formato 'YYYY-mm-dd'")    
        
        self.__data_nascimento = data

    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `portaria`
        '''
        
        try:
            usuario_dict = self.usuario.serialize()
        except AttributeError as msg:
            # print("Usuário não cadastrado.")
            usuario_dict = None

        finally:
            return {
                "nome": self.nome,
                "data_nascimento": self.data_nascimento,
                "funcao": self.funcao,
                "turno_trabalho": self.turno_trabalho,
                "usuario_id_usuario": self.usuario_id_usuario,
                "usuario": usuario_dict if usuario_dict else None,
                "id_portaria": self.id_portaria
            }
    
    @classmethod
    def query_all_names(cls, campus_instituto_id_campus_instituto):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_portaria.label("id"),
            campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto
        )

    def __repr__(self):
        return '<portaria %r>' % self.nome
