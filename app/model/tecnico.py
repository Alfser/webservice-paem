from ..database import db
from .usuario import UsuarioModel
from .campus_instituto import CampusInstitutoModel
from .base_model import BaseHasUsuarioModel
from datetime import date

class TecnicoModel(BaseHasUsuarioModel, db.Model):
    __tablename__ = "tecnico"

    id_tecnico = db.Column(db.Integer, primary_key=True)
    siape = db.Column(db.String(45), unique=True, nullable=False)
    nome = db.Column(db.String(45), nullable=False)
    __data_nascimento = db.Column('data_nascimento', db.Date, nullable=True)
    cargo = db.Column(db.String(45), nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_afastamento = db.Column(db.SmallInteger, nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', lazy='select', uselist=False)

    campus_instituto_id_campus_instituto = db.Column(db.Integer, db.ForeignKey('campus_instituto.id_campus_instituto'), nullable=True)
    campus_instituto = db.relationship('CampusInstitutoModel', uselist=False, lazy='noload')

    @property
    def data_nascimento(self):
        return str(self.__data_nascimento)

    @data_nascimento.setter
    def data_nascimento(self, data):
          if isinstance(data, str):
              day, month, year = data.split('-')
              data = date(day=int(day), month=int(month), year=int(year))

          self.__data_nascimento = data

    def serialize(self):
        try:
            usuario_dict = self.usuario.serialize()
        
        except AttributeError as msg:
            print("Warning: Usuário não cadatrado para este trécnico")
            usuario_dict = None
        
        finally:
            campus_instituto = db.session.query(
                CampusInstitutoModel.nome
            ).filter_by(id_campus=self.campus_instituto_id_campus_instituto).first() # query name and get name from tuple
            
            return {
                'id_tecnico':self.id_tecnico,
                'siape':self.siape, 
                'nome':self.nome, 
                'data_nascimento':self.data_nascimento, 
                "cargo":self.cargo,
                'status_covid':self.status_covid, 
                'status_afastamento':self.status_afastamento, 
                'usuario_id_usuario':self.usuario_id_usuario,
                'usuario': usuario_dict if usuario_dict else None,
                'campus_id_campus':self.campus_instituto_id_campus_instituto,
                'campus': campus_instituto.nome if campus_instituto else None
            }

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_tecnico.label("id"), 
            cls.siape.label("other_id")
        )
    
    def __repr__(self):
        return '<tecnico %r>' % self.nome
