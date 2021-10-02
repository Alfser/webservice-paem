from app import api
from app import AuthorizationResource, AuthorizationBotResource
from app import UsuarioResource, ListaUsuarioResource
from app import DocenteResource, ListaDocenteResource
from app import DiscenteResource, ListaDiscenteResource
from app import TecnicoResource, ListaTecnicoResource
from app import DirecaoResource, ListaDirecaoResource
from app import CoordenacaoResource, ListaCoordenacaoResource
from app import CursoResource, ListaCursoResource
from app import DisciplinaResource, ListaDisciplinaResource
from app import CampusInstitutoResource, ListaCampusInstitutoResource
from app import SolicitacaoAcessoResource, ListaSolicitacaoAcessoResource
from app import AcessoPermitidoResource, ListaAcessoPermitidoResource
from app import RecursoCampusResource, ListaRecursoCampusResource
from app import ProtocoloResource, ListaProtocolosResource
from app import DiscenteVacinacaoResource
from app import HomeResource

# Just to aws know the variable of flask app.

def adicionar_recurso(Recurso):
    api.add_resource(Recurso, Recurso.ROUTE, endpoint=Recurso.ENDPOINT)

adicionar_recurso(HomeResource)
    # Login and get token
adicionar_recurso(AuthorizationResource)
adicionar_recurso(AuthorizationBotResource)

adicionar_recurso(UsuarioResource)
adicionar_recurso(ListaUsuarioResource)

adicionar_recurso(TecnicoResource)
adicionar_recurso(ListaTecnicoResource)

adicionar_recurso(SolicitacaoAcessoResource)
adicionar_recurso(ListaSolicitacaoAcessoResource)

adicionar_recurso(AcessoPermitidoResource)
adicionar_recurso(ListaAcessoPermitidoResource)

adicionar_recurso(DiscenteResource)
adicionar_recurso(ListaDiscenteResource)

adicionar_recurso(RecursoCampusResource)
adicionar_recurso(ListaRecursoCampusResource)

adicionar_recurso(CampusInstitutoResource)
adicionar_recurso(ListaCampusInstitutoResource)

adicionar_recurso(DocenteResource)
adicionar_recurso(ListaDocenteResource)

adicionar_recurso(CursoResource)
adicionar_recurso(ListaCursoResource)

adicionar_recurso(ProtocoloResource)
adicionar_recurso(ListaProtocolosResource)

adicionar_recurso(DiscenteVacinacaoResource)

# Objeto flask que será obtido para realizar o deploy na AWS
# Ele está localizado abaixo dos recursos para ser
# obtido depois que os recursos são adicionados
application = api.app


if __name__=='__main__':

    # application.debug = True
    application.run()
