'''
    Módulo com a classe modelo da tabela `direcao`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from marshmallow import fields, Schema

class DirecaoSerializer(Schema):
    '''
        Classe modelo que serializa a tabela `direcao`, onde descreve quem esteve ou está na direção do campus.

        ...

        Atributos
        ---------
        `id_direcao : int`    
                Identificador da direção.
        `data_entrada : Date(yyyy-mm-dd)`
                Data de entrada na direção do campus.
        `data_saida : Date(yyyy-mm-dd)`
                Data de saída da direção do campus.
        `status_ativo` : INT | None
                Se está ativo na direção do campus.
        `docente_id_docente` : int| None
                Identificador do docente que está ma direção do campus.
        `docente : DocenteModel`
                Dados do docente que está na direção do campus.
    '''
    

    id_direcao = fields.Int()
    data_entrada = fields.Date()
    data_saida = fields.Date()
    status_ativo = fields.Int()
    
    docente_id_docente = fields.Int()
    #TODO:docente = fields.Nested(DocenteSerializer)