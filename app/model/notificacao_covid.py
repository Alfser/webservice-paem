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

    @classmethod
    def contar_notificacao_por_campus(cls, ano, id_campus_instituto):
        query = db.engine.execute(
            "SELECT data, COUNT(id_notificacao_covid) FROM notificacao_covid, campus_instituto"
            " WHERE  notificacao_covid.campus_instituto_id_campus_instituto=id_campus_instituto"
            " AND campus_instituto_id_campus_instituto=%s"
            " AND YEAR(data)=%s GROUP BY MONTH(data)",
            id_campus_instituto, ano
        )

        meses = {1:"JAN", 2:"FEV" , 3:"MAR", 4:"ABR",
                    5:"MAI", 6:"JUN", 7:"JUL", 8:"AGO", 
                    9:"SET", 10:"OUT", 11:"NOV", 12:"DEZ"}
        
        dict_query = {"JAN":0, "FEV":0 , "MAR":0, "ABR":0,
                        "MAI":0, "JUN":0, "JUL":0, "AGO":0, 
                        "SET":0, "OUT":0, "NOV":0, "DEZ":0}
        for row in query:
            dict_query[meses[row[0].month]]=row[1]
        return dict_query

    @classmethod
    def contar_notificacao_por_curso(cls, ano, id_campus_instituto):
        query = db.engine.execute(
            "SELECT curso.nome, count(id_notificacao_covid) count_by_curso"
            " FROM notificacao_covid, discente, curso"
            " WHERE matricula_discente=matricula"
            " AND curso_id_curso=id_curso"
            " AND notificacao_covid.campus_instituto_id_campus_instituto=%s"
            " AND YEAR(data)=%s"
            " GROUP BY id_curso;",
            id_campus_instituto, ano
        )

        dict_query = dict()
        for row in query:
            dict_query[row[0]]=row[1]
        return dict_query


    def __repr__(self):
        return '<notificacao_covid %r>' % self.data