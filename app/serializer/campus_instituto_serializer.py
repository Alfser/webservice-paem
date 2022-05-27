'''
    Módulo com a classe modelo da tabela `campus_instituto`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''

from marshmallow import fields, Schema

class CampusInstitutoSerializer(Schema):
    '''
       Classe para serializar a tabela `campus_instituto` do banco de dados.

       ...

       Atributos
       ---------
       `id_campus_instituto : int`
                Identificador do campus ou instituto.
       `ano_fundacao : str (yyyy-mm-dd)`
                Ano da fundação do campus ou instituto.
       `nome : str`
                Nome do campus ou instituto.
       `abertura_total : int`
                Se o campus ou instituto tem abertura total, ou seja, se o campus ou instituto permite ou não a entrada sem ter tomado a vacina contra a Covid-19.
       `direcao_id_direcao : int`
                Identificador da tabela direcao
       `direcao : list[DirecaoModel]`
                Lista com as direção(s) dos crusos do campus ou institutos.
        
    '''

    id_campus_instituto = fields.Int()
    nome = fields.Str(required=True)
    abertura_total = fields.Int(required=True)
    ano_fundacao = fields.Date()
    direcao_id_direcao = fields.Int(allow_none=True)