'''
    Módulo com a classe modelo da tabela `notificacao_covid`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''

from marshmallow import fields, Schema

class NotificacaoCovidSerializer(Schema):
    '''
        Classe-modelo que serializa a tabela `notificacao_covid`, que é esponsável por receber as notificações dos alunos que tiveram Covid-19.

        ...

        Atributos
        ---------
        `id_notificacao_covid : int`
                Identificador da tupla de notificação de Covid.
        `data : Date(yyyy-mm-dd) | None`
                Data em que teve os sintomas de Covid.
        `data_diagnostico : Date(yyyy-mm-dd)`
                Data em que recebeu o diagnóstico de Covid.
        `teste : boolean | None `
                Se fez o teste para ver se estava com covid.
        `nivel_sintomas : str | None`
                Quais foram os sintomas que teve.
        `observacoes : str | None`
                Algum adendo a despeito da notificação de covid.
        `matricula_discente : int | None`
                Número de matrícula do discente.
        `discente : DiscenteModel`
                Dados do discente que faz a notificação de covid.
        `campus_instituto_id_campus_instituto : int | None`
                Identificador do campus da notificação de covid
        `campus_instituto : CampusInstitutoModel`
                Dados do campus ou instituto que foi realizado a notificação de covid.

    '''


    id_notificacao_covid = fields.Int()
    data = fields.Date()
    data_diagnostico = fields.Date()
    teste = fields.Bool()
    nivel_sintomas = fields.Int()
    observacoes = fields.Str()

    matricula_discente = fields.Str()
    # TODO: discente = fields.Nested(DiscenteSerializer)


    campus_instituto_id_campus_instituto = fields.Int()
    #TODO: campus_instituto = fields.Nested(CampusInstitutoSerializer)

