from app import api
from app import AuthorizationResource, AuthorizationBotResource
from app import UsuarioResource, ListaUsuarioResource
from app import DocenteResource, ListaDocenteResource, DocenteVacinacaoResource
from app import DiscenteResource, ListaDiscenteResource, DiscenteVacinacaoResource
from app import ListaDiscenteVacinacaoResource
from app import TecnicoResource, ListaTecnicoResource, TecnicoVacinacaoResource
from app import DirecaoResource, ListaDirecaoResource
from app import CoordenacaoResource, ListaCoordenacaoResource
from app import CursoResource, ListaCursoResource
from app import DisciplinaResource, ListaDisciplinaResource
from app import CampusInstitutoResource, ListaCampusInstitutoResource
from app import SolicitacaoAcessoResource, ListaSolicitacaoAcessoResource, SolicitacaoAcessoQuantidadePorCampusResource
from app import SolicitacaoAcessoQuantidadePorRecursoCampusResource, SolicitacaoAcessoPorCursoResource, SolicitacaoDisciplina
from app import AcessoPermitidoResource, ListaAcessoPermitidoResource
from app import RecursoCampusResource, ListaRecursoCampusResource
from app import ProtocoloResource, ListaProtocolosResource
from app import PontoVerificacaoResource, ListaPontoVerificacaoResource
from app import NotificacaoCovidResource, ListaNotificacaoCovidResource
from app import PortariaResource, ListaPortariaResource
from app import HomeResource
from app import OAuth2LoginResource
from app.resources.discente_resource import DiscenteVacinadosPorCursoResource
from app.resources.notificacao_covid_resource import NotificacaoCovidQuantidadePorCampusResource, NotificacaoCovidQuantidadePorCursoResource

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
adicionar_recurso(TecnicoVacinacaoResource)

adicionar_recurso(SolicitacaoAcessoResource)
adicionar_recurso(ListaSolicitacaoAcessoResource)
adicionar_recurso(SolicitacaoAcessoQuantidadePorCampusResource)
adicionar_recurso(SolicitacaoAcessoQuantidadePorRecursoCampusResource)
adicionar_recurso(SolicitacaoAcessoPorCursoResource)
adicionar_recurso(SolicitacaoDisciplina)

adicionar_recurso(AcessoPermitidoResource)
adicionar_recurso(ListaAcessoPermitidoResource)

adicionar_recurso(DiscenteResource)
adicionar_recurso(ListaDiscenteResource)
adicionar_recurso(DiscenteVacinacaoResource)
adicionar_recurso(DiscenteVacinadosPorCursoResource)
adicionar_recurso(ListaDiscenteVacinacaoResource)

adicionar_recurso(RecursoCampusResource)
adicionar_recurso(ListaRecursoCampusResource)

adicionar_recurso(CampusInstitutoResource)
adicionar_recurso(ListaCampusInstitutoResource)

adicionar_recurso(DocenteResource)
adicionar_recurso(ListaDocenteResource)
adicionar_recurso(DocenteVacinacaoResource)

adicionar_recurso(CursoResource)
adicionar_recurso(ListaCursoResource)

adicionar_recurso(ProtocoloResource)
adicionar_recurso(ListaProtocolosResource)

adicionar_recurso(DisciplinaResource)
adicionar_recurso(ListaDisciplinaResource)

adicionar_recurso(PontoVerificacaoResource)
adicionar_recurso(ListaPontoVerificacaoResource)

adicionar_recurso(NotificacaoCovidResource)
adicionar_recurso(ListaNotificacaoCovidResource)
adicionar_recurso(NotificacaoCovidQuantidadePorCampusResource)
adicionar_recurso(NotificacaoCovidQuantidadePorCursoResource)

adicionar_recurso(PortariaResource)
adicionar_recurso(ListaPortariaResource)

adicionar_recurso(OAuth2LoginResource)

# Objeto flask que será obtido para realizar o deploy na AWS
# Ele está localizado abaixo dos recursos para ser
# obtido depois que os recursos são adicionados
application = api.app

if __name__=='__main__':

    # application.debug = True
    application.run(host="0.0.0.0")
