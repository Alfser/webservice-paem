from ..util.http_status_code import BAD_REQUEST, UNAUTHORIZED_REQUEST
from ..util.authorization import Authorization

from flask_restful import Resource, request
from flask_httpauth import HTTPBasicAuth

from functools import wraps
from datetime import datetime, timedelta
from jwt import encode, decode

http_auth = HTTPBasicAuth()

# rota normal para obter o token
class AuthorizationResource(Resource):
    
    ENDPOINT = 'auth'
    ROUTE = '/auth'
    
    @http_auth.verify_password
    def verify_credencials(username, password):
        is_auth = Authorization.verify_user(username, password)
        return is_auth
    
    @http_auth.login_required
    def post(self):
        login = http_auth.username()
        #print("usuario: ", login)
        return Authorization.get_token(login)

# rota do chatbot para obter o token
class AuthorizationBotResource(Resource):
    
    ENDPOINT = 'auth.bot'
    ROUTE = '/auth.bot'
    
    @Authorization.cpf_required
    def post(self, usuario):
        return Authorization.get_token(usuario.login)

