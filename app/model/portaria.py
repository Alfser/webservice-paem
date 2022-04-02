'''
    Módulo com a classe modelo da tabela `portaria`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database import db
from .usuario import UsuarioModel
from .curso import CursoModel
from .base_model import BaseHasNameModel


class PortariaModel(BaseHasNameModel, db.Model):
    '''
        Classe-modelo que mapeia a tabela `portaria`, que por sua vez é responsável pelo cadastreo do usuário do porteiro.

        ...

        Atributos
        ---------
        `id_portaria : int`
                Identificador do cadatro portiro. 
        `nome : str`
                Nome do porteiro.
        `data_nascimento : Date(yyyy-mm-dd)` | None
        `funcao : str | None`
                Função do porteiro.
        `turno_trabalho : int`
                Turno de trabalho do porteiro.
        `usuario_id_usuario : int | None`
                Identificador do usuário do porteiro. 
        `usuario : UsuarioModel`
            Dados do usuário do porteiro.
        `curso_id_curso : int | None`
                Identificador do curso o qual a portaria pertence.
        `curso : CursoModel`
                Dados do curso.

        Métodos
        -------
        `serialize(): dict`
            Retorna um dicionário com os dados da tabela para API expor como JSON.
        
    '''
    __tablename__ = "portaria"

    id_portaria = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=True)
    funcao = db.Column(db.String(45), nullable=True)
    turno_trabalho = db.Column(db.SmallInteger, nullable=False)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel',cascade="all, delete", lazy='select')

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)
    curso = db.relationship('CursoModel', lazy="select")

    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `portaria`
        '''
        
        try:
            usuario_dict = self.usuario.serialize()
        except AttributeError as msg:
            print("Usuário não cadastrado.")
            usuario_dict = None

        finally:
            curso = db.session.query(
                CursoModel.nome
            ).filter_by(id_curso=self.curso_id_curso).first()
            
            return {
                "nome": self.nome,
                "data_nascimento": self.data_nascimento,
                "funcao": self.funcao,
                "turno_trabalho": self.turno_trabalho,
                "usuario_id_usuario": self.usuario_id_usuario,
                "usuario": usuario_dict if usuario_dict else None,
                "curso_id_curso": self.curso_id_curso,
                "curso": curso.nome if curso else None,
                "id_portaria": self.id_portaria
            }
    
    @classmethod
    def query_all_names(cls):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_portaria.label("id")
        )

    def __repr__(self):
        return '<portaria %r>' % self.nome
