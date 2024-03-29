from ..util.http_status_code import OK, CREATED, BAD_REQUEST, NOT_FOUND_REQUEST


class BaseController:
    
    @classmethod
    def get(cls, id, Model):
        
        if not id:
            return {"message":"id não pode ser nulo."}, BAD_REQUEST

        model = Model.find_by_id(id)
        if not model:
            return {"message":"Recurso não encontrado."}, NOT_FOUND_REQUEST
      
        return model.serialize(), OK
    
    @classmethod
    def post(cls, body, Model):

        if not body:
            return {"message":"Não encontrado dados no corpo da requisição."}, BAD_REQUEST
        
        # print(body)
        try:
            new_model = Model(**body)
            new_model.save_to_db()
        except ValueError as msg:
            return {"message":msg.args[0]}, BAD_REQUEST
        except Exception:
            return {"message":msg.args[0]}, BAD_REQUEST
        return new_model.serialize(), CREATED

    @classmethod
    def put(cls, body, Model):

        if not body:
            return {"message":"Dados não encontrado no corpo da requisição."}, BAD_REQUEST
        
        try:
            id_key = list(filter(lambda k: k.startswith("id_"), body.keys()))[0]
        except IndexError:
            return {"message":"id não encontrado. O id do recurso deve ser enviado na requisição para realizar a atualização."}, BAD_REQUEST
        
        id = body.get(id_key)

        model = Model.find_by_id(id)
        if not model:
            return {
                "message":"dados não encontrado para esse recurso."\
                "Para realizar a atualização o recurso deve está registrado no banco de dados."
            }, BAD_REQUEST

        Model.update_by_id(id, body)
    
        return {"message":"Atualizado com sucesso."}, OK

    @classmethod
    def delete(cls, id, Model):
        
        model = Model.find_by_id(id)
        
        if not model:
            return {"message":"Can't delete, not found this resource."}, BAD_REQUEST
        
        model.delete_from_db()

        return {"message":" Deletado"}, OK

    @classmethod
    def get_list(cls, Model, campus_instituto_id_campus_instituto=None):
        if campus_instituto_id_campus_instituto:
            models = Model.query_all(campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto)
        else:
            models = Model.query_all()    
        serialized = [model.serialize() for model in models]
        return serialized

class BaseHasUsuarioAndDiscenteController(BaseController):
    
    @classmethod
    def get_list(cls, Model, campus_instituto_id_campus_instituto=None, 
                                usuario_id_usuario=None, 
                                discente_id_discente=None,
                                disciplina_id_disciplina=None):
        if campus_instituto_id_campus_instituto:
            models = Model.query_all(campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto)
        elif usuario_id_usuario:
            models = Model.query_all(usuario_id_usuario=usuario_id_usuario)
        elif discente_id_discente:
            models = Model.query_all(discente_id_discente=discente_id_discente)
        elif disciplina_id_disciplina:
            models = Model.query_all(disciplina_id_disciplina=disciplina_id_disciplina)
        else:
            models = Model.query_all()    
        serialized = [model.serialize() for model in models]
        return serialized

class BaseHasNameController(BaseController):
    
    @classmethod
    def get_all_names(cls, Model, campus_instituto_id_campus_instituto=None):
        
        # models_names receve a tuple of (nome , id)
        model_names = Model.query_all_names(campus_instituto_id_campus_instituto)

        #create a dict with nome as key and id as a value
        names_dict = [{"nome":row.nome, "id":row.id} for row in model_names]
        
        return names_dict

class BaseHasCursoController(BaseController):
    
    @classmethod
    def get_all_names(cls, Model, curso_id_curso=None):
        
        # models_names receve a tuple of (nome , id)
        model_names = Model.query_all_names(curso_id_curso)

        #create a dict with nome as key and id as a value
        names_dict = [{"nome":row.nome, "id":row.id} for row in model_names]
        
        return names_dict

# class to show up recurso_campus
class BaseHasHorarioController(BaseHasNameController):

        @classmethod
        def get_all_names(cls, Model, campus_instituto_id_campus_instituto, usuario_id_usuario):
            # models_names receve a list of resources
            model_names = Model.query_all_names(campus_instituto_id_campus_instituto, usuario_id_usuario)

            #create a dict with nome as key and id as a value
            names_dict = [
                {
                    "nome":row.nome, 
                    "id":row.id,
                    "usuario_id_usuario":row.usuario_id_usuario, 
                    "inicio_horario":str(row.inicio_horario),
                    "fim_hoario":str(row.inicio_horario)
                } for row in model_names
            ]
            
            return names_dict

