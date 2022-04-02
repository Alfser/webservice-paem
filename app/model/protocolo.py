'''
    Módulo com a classe modelo da tabela `protocolo`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database import db
from .usuario import UsuarioModel
from .base_model import BaseModel

class ProtocoloModel(BaseModel, db.Model):
    '''
        Classe-modelo que mapeia a tabela `protocolo`, que, por sua vez é responsável pelo registro das conversão de usuário com o `chatbot`.

        ...

        Atributos
        ---------
        `id_protocolo : int`
                Identificador do protocolo.
        `mensagens : string | None`
                As mensagens enviadas ao chatbot.
        `usuario_id_usuario : int | None`
                O identificador do usuário que enviou as menságens ao chatboot.
        `usuario : UsuarioModel`
                Dados do usuário que enviou as menságens ao chatboot.
        
        Métodos
        -------
        `serialize(): dict`
            Retorna um dicionário com os dados da tabela para API expor como JSON.
    '''

    __tablename__ = "protocolo"

    id_protocolo = db.Column(db.Integer, primary_key=True)
    mensagens = db.Column(db.Text, nullable=True)
    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', lazy='select')

    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `protocolo`.
        '''
        try:
            usuario_dict = self.usuario.serialize()
        except AttributeError as msg:
            print("Usuário não cadastrado.")
            usuario_dict = None

        return {
            "id_protocolo": self.id_protocolo,
            "mensagens": self.mensagens,
            "usuario_id_usuario": self.usuario_id_usuario,
            "usuario": usuario_dict if usuario_dict else None
        }
