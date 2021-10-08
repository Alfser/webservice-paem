from ..database import db
from .base_model import BaseModel

from datetime import time


class AcessoPermitidoModel(BaseModel, db.Model):
      __tablename__ = "acesso_permitido"

      id_acesso_permitido = db.Column(db.Integer, primary_key=True)
      temperatura = db.Column(db.Float, nullable=True)
      matricula_discente = db.Column(db.String(45), nullable=True)
      recurso_campus_id_recurso_campus = db.Column(db.Integer, db.ForeignKey("recurso_campus.id_recurso_campus"), nullable=True)
      __hora_entrada = db.Column("hora_entrada", db.Time, nullable=True)
      __hora_saida = db.Column("hora_saida", db.Time, nullable=True)
    
      solicitacao_acesso_id_solicitacao_acesso = db.Column(
          db.Integer, 
          db.ForeignKey("solicitacao_acesso.id_solicitacao_acesso"), 
          nullable=True
        )
      recurso_campus = db.relationship('RecursoCampusModel', uselist=False, lazy='select')

      campus_instituto_id_campus_instituto = db.Column(
          db.Integer,
          db.ForeignKey("campus_instituto.id_campus_instituto"),
          nullable=True
        )
      campus_instituto = db.relationship('CampusInstitutoModel', uselist=True, lazy='select')

      @property
      def hora_entrada(self):
        return str(self.__hora_entrada)

      @hora_entrada.setter
      def hora_entrada(self, hora_entrada):

          if isinstance(hora_entrada, str):  
              hour_ent, minute_ent, second_ent = hora_entrada.split(':')
              hora_entrada = time(hour=int(hour_ent), minute=int(minute_ent), second=int(second_ent))
          
          self.__hora_entrada = hora_entrada

      @property
      def hora_saida(self):
          return str(self.__hora_saida)

      @hora_saida.setter
      def hora_saida(self, hora_saida):
          if isinstance(hora_saida, str):
              hour_sai, minute_sai, second_sai = hora_saida.split(':')
              hora_saida = time(hour=int(hour_sai), minute=int(minute_sai), second=int(second_sai))
         
          self.__hora_saida = hora_saida 
      
      def serialize(self):
          return {
              "id_acesso_permitido":self.id_acesso_permitido,
              "temperatura":self.temperatura,
              "hora_entrada":self.hora_entrada,
              "hora_saida":self.hora_saida,
              "matricula_discente":self.matricula_discente,
              "recurso_campus_id_recurso_campus":self.recurso_campus_id_recurso_campus,
              "recurso_campus":self.recurso_campus.nome if self.recurso_campus else None,
              "solicitacao_acesso_id_solicitacao_acesso":self.solicitacao_acesso_id_solicitacao_acesso,
              "campus_instituto_id_campus_instituto":self.campus_instituto_id_campus_instituto
          }

      def __repr__(self):
          return '<acesso_permitido %r>' % self.nome
