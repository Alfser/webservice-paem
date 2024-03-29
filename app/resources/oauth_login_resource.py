from ..database.config import OAuth2Credentials
from ..controller.usuario_controller import UsuarioController
from ..util.authorization import Authorization

from flask_restful import Resource, request, reqparse
from requests_oauthlib import OAuth2Session
import logging

class OAuth2LoginResource(Resource):    
    ENDPOINT = 'login'
    ROUTE = '/oauth/login'
        
    def get(self):
        api_credentials = OAuth2Credentials.get_api_credentials()

        oauth_client = OAuth2Session(
            client_id=api_credentials['client_id'], 
            redirect_uri=api_credentials['redirect_uri']
        )

        authorization_url, state = oauth_client.authorization_url(
            'https://autenticacao.ufopa.edu.br/authz-server/oauth/authorize', 
            state=api_credentials['state']
        )
        
        return {'authozation_url':authorization_url}

    def post(self):
        api_credentials = OAuth2Credentials.get_api_credentials()

        oauth_client = OAuth2Session(
            client_id=api_credentials['client_id'], 
            redirect_uri=api_credentials['redirect_uri']
        )

        #Receving access code
        response = request.json

        #Verify if recive state sent
        if not (response.get('state')==api_credentials.get('state')):
            return {'message':'acesso não autorizado.'}, 401

        response_code = response['code']
        
        #Get access token from oauth server
        try:
            _ = oauth_client.fetch_token(
                'https://autenticacao.ufopa.edu.br/authz-server/oauth/token',
                code=response_code,
                include_client_id=api_credentials['client_id'],
                client_secret=api_credentials['client_secret']
            )
        except Exception as msg:
            logging.error(msg=msg.args)
            return {'message':'Credencial de acesso inválida.'}, 401

        # access ctic api
        api_response = oauth_client.get(
            'https://api.ufopa.edu.br/usuario/v1/usuarios?login=francisco.nunes', 
            verify=False, 
            headers={'x-api-key':api_credentials['x_api_key']}
        )[0] # FIXME: trocar o serviço para consultar os dados do usuário que logou.

        usuario = UsuarioController.get_by_login(api_response.get('login')) #TODO:and usuario_ctic==True verificar se o usuário foi cadastrado com o acesso do ctic. 
        esta_cadastrado = usuario or UsuarioController.get_by_email(api_response.get('email'))
        if esta_cadastrado:
            return Authorization.get_token(usuario.login), 200
        
        return api_response, 200





