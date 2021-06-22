from ..util.http_status_code import OK, CREATED, BAD_REQUEST, NOT_FOUND_REQUEST


class BaseController:
    
    @classmethod
    def get_by_id(cls, id, Model):
        
        if not id:
            return{"message":"id can't be null."}, BAD_REQUEST

        model = Model.find_by_id(id)
        if not model:
            return {"message":"Not found this resource."}, NOT_FOUND_REQUEST
      
        return model.serialize(), OK
    
    @classmethod
    def post(cls, body, Model):

        if not body:
            return {"message":"Not found body data ."}, BAD_REQUEST
        
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
    
        return {"message":"Updated"}, OK

    @classmethod
    def delete(cls, id, Model):
        
        model = Model.find_by_id(id)
        
        if not model:
            return {"message":"Can't delete, not found this discente."}, BAD_REQUEST
        
        model.delete_from_db()

        return {"message":" Deleted"}, OK

    @classmethod
    def get_list(cls, Model):
        models = Model.query_all()
        serialized = [model.serialize() for model in models]
        return serialized
    
class BaseHasNameController(BaseController):
    
    @classmethod
    def get_all_names(cls, Model):
        
        # models_names receve a tuple of (nome , id)
        model_names = Model.query_all_names()

        #create a dict with nome as key and id as a value
        names_dict = {row.nome:row.id for row in model_names}
        
        return names_dict

class BaseHasUsuarioController(BaseHasNameController):

    @classmethod
    def post(cls, body, Model, usuario):

        if not body:
            return {"message":"não há dados no body da requsição."}, BAD_REQUEST
        
        print(body)
        new_model = Model(**body, usuario=usuario)
        new_model.save_to_db()

        return new_model.serialize(), CREATED