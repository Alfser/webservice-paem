'''
    Módulo com a classe modelo da tabela `solicitacao_acesso`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database import db
from .base_model import BaseHasUsuarioAndDiscenteModel
from .usuario import UsuarioModel
from .disciplina import DisciplinaModel
from .acesso_permitido import AcessoPermitidoModel
from .discente import DiscenteModel
from .recurso_campus import RecursoCampusModel
from .campus_instituto import CampusInstitutoModel

from datetime import time, datetime

class SolicitacaoAcessoModel(BaseHasUsuarioAndDiscenteModel, db.Model):
    '''
        Classe-modelo que mapeia a tabela `solicitacao_acesso`, que por sua vez é responsável pelo registro das solicitacões de acessos realizadas pelos usuários.

        ...

        Atributos
        ---------
        `id_solicitacao_acesso : int`    
                Identificador da solicitação de acessso.
        `para_si : int`
                Se o acesso é para si mesmo ou outro.
        `data : Date(yyyy-mm-dd)`
                Data da solicitação de acesso ao campus.
        `hora_inicio : Time(hh:mm:ss)`
                Horário inicial requisitado para acessar o local solicitado.
        `hora_fim : Time(hh:mm:ss)`
                Horário final do acesso ao local solicitado.
        `status_acesso : int | None`
                Se o acesso ao recurso foi permitido ou não: `0 para não` e `1 para sim`. 
        `nome : str`
                Nome da pessoa que solicitou o acesso.
        `fone : str`
                Telefone da pessoa que solicitou o acesso.
        `cpf : str | None`
                CPF da pessoa que solicitou o acesso.
        `visitante : str | None`
                Se a pessoa é visitante ou não: `0 para não ` e `1 para sim`.
        `observacao : str | None`
                Adicionar alguma observação sobre a solicitação.
        `usuario_id_usuario : int | None`
                Identificador do usuário que realizou a solicicitação.
        `usuario : UsuarioModel`
                Dados do usuário que solicitou o acesso ao recursodo campus.
        `discente_id_discente : int | None`
                Identificador do discente o qual o solicitação pertense.
        `recurso_campus_id_recurso_campus : int | None`
                Identificador do recurso do campus para o qual o solicitação foi realizada.
        `recurso_campus : RecursoCampusModel`
                Dados do campus para o qual o solicitação foi realizada.
        `disciplina_id_disciplina : int | None`
                Se o acesso foi solicitado para o recurso que pertense a uma disciplina, deverá ser adicionado o id dela, caso não, deixar nullo.
        `disciplina : DisciplinaModel`
                Disciplina para o qual a solicitação foi realizada.
        `campus_instituto_id_campus_instituto : int | None`
                Identificador do campus ou instituto no qual o solicitação foi realizada.
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto no qual o solicitação foi realizada.
        `acesso_permitido : AcessoPermitidoModel`
                Dados do acesso permitido para essa solicitação, casoo não foi, será nullo.

        Métodos
        -------
        `serialize(self): dict`
            Retorna um dicionário com os dados da tabela para API expor como JSON.    
        `@classmethod`
        `find_by_id_discente(): dict`
            Buscar uma solicitação pelo id do discente.
        `@classmethod`
        `contar_agendamento_por_campus() : dict`
            Contar a quantidade de agendamentos por campus.
        `@classmethod`
        `contar_agendamento_por_recurso_campus() : dict`
            Contar a quantidade de agendamentos por recurso do campus.
        `@classmethod`
        `contar_agendamento_por_curso(cls, ano, mes, id_campus_instituto) : dict`
            Contar a quantidade de agendamentos por curso.
    '''
    __tablename__= "solicitacao_acesso"
          
    id_solicitacao_acesso = db.Column(db.Integer, primary_key=True)
    para_si = db.Column(db.SmallInteger, nullable=False) #0-não e 1-sim
    __data = db.Column('data', db.Date, nullable=False)
    __hora_inicio = db.Column('hora_inicio', db.Time, nullable=False)
    __hora_fim = db.Column('hora_fim', db.Time, nullable=False)
    status_acesso = db.Column(db.SmallInteger, nullable=True)
    nome = db.Column(db.String(45), nullable=False)
    fone = db.Column(db.String(45), nullable=True)
    cpf = db.Column(db.String(45), nullable=True)
    visitante = db.Column(db.SmallInteger, nullable=True)
    observacao = db.Column(db.Text, nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, lazy='noload')
    
    discente_id_discente = db.Column(
        db.Integer, 
        db.ForeignKey('discente.id_discente'), 
        nullable=True
    )

    recurso_campus_id_recurso_campus = db.Column(
        db.Integer, 
        db.ForeignKey('recurso_campus.id_recurso_campus'), 
        nullable=True
    )

    disciplina_id_disciplina = db.Column(db.Integer, db.ForeignKey('disciplina.id_disciplina'), nullable=True)
    disciplina = db.relationship('DisciplinaModel', uselist=False, lazy='select', backref=db.backref('solicitacoes_acessos', lazy='select'))

    recurso_campus = db.relationship('RecursoCampusModel', uselist=False, lazy='select')
    
    campus_instituto_id_campus_instituto = db.Column(
        db.Integer, 
        db.ForeignKey('campus_instituto.id_campus_instituto'),
        nullable=True
    )
    campus_instituto = db.relationship('CampusInstitutoModel', uselist=False, lazy='noload')

    acesso_permitido = db.relationship('AcessoPermitidoModel', cascade="all, delete", uselist=False, lazy='select')


    @property
    def data(self):
        return str(self.__data)

    @data.setter
    def data(self, data):
        if isinstance(data, str) and data.find("-")!=-1:
            try:
                data = datetime.strptime(data, "%Y-%m-%d")
            except ValueError:
                raise ValueError("A data deve ser enviada no formato 'YYYY-mm-dd'")    
        self.__data = data

    @property
    def hora_inicio(self):
        return str(self.__hora_inicio)

    @hora_inicio.setter
    def hora_inicio(self, hora_inicio):
        if isinstance(hora_inicio, str) and hora_inicio.find(":")!=-1:
            hour_inic, minute_inic, second_inic = hora_inicio.split(':')
            hora_inicio = time(hour=int(hour_inic), minute=int(minute_inic), second=int(second_inic))
    
        self.__hora_inicio = hora_inicio

    @property
    def hora_fim(self):
        return str(self.__hora_fim)

    @hora_fim.setter
    def hora_fim(self, hora_fim):
        if isinstance(hora_fim, str) and hora_fim.find(":")!=-1:
            hour_inic, minute_inic, second_inic = hora_fim.split(':')
            hora_fim = time(hour=int(hour_inic), minute=int(minute_inic), second=int(second_inic))
        
        self.__hora_fim = hora_fim

    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `solicitacao_acesso`.
        '''
        
        try:
            acesso_permitido_dict = self.acesso_permitido.serialize()
        except AttributeError as msg:
            acesso_permitido_dict = None        

        finally:
        # Query just some rows
            discente = db.session.query(
                DiscenteModel.matricula, 
                DiscenteModel.nome
            ).filter_by(id_discente=self.discente_id_discente).first()
        
            recurso_campus = db.session.query(
                RecursoCampusModel.nome,
                RecursoCampusModel.tipo_restricao
            ).filter_by(id_recurso_campus=self.recurso_campus_id_recurso_campus).first()
        
        return {
            "id":self.id_solicitacao_acesso,
            "para_si":self.para_si,
            "data":self.data,
            "hora_inicio":self.hora_inicio,
            "hora_fim":self.hora_fim,
            "status_acesso":self.status_acesso,
            "nome":self.nome,
            "fone":self.fone,
            "matricula": discente.matricula if discente else None,
            "campus_instituto_id_campus_instituto":self.campus_instituto_id_campus_instituto,
            "usuario_id_usuario": self.usuario_id_usuario,
            "discente_id_discente":self.discente_id_discente,
            "discente": discente.nome if discente else None,
            "recurso_campus_id_recurso_campus":self.recurso_campus_id_recurso_campus,
            "recurso_campus": recurso_campus.nome if recurso_campus else None,
            "tipo_restricao": recurso_campus.tipo_restricao if recurso_campus else None,
            "acesso_permitido": acesso_permitido_dict if acesso_permitido_dict else None
        }

    @classmethod
    def find_by_id_discente(cls, id_discente):
        '''
            Buscar uma solicitação pelo id do discente.

            ...

            Parâmetros
            ----------
            `id_discente : int`
                    Identificador do discente usado para realizar a busca.
            Retorno
            -------
            Um dicionário com os dados do discente pronto para expor como JSON.
        '''
        solicitacao_acesso = cls.query.filter_by(discente_id_discente=id_discente).first()
        return solicitacao_acesso.serialize()

    @classmethod
    def contar_agendamento_por_campus(cls):
        '''
            Contar a quantidade de agendamentos por campus.

            ...

            Retorno
            -------
            Um dicionário a a quantidade de agendamento por campus pronto para expor como JSON.
        '''

        query = db.engine.execute("SELECT campus_instituto.nome, count(id_solicitacao_acesso) as count_by_curso"
                                    " FROM solicitacao_acesso, campus_instituto"
                                    " WHERE campus_instituto_id_campus_instituto=id_campus_instituto"
                                    " AND data BETWEEN DATE_SUB(CURDATE(), INTERVAL 6 MONTH) AND CURDATE()"
                                    " GROUP BY id_campus_instituto;"
                                    )
        dict_query = dict()
        for row in query:
            dict_query[row[0]]=row[1]
        return dict_query

    @classmethod
    def contar_agendamento_por_recurso_campus(cls, ano, mes, id_campus_instituto):
        '''
            Contar a quantidade de agendamentos por recurso do campus.

            ...

            Parâmetros
            ----------
            `ano : int`
                    Ano dos agendamentos.
            `mes : int`
                    Mês dos agendamentos.
            `id_campus_instituto: int`
                    Identificador do campus onde os agendamentos foram solicitados.

            Retorno
            -------
            Um dicionário a a quantidade de agendamento por recurso do campus pronto para expor como JSON.
        '''
        query = db.engine.execute("SELECT recurso_campus.nome, count(id_solicitacao_acesso) count_by_curso"
                                    " FROM solicitacao_acesso, recurso_campus"
                                    " WHERE recurso_campus_id_recurso_campus=id_recurso_campus"
                                    " AND solicitacao_acesso.campus_instituto_id_campus_instituto = %s"
                                    " AND YEAR(data) = %s AND MONTH(data) = %s"
                                    " GROUP BY id_recurso_campus;",
                                    id_campus_instituto, ano, mes
                                )
        dict_query = dict()
        for row in query:
            dict_query[row[0]]=row[1]
        return dict_query

    @classmethod
    def contar_agendamento_por_curso(cls, ano, mes, id_campus_instituto):
        '''
            Contar a quantidade de agendamentos por curso.

            ...

            Parâmetros
            ----------
            `ano : int`
                    Ano dos agendamentos.
            `mes : int`
                    Mês dos agendamentos.
            `id_campus_instituto: int`
                    Identificador do campus onde os agendamentos foram solicitados.

            Retorno
            -------
            Um dicionário a a quantidade de agendamento por curso do campus pronto para expor como JSON.
        '''

        query = db.engine.execute("SELECT curso.nome, count(id_solicitacao_acesso) as count_by_curso"
                                    " FROM solicitacao_acesso, discente, curso"
                                    " WHERE discente_id_discente=id_discente"
                                    " AND curso_id_curso=id_curso"
                                    " AND solicitacao_acesso.campus_instituto_id_campus_instituto = %s"
                                    " AND YEAR(data) = %s AND MONTH(data) = %s"
                                    " GROUP BY id_curso;",
                                    id_campus_instituto, ano, mes
                                )
        dict_query = dict()
        for row in query:
            dict_query[row[0]]=row[1]
        return dict_query

    def __repr__(self):
        return '<solicita_acesso %r>' % self.id_solicitacao_acesso
