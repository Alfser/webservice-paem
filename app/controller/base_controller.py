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
        
        print(body)
        new_model = Model(**body)
        new_model.save_to_db()

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

        return {"message":" Deleted"}, OK

    @classmethod
    def get_list(cls, Model, campus_instituto_id_campus_instituto=None):
        models = Model.query_all(campus_instituto_id_campus_instituto)
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
        def get_all_names(cls, Model, campus_instituto_id_campus_instituto=None):
            # models_names receve a list of resources
            model_names = Model.query_all_names(campus_instituto_id_campus_instituto)

            #create a dict with nome as key and id as a value
            names_dict = [
                {
                    "nome":row.nome, 
                    "id":row.id, 
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
        
        print(body)
        new_model = Model(**body, usuario=usuario)
        new_model.save_to_db()

        return new_model.serialize(), CREATED


    @classmethod
    def get_by_usuario(cls, usuario_id_usuario, Model):

        model_queried = Model.find_by_id_usuario(usuario_id_usuario)
        if model_queried:
            return model_queried.serialize(), OK
            
        return {"message":"usuario not found"}, NOT_FOUND_REQUEST

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
    def get_all_names(cls, Model):
        
        # models_names receve a tuple of (nome , id)
        model_names = Model.query_all_names()

        #create a dict with nome as key and id as a value
        names_dict = [{"nome":row.nome, "id":row.id, "matricula":row.other_id} for row in model_names]
        
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