'''
    Módulo com a classe modelo da tabela `protocolo`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from marshmallow import fields, Schema

class ProtocoloSerializer(Schema):
    '''
        Classe-modelo que serializa a tabela `protocolo`, que, por sua vez é responsável pelo registro das conversão de usuário com o `chatbot`.

        ...

        Atributos
        ---------
        `id_protocolo : int`
                Identificador do protocolo.
        `mensagens : string | None`
                As mensagens enviadas ao chatbot.
        `usuario_id_usuario : int | None`
                O identificador do usuário que enviou as menságens ao chatboot.
        `usuario : UsuarioModel`
                Dados do usuário que enviou as menságens ao chatboot.
    '''


    id_protocolo = fields.Int()
    mensagens = fields.Str()
    usuario_id_usuario = fields.Int()
    #TODO: usuario = fields.Nested(UsuarioSerializer)