#Class to handle users
class BaseHasUsuarioController(BaseHasNameController):
    """
    Recurso que possue um usuário (login)
    
    """
    @classmethod
    def post(cls, body, Model, usuario):

        if not body:
            return {"message":"não há dados no body da requsição."}, BAD_REQUEST
        
        #print(body)

        try:
            new_model = Model(**body, usuario=usuario)
            new_model.save_to_db()
        
        except ValueError as msg:
            return {"message":msg.args[0]}, BAD_REQUEST
        except Exception as msg:
            return {"message":msg.args[0]}, BAD_REQUEST

        return new_model.serialize(), CREATED

    @classmethod
    def get_by_usuario(cls, usuario_id_usuario, Model):

        model_queried = Model.find_by_id_usuario(usuario_id_usuario)
        if model_queried:
            return model_queried.serialize(), OK
        
        return {"message":"usuario not found"}, NOT_FOUND_REQUEST

class BaseHasDiscentesListController(BaseHasNameController):
    """
    Classe que lida com a criação de disciplina
    
    """
    @classmethod
    def post(cls, body, Model, discentes):

        if not body:
            return {"message":"não há dados no body da requsição."}, BAD_REQUEST
        
        # print(body)
        try:
            model = Model(**body)

            for discente in discentes:
                model.discentes.append(discente)
            model.save_to_db()
        except:
            return {"message":"Há dado(s) inválido(s) no body da requisição."}, BAD_REQUEST

        return model.serialize(), CREATED
    
    @classmethod
    def get_all_names(cls, Model, 
                docente_id_docente=None
            ):
        
        # models_names receve a tuple of (nome , id)
        models = Model.query_all(
                                    docente_id_docente=docente_id_docente
                                )

        #create a dict with nome as key and id as a value
        body_dict = [model.serialize() for model in models]
        return body_dict

#class to randle user that has matricula or siape
class BaseHasMatriculaController(BaseHasNameController):

    @classmethod
    def get_by_matricula(cls, Model, matricula):

        query = Model.find_by_matricula(matricula)
        if not query:
            return {"message":"Not found this discente."}, NOT_FOUND_REQUEST
      
        return query.serialize(), OK
    
    @classmethod
    def get_vacinacao(cls, Model, matricula):

        query = Model.get_vacinacao(matricula)
        if not query:
            return {"message":"Not found."}, NOT_FOUND_REQUEST
      
        return query, OK
    
    @classmethod
    def get_vacinacoes(cls, Model, curso_id_curso, ano_turma, numero_de_doses):

        model_discentes = Model.query_vacinacoes(curso_id_curso, ano_turma, numero_de_doses)

        #create a dict with nome as key and id as a value
        discentes_dict = [{"nome":row.nome, "id":row.id, "matricula":row.matricula, "turma":row.turma, "carteirinha_vacinacao":row.carteirinha_vacinacao} for row in model_discentes]
        
        return discentes_dict

    @classmethod
    def get_all_names(cls, Model):
        
        # models_names receve a tuple of (nome , id)
        model_names = Model.query_all_names()

        #create a dict with nome as key and id as a value
        names_dict = [{"nome":row.nome, "id":row.id, "matricula":row.matricula, "curso_id_curso":row.curso_id_curso, "campus_instituto_id_campus_instituto":row.campus_instituto_id_campus_instituto} for row in model_names]
        
        return names_dict

class BaseHasSiapeController(BaseHasNameController):

    @classmethod
    def get_vacinacao(cls, Model, siape):

        query = Model.get_vacinacao(siape)
        if not query:
            return {"message":"Not found."}, NOT_FOUND_REQUEST
      
        return query, OK


    @classmethod
    def get_all_names(cls, Model):
        
        # models_names receve a tuple of (nome , id)
        model_names = Model.query_all_names()

        #create a dict with nome as key and id as a value
        names_dict = [{"nome":row.nome, "id":row.id, "siape":row.other_id} for row in model_names]
        
        return names_dict

class BaseHasCPFController(BaseController):
    
    @classmethod
    def get_all_names(cls, Model):
        
        # models_names receve a tuple of (nome , id)
        model_names = Model.query_all_names()

        #create a dict with nome as key and id as a value
        names_dict = [{"nome":row.nome, "id":row.id, "cpf":row.cpf} for row in model_names]
        
        return names_dict