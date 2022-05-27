'''
    Módulo com a classe modelo da tabela `docente`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''

from marshmallow import fields, Schema


class DocenteModel(Schema):
    '''
        Classe modelo que serializa a tabela `discente` do banco de dados, responsável por pelos dados do discente.

        ...

        Atributos
        ---------
        `id_docente : int`
                Identificador do docente.
        `siape : str`
                Número de siape do docente.
        `nome : str`
                Nome do docente.
        `carteirinha_vacinacao : MediumText | None`
                Carteirinha de vacinacao do docente.
        `data_nascimento : Date(yyyy-mm-dd) | None`
                Data de nacimento do docente.
        `sexo : str | None`
                Sexo do docente. Pode ser 'M', 'F'..
        `quantidade_pessoas : int | None`
                Quantidade de psessoas que moram com o docente.
        `quantidade_vacinas : int | None`
                Número de doses de vacina que o docente recebeu. Pode ser 0, para nenhuma, 1, para uma dose, 2, para duas doses, 3, para três doses e 4 para mais.
        `situacao : str | None`
                Como está situação atual do docente.
        `escolaridade : str | None`
                O nível de escolaridade do docente.
        TODO:`grupo_risco : int | None`
                Se o docente faz parte do grupo de risco ou não. Pose ser `0 para não` e `1 para sim`.
        `status_covid : int | None`
                Se o docente está com covid ou não. Pode ser `0 para não` e `1 para sim`.
        `status_afastamento : int | None`
                Se o docente está afastado do campus.
        `justificativa : str | None`
                Alguma justificativa que o discente queira informar.
        `fabricante : str | None`
                As fabricant es de cada uma das doses que o docente recebeu.
        `usuario_id_usuario : int | None`
                Identificador do usuário do docente.
        `usuario : UsuarioModel`
                Dados do usuário do docente.
        `campus_instituto_id_campus_instituto : int | None`
                Campus ou instituto do docente.
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto do docente.
        `curso_id_curso : int | None`
                Identificador do curso do docente.
      
    '''


    id_docente = fields.Int()
    siape = fields.Str()
    nome = fields.Str()
    data_nascimento = fields.Date()
    status_covid = fields.Int()
    status_afastamento = fields.Int()
    escolaridade = fields.Str()
    situacao = fields.Str()
    sexo = fields.Str()
    quantidade_pessoas = fields.Int()
    quantidade_vacinas = fields.Int()
    fabricante = fields.Str()
    justificativa = fields.Str()
    carteirinha_vacinacao = fields.Str()

    