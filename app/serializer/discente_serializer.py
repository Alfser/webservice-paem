
'''
    Módulo com a classe modelo da tabela `discente`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from marshmallow import fields, Schema

class DiscenteSerializer(Schema):
    '''
        Classe modelo que serializa a tabela `discente` do banco de dados, responsável por pelos dados do discente.

        ...

        Atributos
        ---------
        `id_discente : int`
                Identificador do discente.
        `matricula : str`
                Número de matrícula do discente.
        `nome : str`
                Nome do discente.
        `entrada : str | None`
                Tipo de entrada do discente.
        `carteirinha_vacinacao : MediumText | None`
                Carteirinha de vacinacao do discente.
        `data_nascimento : Date(yyyy-mm-dd) | None`
                Data de nacimento do discente.
        `ano_de_ingresso : int | None`
                Ano de ingresso do discente.
        `sexo : str | None`
                Sexo do discente. Pode ser 'M', 'F'..
        `quantidade_pessoas : int | None`
                Quantidade de psessoas que moram com o discente.
        `quantidade_vacinas : int | None`
                Número de doses de vacina que o discente recebeu. Pode ser 0, para nenhuma, 1, para uma dose, 2, para duas doses, 3, para três doses e 4 para mais.
        `fabricante : str | None`
                As fabricantes de cada uma das doses que o discente recebeu.
        `justificativa : str | None`
                Alguma justificativa que o discente queira informar.
        `semestre : int | None`
                O semestre em que o discente está atualmente.
        `endereco : str | None`
                O enderesso atual do discente.
        `grupo_risco : int | None`
                Se o discente faz parte do grupo de risco ou não. Pose ser `0 para não` e `1 para sim`.
        `status_covid : int | None`
                Se o discente está com covid ou não. Pode ser `0 para não` e `1 para sim`.
        `status_permissao : int | None`
                Se o discente tem permissção ou não para entrar no campus.
        `usuario_id_usuario : int | None`
                Identificador do usuário do discente.
        `usuario : UsuarioModel`
                Dados do usuário do discente.
        `campus_instituto_id_campus_instituto : int | None`
                Campus ou instituto do discente.
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto do discente.
        `curso_id_curso : int | None`
                Identificador do curso do discente.
        `solicitacoes_acesso : list[SolicitacaoAcesso]`
            As solicitações de acesso realizadas pelo discente.
    '''


    id_discente = fields.Int()
    matricula = fields.Str()
    nome = fields.Str()
    entrada = fields.Str()
    carteirinha_vacinacao = fields.Str()
    data_nascimento = fields.Date()
    ano_de_ingresso = fields.Int()
    sexo = fields.Str()
    quantidade_pessoas = fields.Int()
    quantidade_vacinas = fields.Int()
    fabricante = fields.Str()
    justificativa = fields.Str()
    semestre = fields.Str()
    endereco = fields.Str()
    grupo_risco = fields.Int()
    status_covid = fields.Int()
    status_permissao = fields.Int()

    usuario_id_usuario = fields.Str()
    #TODO:usuario = fields.Nested(UsuarioSerializer)

    campus_instituto_id_campus_instituto = fields.Int()
    #TODO:campus_intituto = fields.Nested(CampusInstitutoSerializer)

    curso_id_curso = fields.Int()

    #TODO:solicitacoes_acesso = fields.Nested(SolicitacaoAcessoSerializer, many=True)
