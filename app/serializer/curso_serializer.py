'''
    Módulo com a classe modelo da tabela `curso`.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''
from dataclasses import field
from marshmallow import fields, Schema

from .campus_instituto_serializer import CampusInstitutoSerializer

class CursoSerializer(Schema):
    '''
        Classe-modelo que serializar a tabela `curso` do banco de dados.

        ...

        Atributos
        ---------
        `id_curso : int`
                Identificador do curso.
        `nome : str`
                Nome do curso.
        `data_fundacao : Date(yyyy-mm-dd)`
                Ano de fundação do curso.
        `unidade : str`
                Unidade a qual pertence o curso.
        `cidade : str`
                Cidade a qual o curso é ofertado.
        `grau_academico : string`
                Grau acadêmico do curso(Bacharel, licenciatura...).
        `situacao : str`
                situação do curso.
        `modalidade : str`
                modalidade do curso.
        `convenio : str`
                convênio do curso.
        `ativo : int`
                se o curso está ativo.
        `campus_instituto_id_campus_instituto : int`
                Identificador do campus ou instituto do curso.
        `docentes : list[DocenteModel]`
                Lista de docentes que fazem parte desse curso.
        `disciplinas : list[DisciplinaModel]`
                Lista de disciplinas que pertencem a esse curso.
        `discentes : list[DiscenteModel]`
                Lista de discentes que são desse curso.
        
    '''

    id_curso = fields.Int()
    nome = fields.Str(required=True)
    data_fundacao = fields.Date()
    unidade = fields.Str()
    cidade = fields.Str()
    grau_academico = fields.Str()
    situacao = fields.Str()
    modalidade = fields.Str()
    convenio = fields.Str()
    ativo = fields.Str()
    
    campus_instituto_id_campus_instituto = fields.Int(required=True)

    #TODO:campus_instituto = fields.Nested(CampusInstitutoSerializer.nome)

    #TODO:docentes = fields.Nested(DOcenteSerializer.nome)
    
    #TODO:disciplinas = fields.Nested(DisciplinaSerializer, many=True)

    #TODO:discentes = fields.Nested(DiscenteSerializer,many=True)

