'''
    Módulo com a classe modelo da tabela `coordenacao`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''

from marshmallow import fields, Schema

class CoordenacaoSerializer(Schema):
    '''
        Classe-modelo para serializar a tabela `coodenacao` que é destina ao coodenador de cada curso.

        ...

        Atrinutos
        ---------
        `id_coordenacao : int`
        `data_entrada : Date(yyyy-mm-dd)| None`
        `data_saida : Date(yyyy-mm-dd)| None`
        `status_ativo : int | None`
        `curso_id_curso : int`
        `curso : list[CursoModel]`
        `docente_id_docente : int`
        `docente : list[DocenteModel]`

    '''
    
    id_coordenacao = fields.Int()
    data_entrada = fields.Date()
    data_saida = fields.Date()
    status_ativo = fields.Int()
    curso_id_curso = fields.Int()
    # TODO: curso = fields.Nested(CursoSerializer)
    docente_id_docente = fields.Int()
    # TODO: docente = fields.Nested(DocenteSerializer)

    def __repr__(self):
        return '<coordenacao %r>' % self.id_coordenacao
