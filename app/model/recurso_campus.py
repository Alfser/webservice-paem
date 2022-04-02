'''
    Módulo com a classe modelo da tabela `recurso_campus`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from ..database import db
from .campus_instituto import BaseHasNameModel, CampusInstitutoModel
from .usuario import UsuarioModel
from datetime import time


class RecursoCampusModel(BaseHasNameModel, db.Model):
    '''
        Classe-modelo que mapeia a tabela `recurso_campus`, que por sua vez é responsável pelos dados dos recursos que são possíveis de usar no campus universitário.

        ...

        `id_recurso_campus : int`
                Identificador do recurso do campus.
        `nome : string`
                Nome do recurso do campus.
        `capacidade : int`
                quantidade de pessoas que o recurso tem capacidade de recerber.
        `tipo_restricao : int`
                Tipo de restrição que o recurso tem: `0(livre)`, pode entrar qualquer aluno mesmo sem solicitar o acesso; `1(parcial)`, pode entrar qualquer aluno desde que tenha tomado uma dose da vacina; `3(total)`, pode entrar somente quem solicitar um cesso e tiver as doses necessárias da vacina contra a Covid-19.
        `descricao : string | None`
                Descrição do recurso do campus.
        `inicio_horario_funcionamento : Time(hh:mm:ss)`
                Horário do início de funcionamento do local que o recurso pertence.
        `fim_horario_funcionamento : Time(hh:mm:ss)`
                Horário do fim de funcionamento do local que o recurso pertence.
        `quantidade_horas : int`
                Quantidade de horas que uma pessoal pode ficar ocupando um recurso do campus.
        `usuario_id_usuario : int | None`
                Identificador do usuário que criou o recurso.
        `usuario : UsuarioModel`
                Dados do usuário que solicitou o recurso.
        `campus_instituto_id_campus_instituto`
                Identificador do campus o qual o recurso pertence.
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto o qual o recurso pertence.
        
        Métodos
        -------
        `serialize():dict`
            Retorna um dicionário com os dados da tabela para API expor como JSON.    
    '''

    __tablename__ = "recurso_campus"

    id_recurso_campus = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    tipo_restricao = db.Column(db.SmallInteger, nullable=False)#(0=livre, 1=restricão parcial; 2=restricão total)
    descricao = db.Column(db.Text, nullable=True)
    __inicio_horario_funcionamento = db.Column('inicio_horario_funcionamento', db.Time, nullable=False)
    __fim_horario_funcionamento = db.Column('fim_horario_funcionamento', db.Time, nullable=False)
    quantidade_horas = db.Column(db.Integer, nullable=False)
    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    campus_instituto_id_campus_instituto = db.Column(db.Integer, db.ForeignKey('campus_instituto.id_campus_instituto'), nullable=True)
    
    usuario = db.relationship('UsuarioModel', lazy='select', uselist=False)
    campus_instituto = db.relationship('CampusInstitutoModel', backref=db.backref('recursos_campus', lazy='select'))

            
    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `recurso_campus`.
        '''
        campus_instituto = db.session.query(
            CampusInstitutoModel.nome
        ).filter_by(
            id_campus_instituto=self.campus_instituto_id_campus_instituto
            ).first() # query name of campus
        
        return {
            "id_recuso_campus": self.id_recurso_campus, 
            "nome": self.nome,
            "capacidade": self.capacidade,
            "tipo_restricao":self.tipo_restricao,
            "usuario_id_usuario":self.usuario_id_usuario,
            'descricao':self.descricao,
            'inicio_horario_funcionamento':self.inicio_horario_funcionamento,
            'fim_horario_funcionamento':self.fim_horario_funcionamento,
            'quantidade_horas': self.quantidade_horas,
            'campus_instituto_id_campus_instituto':self.campus_instituto_id_campus_instituto,
            'campus_instituto': campus_instituto.nome if campus_instituto else None
        }
    
    @property                    
    def inicio_horario_funcionamento(self):
        return str(self.__inicio_horario_funcionamento)
    
    @inicio_horario_funcionamento.setter
    def inicio_horario_funcionamento(self, inicio_horario_funcionamento):
        if isinstance(inicio_horario_funcionamento, str) and inicio_horario_funcionamento.find(":")!=-1:
            hour_inicio, minute_inicio, second_inicio = inicio_horario_funcionamento.split(':')
            self.__inicio_horario_funcionamento = time(
                hour=int(hour_inicio), 
                minute=int(minute_inicio), 
                second=int(second_inicio)
            )

        self.__inicio_horario_funcionamento = inicio_horario_funcionamento

    @property
    def fim_horario_funcionamento(self):
        return str(self.__fim_horario_funcionamento)

    @fim_horario_funcionamento.setter
    def fim_horario_funcionamento(self, fim_horario_funcionamento):        
        if isinstance(fim_horario_funcionamento, str) and fim_horario_funcionamento.find(":")!=-1:
            hour_fim, minute_fim, sec_fim = fim_horario_funcionamento.split(':')
            self.__fim_horario_funcionamento = time(
                hour=int(hour_fim),
                minute=int(minute_fim),
                second=int(sec_fim)
            )

        self.__fim_horario_funcionamento = fim_horario_funcionamento
    
    @classmethod
    def query_all_names(cls, campus_instituto_id_campus_instituto, usuario_id_usuario):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_recurso_campus.label("id"),
            cls.usuario_id_usuario.label("usuario_id_usuario"),
            cls.__inicio_horario_funcionamento.label("inicio_horario"),
            cls.__fim_horario_funcionamento.label("fim_horario"), 
            campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto,
            usuario_id_usuario=usuario_id_usuario
        )

    def __repr__(self):
        return '<recurso_campus %r>' % self.nome