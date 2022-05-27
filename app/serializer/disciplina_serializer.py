'''
    Módulo com a classe modelo da tabela `disciplina`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''

from dataclasses import field
from marshmallow import fields, Schema

class DisciplinaSerializer(Schema):
    '''
        Classe-modelo que serializa a tabela `disciplina`, que é utilizada pelo usário docente para criar solicitações de acesso aos discentes que assistirão sua maéria, do bancop de dados.

        ...

        Atributos
        ---------
        `id_disciplina : int`
        `nome : str`
        `código_sigaa : str`
        `semestre : str | None`
        `curso_id_curso : int | None`
        `docente_id_docente : int | None`
        `discentes : list[DiscenteModel]`
        `docente : DocenteModel`

    '''

    id_disciplina = fields.Int()
    nome = fields.Str()
    codigo_sigaa = fields.Str()
    semestre = fields.Int()
    curso_id_curso = fields.Int()
    docente_id_docente = fields.Int()
    #TODO: discentes = fields.Nested(DiscenteSerializer)
    #TODO: docente = fields.Nested(DocenteSerializer)
    