from flask_apispec import marshal_with, Ref
from flask_apispec.views import MethodResource

@marshal_with(Ref('schema'))
class BaseResource(MethodResource):
    schema = None