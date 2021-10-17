from ..database import db
from .campus_instituto import CampusInstitutoModel
from .base_model import BaseHasUsuarioModel

class PontoVerificacaoModel(BaseHasUsuarioModel, db.Model):
    __tablename__ = "ponto_verificacao"

    id_ponto_verificacao = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=True)
    descricao = db.Column(db.Text, nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, lazy='select')

    campus_instituto_id_campus_instituto = db.Column(db.Integer, db.ForeignKey('campus_instituto.id_campus_instituto'))
    campus_instituto = db.relationship('CampusInstitutoModel', uselist=True, lazy='select')

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_ponto_verificacao.label("id")
        )

    def serialize(self):
        try:    
            usuario_dict = self.usuario.serialize()
        
        except AttributeError as msg:
            print("usuario não cadastrado.")
            usuario_dict = None
        
        campus_instituto = db.session.query(
                CampusInstitutoModel.nome
            ).filter_by(id_campus_instituto=self.campus_instituto_id_campus_instituto).first()
        
        return{
            "id_ponto_verificacao":self.id_ponto_verificacao,
            "nome":self.nome,
            "descricao":self.descricao,
            "campus_instituto_id_campus_instituto":self.campus_instituto_id_campus_instituto,
            "campus_instituto": campus_instituto.nome if campus_instituto else None,
            "usuario_id_usuario":self.usuario_id_usuario,
            "usuario": usuario_dict if usuario_dict else None
        }
        