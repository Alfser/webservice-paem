'''
    Módulo com a classe modelo da tabela `recurso_campus`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from marshmallow import fields, Schema

class RecursoCampusSerializer(Schema):
    '''
        Classe-modelo que serializa a tabela `recurso_campus`, que por sua vez é responsável pelos dados dos recursos que são possíveis de usar no campus universitário.

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
        
    '''

    id_recurso_campus = fields.Int()
    nome = fields.Str()
    capacidade = fields.Int()
    tipo_restricao = fields.Int()
    descricao = fields.Str()
    inicio_horario_funcionamento = fields.Time()
    fim_horario_funcionamento = fields.Time()
    quantidade_horas = fields.Int()
    usuario_id_usuario = fields.Int()
    campus_instituto_id_campus_instituto = fields.Int()
    
    #TODO: usuario = fields.Nested(UsuarioSerializer)
    #TODO: campus_instituto = fields.Nested(CampusInstituto)