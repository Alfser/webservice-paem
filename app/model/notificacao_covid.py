from ..database import db
from .base_model import BaseModel
from datetime import datetime

class NotificacaoCovidModel(BaseModel, db.Model):
    __tablename__ = "notificacao_covid"

    id_notificacao_covid = db.Column(db.Integer, primary_key=True)
    __data = db.Column('data', db.Date, nullable=True)
    teste = db.Column(db.Boolean, nullable=True)
    nivel_sintomas = db.Column(db.SmallInteger, nullable=True) # 0-não desejo informar, 1-leve, 2-moderado, 3-grave
    
    matricula_discente = db.Column(
        db.String(45), 
        db.ForeignKey("discente.matricula"), 
        nullable=True
    )
    discente = db.relationship('DiscenteModel', uselist=True, lazy='noload')


    campus_instituto_id_campus_instituto = db.Column(
        db.Integer,
        db.ForeignKey("campus_instituto.id_campus_instituto"),
        nullable=True
    )
    campus_instituto = db.relationship('CampusInstitutoModel', uselist=True, lazy='select')

    @property
    def data(self):
        return str(self.__data)

    @data.setter
    def data(self, data):
        if isinstance(data, str) and data.find("-")!=-1:
            data = datetime.strptime(data, "%Y-%m-%d")
        self.__data = data

    def serialize(self):
        return {
            "id_notificacao_covid":self.id_notificacao_covid,
            "data":self.data,
            "teste":self.teste,
            "nivel_sintomas":self.nivel_sintomas,
            "matricula_discente":self.matricula_discente,
            "campus_instituto_id_campus_instituto":self.campus_instituto_id_campus_instituto
        }

    def __repr__(self):
        return '<notificacao_covid %r>' % self.data