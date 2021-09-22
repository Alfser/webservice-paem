from ..database import db
from .usuario import UsuarioModel
from .base_model import BaseModel

class ProtocoloModel(BaseModel, db.Model):
    __tablename__ = "protocolo"

    id_protocolo = db.Column(db.Integer, primary_key=True)
    mensagens = db.Column(db.Text, nullable=True)
    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', lazy='select')


    def serialize(self):

        try:
            usuario_dict = self.usuario.serialize()
        except AttributeError as msg:
            print("Usuário não cadastrado.")
            usuario_dict = None

        return {
            "id_protocolo": self.id_protocolo,
            "mensagens": self.mensagens,
            "usuario_id_usuario": self.usuario_id_usuario,
            "usuario": usuario_dict if usuario_dict else 'nenhum registro'
        }
