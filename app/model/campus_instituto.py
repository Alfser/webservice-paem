# Table structure for table `campus`
from ..database import db
from .base_model import BaseHasNameModel

from datetime import datetime

class CampusInstitutoModel(BaseHasNameModel, db.Model):
    __tablename__ = "campus_instituto"

    id_campus_instituto = db.Column(db.Integer, primary_key=True)
    __ano_fundacao = db.Column('ano_fundacao', db.Date, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    abertura_total = db.Column(db.SmallInteger, nullable=True)

    direcao_id_direcao = db.Column(db.Integer, db.ForeignKey('direcao.id_direcao'), nullable=True)
    direcao = db.relationship('DirecaoModel', uselist=False, lazy='select')

    @property
    def ano_fundacao(self):
        return str(self.__ano_fundacao)

    @ano_fundacao.setter
    def ano_fundacao(self, data):
        if isinstance(data, str) and data.find("-")!=-1:
            data = datetime.strptime(data, "%Y-%m-%d")

        self.__ano_fundacao = data

    def serialize(self):
        
        try:
            docente_dict = self.direcao.docente.serialize()
        except AttributeError as msg:
            print("warning: nenhum docente na direção cadastrado neste campus.")
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
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_campus_instituto.label("id"), 
            campus_instituto_id_campus_instituto=campus_instituto
        )

    def __repr__(self):
        return '<campus %r>' % self.nome