'''
    Módulo com a classe modelo da tabela `reserva_recurso_servidores`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''

from marshmallow import fields, Schema

class ReservaRecursoServidoreserializer(Schema):
    '''
        Classe-modelo que srializa a tabela `reserva_recurso_servidores`, que por sua vez é responsável pela reserva de recurso dos servidores do campus universitário.

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
        
    '''

    

    id_reserva_recurso_servidores = fields.Int()
    data_inicio = fields.Date()
    data_fim = fields.Date()
    hora_inicio = fields.Time()
    hora_final = fields.Time()
    descricao = fields.Str()

    usuario_id_usuario = fields.Int()
    #TODO: usuario = fields.Nested(UsuarioSerializer)