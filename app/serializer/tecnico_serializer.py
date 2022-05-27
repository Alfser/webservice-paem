'''
    Módulo com a classe modelo da tabela `tecnico`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from marshmallow import fields, Schema

class TecnicoSerializer(Schema):
    '''
        Classe modelo que serializa a tabela `discente` do banco de dados, responsável por pelos dados do discente.

        ...

        Atributos
        ---------
        `id_tecnico : int`
                Identificador do técnico.
        `siape : str`
                Número de siape do técnico.
        `nome : str`
                Nome do técnico.
        `cargo : str | None`
                O cargo do técnico.
        `carteirinha_vacinacao : MediumText | None`
                Carteirinha de vacinacao do técnico.
        `data_nascimento : Date(yyyy-mm-dd) | None`
                Data de nacimento do técnico.
        `sexo : str | None`
                Sexo do técnico. Pode ser 'M', 'F'..
        `quantidade_pessoas : int | None`
                Quantidade de psessoas que moram com o técnico.
        `quantidade_vacinas : int | None`
                Número de doses de vacina que o técnico recebeu. Pode ser 0, para nenhuma, 1, para uma dose, 2, para duas doses, 3, para três doses e 4 para mais.
        TODO:`grupo_risco : int | None`
                Se o técnico faz parte do grupo de risco ou não. Pose ser `0 para não` e `1 para sim`.
        `status_covid : int | None`
                Se o técnico está com covid ou não. Pode ser `0 para não` e `1 para sim`.
        `status_afastamento : int | None`
                Se o técnico está afastado do campus.
        `justificativa : str | None`
                Alguma justificativa que o discente queira informar.
        `fabricante : str | None`
                As fabricante es de cada uma das doses que o técnico recebeu.
        `usuario_id_usuario : int | None`
                Identificador do usuário do técnico.
        `usuario : UsuarioModel`
                Dados do usuário do técnico.
        `campus_instituto_id_campus_instituto : int | None`
                Campus ou instituto do técnico.
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto do técnico.

    '''


    id_tecnico = fields.Int()
    siape = fields.Str()
    nome = fields.Str()
    data_nascimento = fields.Date()
    cargo = fields.Str()
    status_covid = fields.Int()
    status_afastamento = fields.Int()
    sexo = fields.Str()
    quantidade_pessoas = fields.Int()
    quantidade_vacinas = fields.Int()
    fabricante = fields.Str()
    justificativa = fields.Str()
    carteirinha_vacinacao = fields.Str()
    
    usuario_id_usuario = fields.Int()
    #TODO: usuario = fields.Nested(UsuarioSrializer)

    campus_instituto_id_campus_instituto = fields.Int()
    #TODO: campus_instituto = fields.Nested(CampusInstitutoSerializer)