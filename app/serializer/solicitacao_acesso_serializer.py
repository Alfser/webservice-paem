'''
    Módulo com a classe modelo da tabela `solicitacao_acesso`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from marshmallow import fields, Schema

class SolicitacaoAcessoSerializer(Schema):
    '''
        Classe-modelo que serializa a tabela `solicitacao_acesso`, que por sua vez é responsável pelo registro das solicitacões de acessos realizadas pelos usuários.

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

    '''

          
    id_solicitacao_acesso = fields.Int()
    para_si = fields.Int()
    data = fields.Int()
    hora_inicio = fields.Time()
    hora_fim = fields.Time()
    status_acesso = fields.Int()
    nome = fields.Str()
    fone = fields.Str()
    cpf = fields.Str()
    visitante = fields.Bool()
    observacao = fields.Str()

    usuario_id_usuario = fields.Int()
    #TODO: usuario = fields.Nested(UsuarioSerializer)
    
    discente_id_discente = fields.Int()
    recurso_campus_id_recurso_campus = fields.Int()
    disciplina_id_disciplina = fields.Int()
    #TODO: disciplina = fields.Nested(DisciplinaSerializer)

    #TODO: recurso_campus = fields.Nested(RecursoCampusSerializer)
    
    campus_instituto_id_campus_instituto = fields.Int()
    #TODO: campus_instituto = fields.Nested(CampusInstitutoSerializer)

    #TODO: acesso_permitido = fields.Nested(AcessoPermitidoSerializer)