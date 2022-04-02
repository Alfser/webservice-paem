'''
    Módulo com a classe modelo da tabela `usuario`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database import db
from .base_model import BaseHasNameModel

from passlib.apps import custom_app_context as pwd_context


class UsuarioModel(BaseHasNameModel, db.Model):
    '''
        Classe-modelo que mapeia a tabela `usuario`, que por sua ves é responsável pelos dados de todos os usários.

        ...

        Atributos
        ---------
        `id_usuario : int`
                Identificador do usuário.
        `login : str`
                Login do usuário.
        `cpf : str | None`
                CPF do usuário.
        `senha : str`
                Senha do usuário.
        `email : str`
                Email do usuário.
        `tipo : int`
                Tipo de usuário: `0(admin)`; `1(técnico)`; `2(docente)`; `3(discente)` e `4(portaria)`
        `campus_instituto_id_campus_instituto : int`
                Identificador do campus ou instituto o qual o usuário pertence.
        `campus_instituto : CampusIntitutoModel`
                Dados do campus ou instituto do usuário.
        
        Métodos
        -------
        `verify_password(): boolean`
                Verificar se a senha corresponde à que está na base de dados.
        `serialize(): dict`
                Retorna um dicionário com os dados da tabela para API expor como JSON.
        `@classmethod`
        `find_by_login(login): UsuarioModel`
                Buscar um usuário pelo `login`.
        `@classmethod`
        `find_by_cpf(cpf): UsuarioModel`
                Buscar um usuário pelo `cpf`.
        `@classmethod`
        `find_by_email(email): UsuarioModel`
            Buscar um usuário pelo `email`.
    '''

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
        ''' 
            Verificar se a senha corresponde à que está na base de dados.

            ...

            Parâmetros
            ----------
            `password : str`
                    senha de entrada do usuário.
            
            Retorno
            -------
            Retorna um Booleano: `True` se a senha corresponder e `False` caso contrario.
        '''
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
        '''
            Buscar um usuário pelo `login`.

            ...

            Parâmetros
            ----------
            `login : str`
                    Login do usuário usado para a busca no banco de dados.
            
            Retorno
            -------
            Retorna os dado do usuário no objeto `UsuarioModel`.
        '''
        return cls.query.filter_by(login=login).first()

    @classmethod
    def find_by_cpf(cls, cpf):
        '''
            Buscar um usuário pelo `cpf`.

            ...

            Parâmetros
            ----------
            `cpf : str`
                    CPF do usuário usado para a busca no banco de dados.
            
            Retorno
            -------
            Retorna os dado do usuário no objeto `UsuarioModel`.
        '''
        return cls.query.filter_by(cpf=cpf).first()
    
    @classmethod
    def find_by_email(cls, email):
        '''
            Buscar um usuário pelo `email`.

            ...

            Parâmetros
            ----------
            `email : str`
                    Email do usuário usado para a busca no banco de dados.
            
            Retorno
            -------
            Retorna os dado do usuário no objeto `UsuarioModel`.
        '''
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