'''
    Módulo com as classes Base e especializadas usadas como Modelos 
    com os métodos genéricos usados pelas outras classes mais especícicas.
    
    autor : alfser
    email : j.janilson12@gmail.com
'''

# Model class base of tables
from ..database import db

# class to work on object model properties
class BaseModel():
    '''
        Classe base com os métodos de consulta, adição, deleção e atualização de dados do banco de dados.

        ...

        Métodos
        -------
        `@classmethod`
        `find_by_id(id):`
                Consulta dos dados do banco baseado no id enviado como parâmetro.
        `@classmethod`
        `query_all(campus_instituto_id_campus_instituto=None):`
                Consultar todos os dados do banco na tabela do modelo,
                ado campus_instituto_id_campus_instituto seja None, 
                acordo com o objeto ou filtrando pelo campus_instituto.
        `@classmethod`
        `update_by_id(id, dict):`
                Atualiza os dados do objeto-modelo, identificado pelo id, 
                de acordo com os dados enviados no dict.
        `save_to_db():`
                Registrar no banco as alterações realizadas no objeto relacionado.
        `@classmethod`
        `save_all(values):`
                Salvar no banco todos os dados registrados na lista de objetos-modelos.
        `delete_from_db():`
                Deletar os dados do banco relacionandos a este objeto-modelo.
        `@classmethod`
        `save():`
                Salvar todas as alterações realizadas no banco.
    '''        

    @classmethod
    def find_by_id(cls, id):
        '''
         Consulta os dados do banco de acordo com o id enviado como parâmetro.

         ...

         Parâmeros
         ---------
         `id : int`
                identificador do dado na tabela referente ao objeto-modelo.
        '''
        return cls.query.get(id)
    
    @classmethod
    def query_all(cls, campus_instituto_id_campus_instituto=None):
        '''
        Consultar todos os dados do banco na tabela do modelo,
        cado campus_instituto_id_campus_instituto seja None, 
        acordo com o objeto ou filtrando pelo campus_instituto.
        
        ...

        Parâmeros
        ---------
        `campus_instituto_id_campus_instituto : int | None`
                identificador do campus_instituto.

        '''
        if campus_instituto_id_campus_instituto: 
           return cls.query.filter_by(
             campus_instituto_id_campus_instituto = campus_instituto_id_campus_instituto
         ).all()
        return cls.query.all() 

    @classmethod
    def update_by_id(cls, id, dict):
        '''
        Atualiza os dados do objeto-modelo, identificado pelo id, 
        de acordo com os dados enviados no dict.

        ...

        Parâmetros
        ----------
        `id : int`
                identificador da tupla na tabelo mapeada pelo objeto-modelo.
        `dict : dict`
                dicionário com os novos dados que serão atualizações na tabela de acordo com onjeto-modelo.
        '''

        model = cls.query.get(id)
        for key, value in dict.items():
            if hasattr(model, key):
                setattr(model, key, value)
        cls.save()

    def save_to_db(self):
        '''
        Registrar no banco as alterações realizadas nos dados de acordo com o objeto-modelo.

        ...

        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def save_all(cls, values):
        '''
        Salvar no banco todos os dados registrados na lista em objetos-modelos.

        ...

        `values : list`
                lista de objetos-modelos com os dados que serão enviados ao banco de dados.
        '''

        db.session.add_all(values)
        db.session.commit()

    def delete_from_db(self):
        '''
        Deletar os dados do banco relacionados a este objeto-modelo.

        ...

        '''
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def save(cls):
        '''
        Salvar todas as alterações realizadas no banco.
        '''
        db.session.commit()

class BaseHasUsuarioAndDiscenteModel(BaseModel):
    '''
        Classe base especializada para conter principalmente métodos de filtragem por discente e usuário.

        ...

        Métodos
        -------
        `@classmethod`
        `query_all(campus_instituto_id_campus_instituto=None, usuario_id_usuario=None, discente_id_discente=None, disciplina_id_disciplina=None, docente_id_docente=None):`
                Consultar os dados fitrando de acrodo com os parâmetros enviados no parâmetro da função.

    '''

    @classmethod
    def query_all(cls, campus_instituto_id_campus_instituto=None, 
                        usuario_id_usuario=None, 
                        discente_id_discente=None,
                        disciplina_id_disciplina=None,
                        docente_id_docente=None):
        '''
            Consultar os dados fitrando de acrodo com os parâmetros enviados no parâmetro da função.
            
            ...

            Parâmetros
            ----------
            `campus_instituto_id_campus_instituto : int | None`
                    identificador do campus ou institituto.
            `usuario_id_usuario : int | None`
                    identificador do usuário.
            `discente_id_discente : int | None`
                    identificador do discente.
            `disciplina_id_disciplina : int | None`
                    identificador da disciplina.
            `docente_id_docente : int | None`
                    identificador do docente.
        '''

        if campus_instituto_id_campus_instituto: 
          return cls.query.filter_by(
            campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto
        ).all()
        elif usuario_id_usuario: 
          return cls.query.filter_by(
            usuario_id_usuario=usuario_id_usuario
        ).all()
        elif discente_id_discente: 
          return cls.query.filter_by(
            discente_id_discente=discente_id_discente
        ).all()
        elif disciplina_id_disciplina: 
          return cls.query.filter_by(
            disciplina_id_disciplina=disciplina_id_disciplina
        ).all()
        elif docente_id_docente: 
          return cls.query.filter_by(
            docente_id_docente=docente_id_docente
        ).all()

        return cls.query.all()

# class to working on person atributes 
class BaseHasNameModel(BaseModel):
    '''
        Classe base especializada para classes-modelos que tenham o atriburo `nome`.

        ...

        Métodos
        -------
        `@classmethod`
        `query_all_names(cls, *entiries, campus_instituto_id_campus_instituto=None, usuario_id_usuario=None):`
                Consultar dados do banco de acordo com os parâmetros usados para selecionar os dados, em `entity`, da consulta e os parâmetros usados para filtragem desta.

    '''

    @classmethod
    def query_all_names(cls, *entiries, campus_instituto_id_campus_instituto=None, usuario_id_usuario=None):
        '''
            Consultar dados do banco de dados de acordo com os parâmetros usados para selecionar os dados, em `entity`, da consulta e os parâmetros usados para filtragem desta.

            ...

            Parâmetros
            ----------
            `entiries : Model`
                    Clase-Model com as colunas buscadas na consulta.
            `campus_instituto_id_campus_instituto: int | None`
                    Identificador do campus ou intituto.
            `usuario_id_usuario : int | None`
                    Identificador fdo usuário.

        '''
        if campus_instituto_id_campus_instituto and usuario_id_usuario:
            return list(db.session.query(*entiries).filter_by(campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto, usuario_id_usuario=usuario_id_usuario).all())
        return db.session.query(*entiries).all()

class BaseHasCurso(BaseModel):
    '''
        Especialização para classes-base que tenham o atributo curso.

        ...

        Métodos
        -------

        `@classmethod`
        `query_all_names(cls,*entiries, curso_id_curso=None):`
                Consultar os dados filtrando por curso.
    '''

    @classmethod
    def query_all_names(cls,*entiries, 
                curso_id_curso=None
            ):
        '''
            Consultar os dados filtrando por curso.

            ...

            Parâmetros
            ----------
            `entities : Model`
                    Classe-model com as colunas desejadas da tabela.
            `curso_id_curso : int | None`
                    Identificador do curso.
        '''
        if curso_id_curso:
            return list(db.session.query(*entiries).filter_by(
                    curso_id_curso=curso_id_curso
                ).all())
        return db.session.query(*entiries).all()

class BaseListaDisciplina(BaseModel):
    '''
        Classe base especializada para moldar a forma distar as disciplinas.

        ...

        `@classmethod`
        `query_all_names(cls,*entiries, campus_instituto_id_campus_instituto=None, docente_id_docente=None):`
                Consultar a tabela de disciplinas, filtrar e listar as colunas especificadas.
    '''
    @classmethod
    def query_all_names(cls,*entiries, 
                campus_instituto_id_campus_instituto=None, 
                docente_id_docente=None
            ):
        '''
            Consultar a tabela de disciplinas, filtrar e listar as colunas especificadas.

            ...

            Parâmetros
            ----------
            `entities : Model`
                    Classe-model com as colunas desejadas da tabela.
            `campus_instituto_id_campus_instituto : int | None`
                    Identificador do campus ou instituto.
            `docente_id_docente : int | None`
                    Identificador do docente.
        '''

        if campus_instituto_id_campus_instituto:
            return list(db.session.query(*entiries).filter_by(
                    campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto
                ).all())
        
        if docente_id_docente:
            return list(db.session.query(*entiries).filter_by(
                    docente_id_docente=docente_id_docente
                ).all())

        return list(db.session.query(*entiries).all())

class BaseHasSiape(BaseModel):
    '''
        Classe base especializada para classes-modelos que tenham o atributo siape.

        ...

        Métodos
        -------
        `@classmethod`
        `find_by_siape(*entiries, siape):`
                        Consultar os dados do banco, com as colunas especificadas em `entities`, filtrando de acordo com `siape`.
    '''
    @classmethod
    def find_by_siape(cls, *entiries, siape):
        '''
           Consultar os dados do banco, com as colunas especificadas em `entities`, filtrando de acordo com `siape`.
           
           ...

           Parâmetros
           ----------
           `entities : Model`
                        Classe-model com as colunas desejadas da tabela.
           `siape : str`
                        Codigo siape do técnico ou do docente.
        '''

        return db.session.query(*entiries).filter_by(siape=siape).first()

# List id_usuario of all that is user
class BaseHasUsuarioModel(BaseHasNameModel):
    '''
        Classe base especializada para classes-modelos que tenham relação com a tabela usuario.

        ...

        Métodos
        -------
        `@classmethod`
        `find_by_id_usuario(usuario_id_usuario):`
                        Consultar os dados do banco de acordo com a classe-modelo filtrando por usuário.
    '''

    @classmethod
    def find_by_id_usuario(cls, usuario_id_usuario):
        '''
           Consultar os dados do banco de dados de acordo com a classe-modelo filtrando por usuário.

           ...

           Parâmetros
           ----------
           `usuario_id_usuario : int`
                        Identificador do usuário.

        '''
        
        return cls.query.filter_by(usuario_id_usuario=usuario_id_usuario).first()

class BaseHasVacinacaoModel(BaseHasUsuarioModel):
    '''
        Classe base especializada para classes-modelos que tenham os dado de vacinação do aluno.

        ...

        Métodos
        -------
        `@classmethod`
        `query_all_names(cls, *entiries, campus_instituto_id_campus_instituto=None, usuario_id_usuario=None):`
                Consultar dados do banco de acordo com os parâmetros usados para selecionar os dados, em `entity`, da consulta e os parâmetros usados para filtragem desta.
        `@classmethod`
        `query_vacinacoes(cls, *entiries, curso_id_curso=None, ano_turma=None, numero_de_dose=None):`
                Consultar dados de vacinações do banco de dados de acordo com os parâmetros de filtragem..
    '''

    @classmethod
    def query_vacinacoes(cls, *entiries, curso_id_curso=None, ano_turma=None, numero_de_doses=None):
        '''
        Consultar dados de vacinações do banco de dados de acordo com os parâmetros de filtragem.

        ...

        Parâmetros
        ----------
        `entiries : Model`
                    Clase-Model com as colunas buscadas na consulta.
        `curso_id_curso : int | None`
                        Identficador do curso usado para filtragem na consulta.
        `ano_turma : int | None`
                        turma do considerado o ano de ingresso do discente usado para filtragem na consulta.
        `numero_de_dose : int | None`
                        número de dose tomadas usado para filtragem na consulta.
        '''

        if curso_id_curso and ano_turma and numero_de_doses:
                return list(db.session.query(*entiries).filter_by(curso_id_curso=curso_id_curso, quantidade_vacinas=numero_de_doses, ano_de_ingresso=ano_turma).all())
        elif curso_id_curso and ano_turma:
                return list(db.session.query(*entiries).filter_by(curso_id_curso=curso_id_curso, ano_de_ingresso=ano_turma).all())
        elif curso_id_curso and numero_de_doses:
                return list(db.session.query(*entiries).filter_by(curso_id_curso=curso_id_curso, quantidade_vacinas=numero_de_doses).all())
        elif ano_turma and numero_de_doses:
                return list(db.session.query(*entiries).filter_by(ano_de_ingresso=ano_turma, quantidade_vacinas=numero_de_doses).all())
        elif curso_id_curso:
                return list(db.session.query(*entiries).filter_by(curso_id_curso=curso_id_curso).all())
        elif ano_turma:
                return list(db.session.query(*entiries).filter_by(ano_de_ingresso=ano_turma).all())
        elif numero_de_doses:
                return list(db.session.query(*entiries).filter_by(quantidade_vacinas=numero_de_doses).all())
        else:
                return db.session.query(*entiries).all()
