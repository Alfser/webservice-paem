'''
    Módulo com a classe de serializqação da tabela `acesso_permitido`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''

from marshmallow import fields, Schema

class AcessoPermitidoSerializer(Schema):
      '''
        Classe para serializar a tabela acesso_permtido.

        ...

        Atributos
        ---------
        id_acesso_permitido : int
                identificador do acesso permitido.
        temperatura : decimal
                valor da temperatura medida no discente.
        hora_entrada : str
                hora da entrada do discente.
        hora_saida : str
                hora da saída do discente.
        recurso_campus_id_recurso_campus : int
                identificador do recurso solicitado.
        campus_instituto_id_campus_instituto : int
                identificador do campus onde o acesso foi permitido

      '''
      
      __tablename__ = "acesso_permitido"

      id_acesso_permitido = fields.Int()
      temperatura = fields.Float()
      matricula_discente = fields.Str()
      recurso_campus_id_recurso_campus = fields.Int()
      hora_entrada = fields.Time()
      hora_saida = fields.Time()
      solicitacao_acesso_id_solicitacao_acesso = fields.Int()
      recurso_campus_id_recurso_campus = fields.Int()
    #   TODO: recurso campus object
      campus_instituto_id_campus_instituto = fields.Int()