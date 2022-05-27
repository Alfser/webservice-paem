'''
    Módulo com a classe modelo da tabela `portaria`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from marshmallow import fields, Schema

class PortariaSerializer(Schema):
    '''
        Classe-modelo que serializa a tabela `portaria`, que por sua vez é responsável pelo cadastreo do usuário do porteiro.

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
        `campus_instituto_id_campus_instituto : int | None`
                Campus ou instituto do porteiro.
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto do porteiro.
        
    '''


    id_portaria = fields.Int()
    nome = fields.Str()
    data_nascimento = fields.Date()
    funcao = fields.Str()
    turno_trabalho = fields.Int()

    usuario_id_usuario = fields.Int()
    #TODO: usuario = fields.Nested(UsuarioSerializer)

    campus_instituto_id_campus_instituto = fields.Int()
    #TODO: campus_instituto = fields.Nested(CampusInstitutoSerializer)