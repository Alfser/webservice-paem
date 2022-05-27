'''
    Módulo com a classe modelo da tabela `ponto_verificacao`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''

from marshmallow import fields, Schema
class PontoVerificacaoSerializer(Schema):
    '''
        Classe-modelo que serializa a tabela `ponto_verificacão`, que descreve outro ponto de verificação de entrada dentro do campus.

        ...

        Atributos
        ---------
        `id_ponto_verificacao : int`
                Identificador do ponto de acesso.
        `nome : str`
                Nome do responsável pelo ponto de acesso.
        `descricao : string | None`
                Descrição do ponto de acesso.
        `usuario_id_usuario : int | None`
                Identificador do usuário responsável pelo ponto de acesso.
        `usuario : UsuarioModel`
                Dados do usuário do ponto de acesso.
        `campus_instituto_id_campus_instituto: int`
                Identificador do campus do ponto de acesso.
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto do ponto de acesso.

    '''


    id_ponto_verificacao = fields.Int()
    nome = fields.Str()
    descricao = fields.Str()
    usuario_id_usuario = fields.Int()
    #TODO: usuario = fields.Nested(UsuarioSerializer)

    campus_instituto_id_campus_instituto = fields.Int()
    #TODO: campus_instituto = fields.Nested(CampusInstituto)