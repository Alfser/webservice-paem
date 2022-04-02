'''
    Módulo com a classe modelo da tabela `reserva_recurso_servidores`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from sqlalchemy.orm import backref
from ..database import db
from .usuario import UsuarioModel


class ReservaRecursoServidoresModel(db.Model):
    '''
        Classe-modelo que mapeia a tabela `reserva_recurso_servidores`, que por sua vez é responsável pela reserva de recurso dos servidores do campus universitário.

        ...

        Atributos
        ---------
        `id_reserva_recurso_servidores : int`
                Identificador da reserva.
        `data_inicio : Date(yyyy-mm-dd)`
                Data inicial da reserva.
        `data_fim : Date(yyyy-mm-dd)`
                Data final da reserva.
        `hora_inicio : Time(hh:mm:ss)`
                Horário inicial da reserva.
        `hora_final : Time(hh:mm:ss)`
                Horário final da reserva.
        `descricao : string | None`
                Descrição da reserva.
        `usuario_id_usuario : int | None`
                Dados do usuário que criou a reserva.
        `usuario : UsuarioModel`
                Dados do usuário que criou a reserva.
        
        Métodos
        -------
        `serialize() : dict`
            Retorna um dicionário com os dados da tabela para API expor como JSON.
    '''

    __tablename__= "reserva_recurso_servidores"

    id_reserva_recurso_servidores = db.Column(db.Integer, primary_key=True)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_final = db.Column(db.Time, nullable=False)
    descricao = db.Column(db.SmallInteger, nullable=True)

    usuario_id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=True)
    usuario = db.relationship('UsuarioModel', uselist=False, lazy='select', backref=db.backref('reserva_recurso_servidores', lazy='select'))

    # TODO: Add recursos aos servidores(docentes, tecnicos..)
    
    def serialize(self):
        '''
            Retorna um dicionário com os dados da tabela para API expor como JSON.

            ...

            Retorno
            -------
            Dicionário `dict` com os dados da tabela `reserva_recurso_servidores`.
        '''
        
        return {
            "id_reserva_recurso_servidores":self.id_reserva_recurso_servidores,
            "data_inicio":self.data_inicio,
            "data_fim":self.data_fim,
            "hora_inicio":self.hora_inicio,
            "hora_final":self.hora_final,
            "descricao":self.descricao,
            "usuario_id_usuario":self.usuario_id_usuario,
            "usuario":self.usuarios
        }
    def __repr__(self):
        return '<reserva_recurso_campus %r>' % self.nome