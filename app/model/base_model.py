
# Model class base of tables
from ..database import db

# class to work on object model properties
class BaseModel():
    
    @classmethod
    def find_by_id(cls, id):
       return cls.query.get(id)
    
    @classmethod
    def query_all(cls, campus_instituto_id_campus_instituto=None):
       if campus_instituto_id_campus_instituto: 
          return cls.query.filter_by(
            campus_instituto_id_campus_instituto = campus_instituto_id_campus_instituto
        ).all()
       return cls.query.all() 

    @classmethod
    def update_by_id(cls, id, dict):
        model = cls.query.get(id)
        for key, value in dict.items():
            if hasattr(model, key):
                setattr(model, key, value)
        cls.save()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def save_all(cls, values):
        db.session.add_all(values)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def save(cls):
        db.session.commit()

# class to working on person atributes 
class BaseHasNameModel(BaseModel):
    '''
        Base model for tables that has a name column
    '''
    # @classmethod
    # def find_by_name(cls, nome):
    #    return cls.query.filter_by(nome=nome).first()

    # @classmethod
    # def update_by_name(cls, nome, dict):
    #    cls.query.filter_by(nome=nome).update(dict)
    #    cls.save()
    @classmethod
    def query_all_names(cls, *entiries, campus_instituto_id_campus_instituto=None):
        if campus_instituto_id_campus_instituto:
            return list(db.session.query(*entiries).filter_by(campus_instituto_id_campus_instituto = campus_instituto_id_campus_instituto).all())
        return db.session.query(*entiries).all()
        
class BaseHasCurso(BaseModel):

    @classmethod
    def query_all_names(cls,*entiries, 
                curso_id_curso=None
            ):
        if curso_id_curso:
            return list(db.session.query(*entiries).filter_by(
                    curso_id_curso=curso_id_curso
                ).all())
        return db.session.query(*entiries).all()

class BaseListaDisciplina(BaseModel):

    @classmethod
    def query_all_names(cls,*entiries, 
                campus_instituto_id_campus_instituto=None, 
                docente_id_docente=None
            ):
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

    @classmethod
    def find_by_siape(cls, *entiries, siape):
        return db.session.query(*entiries).filter_by(siape=siape).first()

# List id_usuario of all that is user
class BaseHasUsuarioModel(BaseHasNameModel):
    '''
        Base model for tables that has a name column
    '''

    @classmethod
    def find_by_id_usuario(cls, usuario_id_usuario):
       return cls.query.filter_by(usuario_id_usuario=usuario_id_usuario).first()