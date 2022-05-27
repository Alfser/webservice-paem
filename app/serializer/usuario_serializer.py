'''
    Módulo com a classe modelo da tabela `usuario`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from marshmallow import fields, Schema


class UsuarioSerializer(Schema):
    '''
        Classe-modelo que serializa a tabela `usuario`, que por sua ves é responsável pelos dados de todos os usários.

        ...

        Atributos
        ---------
        `id_usuario : int`
                Identificador do usuário.
        `login : str`
                Login do usuário.
        `cpf : str | None`
                CPF do usuário.
        `senha : str`
                Senha do usuário.
        `email : str`
                Email do usuário.
        `tipo : int`
                Tipo de usuário: `0(admin)`; `1(técnico)`; `2(docente)`; `3(discente)` e `4(portaria)`
        `campus_instituto_id_campus_instituto : int`
                Identificador do campus ou instituto o qual o usuário pertence.
        `campus_instituto : CampusIntitutoModel`
                Dados do campus ou instituto do usuário.
        
    '''


    id_usuario = fields.Int()
    login = fields.Str()
    cpf = fields.Str()
    senha = fields.Str()
    email = fields.Email()
    tipo = fields.Int()

    campus_instituto_id_campus_instituto = fields.Int()