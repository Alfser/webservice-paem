'''
    Módulo com a classe modelo da tabela `usuario`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database import db
from .base_model import BaseHasNameModel

from passlib.apps import custom_app_context as pwd_context


class UsuarioModel(BaseHasNameModel, db.Model):
    __tablename__='usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), unique=True, nullable=False)
    cpf = db.Column(db.String(15), unique=True, nullable=True)
    _senha = db.Column('_senha', db.Text, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    tipo = db.Column(db.Integer, nullable=False)

    campus_instituto_id_campus_instituto = db.Column(
        db.Integer, 
        db.ForeignKey('campus_instituto.id_campus_instituto'),
        nullable=True
    )
    campus_instituto = db.relationship('CampusInstitutoModel', uselist=False, lazy='noload')

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, password):
        self._senha = pwd_context.hash(password)
    
    def verify_password(self, password):
        ''' Verify password hashed '''
        return pwd_context.verify(password, self.senha)

    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `usuario`.
        '''
        
        return {"id_usuario": self.id_usuario, 
                "login": self.login,
                "cpf": self.cpf,
                "email":self.email,
                "tipo":self.tipo,
                "campus_instituto_id_campus_instituto":self.campus_instituto_id_campus_instituto
                
        }

    @classmethod
    def find_by_login(cls, login):
       return cls.query.filter_by(login=login).first()

    @classmethod
    def find_by_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf).first()
    
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(
            cls.login.label("nome"),
            cls.id_usuario.label("id"),
            cls.cpf.label("cpf")
        )

    def __repr__(self):
        return '<usuario %r>' % self.login