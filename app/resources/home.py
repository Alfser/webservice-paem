from flask_restful import Resource, current_app
from flask import render_template

class HomeResource(Resource):

    ENDPOINT = 'home'
    ROUTE = '/'

    def get(self):  
        return [
            {"home": "Home Pege of PAEM Webservice"},
            {"rotas disponíveis":{
                "autenticacao": ["/auth", "/auth.bot"],
                "usuario": ["/usuarios", "/usuarios/usuario"],
                "discente": ["/discentes", "/discentes/discente"],
                "docente": ["/docentes", "/docentes/docente"],
                "tecnico": ["/tecnicos", "/tecnicos/tecnico"],
                "curso": ["/cursos", "/cursos/curso"],
                "campus": ["/campus", "/campus/campi"],
                "recurso_campus": ["/recursos_campus", "/recursos_campus/recurso_campus"],
                "solicitacao_acesso": ["/solicitacoes_acessos", "/solicitacoes_acessos/solicitacao_acesso"],
                "acesso_permitido": ["/acessos_permitidos", "/acessos_permitidos/acesso_permitido"],
                }
            }
        ]