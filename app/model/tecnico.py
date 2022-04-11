'''
    Módulo com a classe modelo da tabela `tecnico`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database import db
from .usuario import UsuarioModel
from .campus_instituto import CampusInstitutoModel
from .base_model import BaseHasUsuarioModel, BaseHasSiape
from datetime import datetime

class TecnicoModel(BaseHasUsuarioModel, BaseHasSiape, db.Model):
    '''
        Classe modelo que mapeia a tabela `discente` do banco de dados, responsável por pelos dados do discente.

        ...

        Atributos
        ---------
        `id_tecnico : int`
                Identificador do técnico.
        `siape : str`
                Número de siape do técnico.
        `nome : str`
                Nome do técnico.
        `cargo : str | None`
                O cargo do técnico.
        `carteirinha_vacinacao : MediumText | None`
                Carteirinha de vacinacao do técnico.
        `data_nascimento : Date(yyyy-mm-dd) | None`
                Data de nacimento do técnico.
        `sexo : str | None`
                Sexo do técnico. Pode ser 'M', 'F'..
        `quantidade_pessoas : int | None`
                Quantidade de psessoas que moram com o técnico.
        `quantidade_vacinas : int | None`
                Número de doses de vacina que o técnico recebeu. Pode ser 0, para nenhuma, 1, para uma dose, 2, para duas doses, 3, para três doses e 4 para mais.
        TODO:`grupo_risco : int | None`
                Se o técnico faz parte do grupo de risco ou não. Pose ser `0 para não` e `1 para sim`.
        `status_covid : int | None`
                Se o técnico está com covid ou não. Pode ser `0 para não` e `1 para sim`.
        `status_afastamento : int | None`
                Se o técnico está afastado do campus.
        `justificativa : str | None`
                Alguma justificativa que o discente queira informar.
        `fabricante : str | None`
                As fabricante es de cada uma das doses que o técnico recebeu.
        `usuario_id_usuario : int | None`
                Identificador do usuário do técnico.
        `usuario : UsuarioModel`
                Dados do usuário do técnico.
        `campus_instituto_id_campus_instituto : int | None`
                Campus ou instituto do técnico.
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto do técnico.
      
        Métodos
        -------
        `serialize(): dict`
                Retorna um dicionário com os dados da tabela para API expor como JSON.
        `get_vacinacao(siape_tecnico): dict`
            Obtem os dados relacionados a vacinação do técnico.
        `@classmethod`
        `query_all_names():`
                Consultar todos dos dados das colunas `nome`, `id_tecnico`, `siape` da tabela tecnico.
    '''

    __tablename__ = "tecnico"

    id_tecnico = db.Column(db.Integer, primary_key=True)
    siape = db.Column(db.String(45), unique=True, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    __data_nascimento = db.Column('data_nascimento', db.Date, nullable=True)
    cargo = db.Column(db.String(45), nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_afastamento = db.Column(db.SmallInteger, nullable=True)
    sexo = db.Column(db.String(2), nullable=True)
    quantidade_pessoas = db.Column(db.Integer, nullable=True)
    quantidade_vacinas = db.Column(db.Integer, nullable=True)
    fabricante = db.Column(db.String(45), nullable=True)
    justificativa = db.Column(db.Text, nullable=True)
    carteirinha_vacinacao = db.Column(db.Text(150000), nullable=True)
    
    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel',cascade="all, delete", lazy='select', uselist=False)

    campus_instituto_id_campus_instituto = db.Column(db.Integer, db.ForeignKey('campus_instituto.id_campus_instituto'), nullable=True)
    campus_instituto = db.relationship('CampusInstitutoModel', uselist=False, lazy='noload')

    @property
    def data_nascimento(self):
        return str(self.__data_nascimento)

    @data_nascimento.setter
    def data_nascimento(self, data):
        if isinstance(data, str) and data.find("-")!=-1:
             try:
                data = datetime.strptime(data, "%Y-%m-%d")
             except ValueError:
                raise ValueError("Erro: A data deve ser enviada no formato 'YYYY-mm-dd'")    
        self.__data_nascimento = data

    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `tecnico`.
        '''
        try:
            usuario_dict = self.usuario.serialize()
        
        except AttributeError as msg:
            print("Warning: Usuário não cadatrado para este trécnico")
            usuario_dict = None
        
        finally:
            campus_instituto = db.session.query(
                CampusInstitutoModel.nome
            ).filter_by(id_campus_instituto=self.campus_instituto_id_campus_instituto).first() # query name and get name from tuple
            
            return {
                "id_tecnico":self.id_tecnico,
                "siape":self.siape, 
                "nome":self.nome, 
                "data_nascimento":self.data_nascimento, 
                "cargo":self.cargo,
                "status_covid":self.status_covid, 
                "status_afastamento":self.status_afastamento,
                "sexo": self.sexo,
                "carteirinha_vacinacao":self.carteirinha_vacinacao,
                "quantidade_pessoas": self.quantidade_pessoas,
                "quantidade_vacinas": self.quantidade_vacinas,
                "fabricantes": self.fabricante,
                "justificativa": self.justificativa,
                "usuario_id_usuario":self.usuario_id_usuario,
                "usuario": usuario_dict if usuario_dict else None,
                "campus_id_campus":self.campus_instituto_id_campus_instituto,
                "campus": campus_instituto.nome if campus_instituto else None
            }

    @classmethod
    def get_vacinacao(cls, siape_tecnico):
        '''
            Obtem os dados relacionados a vacinação do téncico.

            ...

            Parâmetros
            ----------
            `siape_tecnico : str`
                    O número de siape do técnico que será usado na consulta dos dados de vacinação.
            
            Retorno
            -------
            Dicionário com os dados de vacinação do técnico.
        '''

        tecnico = cls.find_by_siape(
            cls.id_tecnico,
            cls.nome,
            cls.fabricante,
            cls.status_covid,
            cls.quantidade_vacinas,
            cls.justificativa,
            cls.carteirinha_vacinacao,
            siape=siape_tecnico
        )

        if tecnico:
            return {
                "id_tecnico":tecnico.id_tecnico,
                "nome":tecnico.nome,
                "fabricante":tecnico.fabricante,
                "status_covid":tecnico.status_covid,
                "quantidade_vacinas":tecnico.quantidade_vacinas,
                "justificativa": tecnico.justificativa,
                "carteirinha_vacinacao":tecnico.carteirinha_vacinacao
            }
        return None

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_tecnico.label("id"), 
            cls.siape.label("other_id")
        )
    
    def __repr__(self):
        return '<tecnico %r>' % self.nome
