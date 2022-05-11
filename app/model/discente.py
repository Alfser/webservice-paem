
'''
    Módulo com a classe modelo da tabela `discente`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from .curso import CursoModel
from .usuario import UsuarioModel
from .campus_instituto import CampusInstitutoModel
from .base_model import BaseHasVacinacaoModel
from datetime import datetime
from ..database import db

class DiscenteModel(BaseHasVacinacaoModel, db.Model):
    '''
        Classe modelo que mapeia a tabela `discente` do banco de dados, responsável por pelos dados do discente.

        ...

        Atributos
        ---------
        `id_discente : int`
                Identificador do discente.
        `matricula : str`
                Número de matrícula do discente.
        `nome : str`
                Nome do discente.
        `entrada : str | None`
                Tipo de entrada do discente.
        `carteirinha_vacinacao : MediumText | None`
                Carteirinha de vacinacao do discente.
        `data_nascimento : Date(yyyy-mm-dd) | None`
                Data de nacimento do discente.
        `ano_de_ingresso : int | None`
                Ano de ingresso do discente.
        `sexo : str | None`
                Sexo do discente. Pode ser 'M', 'F'..
        `quantidade_pessoas : int | None`
                Quantidade de psessoas que moram com o discente.
        `quantidade_vacinas : int | None`
                Número de doses de vacina que o discente recebeu. Pode ser 0, para nenhuma, 1, para uma dose, 2, para duas doses, 3, para três doses e 4 para mais.
        `fabricante : str | None`
                As fabricantes de cada uma das doses que o discente recebeu.
        `justificativa : str | None`
                Alguma justificativa que o discente queira informar.
        `semestre : int | None`
                O semestre em que o discente está atualmente.
        `endereco : str | None`
                O enderesso atual do discente.
        `grupo_risco : int | None`
                Se o discente faz parte do grupo de risco ou não. Pose ser `0 para não` e `1 para sim`.
        `status_covid : int | None`
                Se o discente está com covid ou não. Pode ser `0 para não` e `1 para sim`.
        `status_permissao : int | None`
                Se o discente tem permissção ou não para entrar no campus.
        `usuario_id_usuario : int | None`
                Identificador do usuário do discente.
        `usuario : UsuarioModel`
                Dados do usuário do discente.
        `campus_instituto_id_campus_instituto : int | None`
                Campus ou instituto do discente.
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto do discente.
        `curso_id_curso : int | None`
                Identificador do curso do discente.
        `solicitacoes_acesso : list[SolicitacaoAcesso]`
            As solicitações de acesso realizadas pelo discente.

        Métodos
        -------
        `serialize(): dict`
                Retorna um dicionário com os dados da tabela para API expor como JSON.
        `@classmethod`
        `get_vacinacao(matricula_discente): dict`
            Obtem os dados relacionados a vacinação do discente.
        `serialize_to_list(): dict`
                Consultar os dados dos discentes somente das colunas `id_discente`,`nome` e `matrícula` para serem listados.
        `@classmethod`
        `query_all_names():`
                Consultar todos dos dados das colunas `nome`, `id_discente`, `matrícula`, `curso_id_curso` e `campus_istituto_id_campus_instituto` da tabela discente.
        `@classmethod`
        `contar_vacinados_por_curso(cls, id_campus_instituto):`
            Contar o número de vacinados por curso e número total de alunos.
    '''

    __tablename__='discente'

    id_discente = db.Column(db.Integer, primary_key=True)
    matricula = db.Column(db.String(45), unique=True, nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    entrada = db.Column(db.String(6), nullable=True)
    carteirinha_vacinacao = db.Column(db.Text(150000), nullable=True)
    __data_nascimento = db.Column('data_nascimento', db.Date, nullable=True)
    ano_de_ingresso = db.Column(db.Integer, nullable=True)
    sexo = db.Column(db.String(2), nullable=True)
    quantidade_pessoas = db.Column(db.Integer, nullable=True)
    quantidade_vacinas = db.Column(db.Integer, nullable=True)
    fabricante = db.Column(db.String(45), nullable=True)
    justificativa = db.Column(db.Text, nullable=True)
    semestre = db.Column(db.Integer, nullable=True)
    endereco = db.Column(db.String(255), nullable=True)
    grupo_risco = db.Column(db.SmallInteger, nullable=True)
    status_covid = db.Column(db.SmallInteger, nullable=True)
    status_permissao = db.Column(db.SmallInteger, nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', cascade="all, delete", uselist=False, lazy='select')

    campus_instituto_id_campus_instituto = db.Column(db.Integer, db.ForeignKey('campus_instituto.id_campus_instituto'), nullable=True)
    campus_intituto = db.relationship('CampusInstitutoModel', uselist=False, lazy='select')

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)

    solicitacoes_acesso = db.relationship('SolicitacaoAcessoModel', uselist=True, lazy='select')

    @classmethod
    def find_by_matricula(cls, matricula):
       return cls.query.filter_by(matricula=matricula).first()
    
    @classmethod
    def update_by_matricula(cls, matricula, dict):
       cls.query.filter_by(matricula=matricula).update(dict)
       cls.save()
    
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

    @classmethod
    def get_vacinacao(cls, matricula_discente):
        '''
            Obtem os dados relacionados a vacinação do discente.

            ...

            Parâmetros
            ----------
            `matricula_discente : str`
                    O número de matrícula do discente que será usado na consulta dos dados de vacinação.
            
            Retorno
            -------
            Dicionário com os dados de vacinação.
        '''
        discente = cls.find_by_matricula(matricula_discente)

        if discente:
            return {
                "id_discente":discente.id_discente,
                "nome":discente.nome,
                "carteirinha_vacinacao":discente.carteirinha_vacinacao,
                "fabricante":discente.fabricante,
                "status_covid":discente.status_covid,
                "quantidade_vacinas":discente.quantidade_vacinas,
                "justificativa": discente.justificativa
            }
        
        return None

    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `discente`.
        '''
        try:
            usuario_dict = self.usuario.serialize()
        except AttributeError as msg:
            print("usuário não cadastrado")
            usuario_dict = None
        
        finally:

            curso = db.session.query(
                CursoModel.nome
            ).filter_by(id_curso=self.curso_id_curso).first()
            
            campus_instituto = db.session.query(
                CampusInstitutoModel.nome
            ).filter_by(id_campus_instituto=self.campus_instituto_id_campus_instituto).first()

            return {
                "id_discente": self.id_discente, 
                "nome": self.nome,
                "matricula": self.matricula,
                "entrada": self.entrada,
                "data_nascimento": self.data_nascimento,
                "ano_de_ingresso": self.ano_de_ingresso,
                "sexo": self.sexo,
                "carteirinha_vacinacao":self.carteirinha_vacinacao,
                "quantidade_pessoas": self.quantidade_pessoas,
                "quantidade_vacinas": self.quantidade_vacinas,
                "fabricantes": self.fabricante,
                "justificativa": self.justificativa,
                "semestre": self.semestre,
                "endereco": self.endereco,
                "grupo_risco": self.grupo_risco,
                "status_covid": self.status_covid,
                "status_permissao": self.status_permissao,
                "usuario": usuario_dict if usuario_dict else None,
                "curso_id_curso": self.curso_id_curso,
                "curso": curso.nome if curso else None,
                "campus_instituto_id_campus_instituto": self.campus_instituto_id_campus_instituto,
                "campus_instituto": campus_instituto.nome if campus_instituto else None
            }

    def serialize_to_list(self):
        '''
            Consultar os dados dos discentes somente das colunas `id_discente`,`nome` e `matrícula` para serem listados. 

            ...

            Retorno
            -------
            Discionário com o resultado da consulta.
        '''

        discente_list = db.session.query(
            DiscenteModel.id_discente,
            DiscenteModel.nome,
            DiscenteModel.matricula
        ).filter_by().first()
        return {
            "id_discente":discente_list.id_discente,
            "nome":discente_list.nome,
            "matricula":discente_list.matricula
        }

    @classmethod
    def query_vacinacoes(cls, curso_id_curso, ano_turma, numero_de_doses):
        return super().query_vacinacoes(
            cls.nome.label("nome"), 
            cls.id_discente.label("id"),
            cls.matricula.label("matricula"),
            cls.ano_de_ingresso.label("turma"),
            cls.carteirinha_vacinacao.label("carteirinha_vacinacao"),
            curso_id_curso=curso_id_curso,
            ano_turma=ano_turma,
            numero_de_doses=numero_de_doses
        )

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_discente.label("id"),
            cls.matricula.label("matricula"),
            cls.curso_id_curso.label("curso_id_curso"),
            cls.campus_instituto_id_campus_instituto.label("campus_instituto_id_campus_instituto")
        )

    @classmethod
    def contar_vacinados_por_curso(cls, id_campus_instituto):
        '''
            Contar o número de vacinados por curso e número total de alunos.

            ...

            Parâmetros
            -----------
            `id_campus_instituto : int`
                    Identificador do campus ou instituto dos discente usado para filtragem na consulta ao banco..
        '''
        query_vacinados = db.engine.execute(
            "SELECT curso.nome, COUNT(quantidade_vacinas) quantidade_vacinados"
            " FROM discente, curso"
            " WHERE curso_id_curso=id_curso"
            " AND discente.campus_instituto_id_campus_instituto=%s"
            " AND quantidade_vacinas>0"
            " GROUP BY id_curso;",
            id_campus_instituto
        )
        dict_query_vacinados = dict()
        for row in query_vacinados:
            dict_query_vacinados[row[0]]=row[1]
        

        query_alunos = db.engine.execute(
            "SELECT curso.nome, COUNT(id_discente) quantidade_discente"
            " FROM discente, curso"
            " WHERE curso_id_curso=id_curso"
            " AND discente.campus_instituto_id_campus_instituto=%s"
            " GROUP BY id_curso;",
            id_campus_instituto
        )

        dict_query_alunos = dict()
        for row in query_alunos:
            dict_query_alunos[row[0]]=row[1]

        return{"total_vacinados":dict_query_vacinados, "total_alunos":dict_query_alunos}
        
    def __repr__(self):
        return '<discente %r>' % self.login