from .resources import AuthorizationResource, AuthorizationBotResource
from .resources import UsuarioResource, ListaUsuarioResource
from .resources import DocenteResource, ListaDocenteResource, DocenteVacinacaoResource
from .resources import DiscenteResource, ListaDiscenteResource, DiscenteVacinacaoResource
from .resources import ListaDiscenteVacinacaoResource
from .resources import TecnicoResource, ListaTecnicoResource, TecnicoVacinacaoResource
from .resources import DirecaoResource, ListaDirecaoResource
from .resources import CoordenacaoResource, ListaCoordenacaoResource
from .resources import CursoResource, ListaCursoResource
from .resources import DisciplinaResource, ListaDisciplinaResource
from .resources import CampusInstitutoResource, ListaCampusInstitutoResource
from .resources import SolicitacaoAcessoResource, ListaSolicitacaoAcessoResource, SolicitacaoAcessoQuantidadePorCampusResource
from .resources import SolicitacaoAcessoQuantidadePorRecursoCampusResource, SolicitacaoAcessoPorCursoResource
from .resources import SolicitacaoDisciplina
from .resources import AcessoPermitidoResource, ListaAcessoPermitidoResource
from .resources import RecursoCampusResource, ListaRecursoCampusResource
from .resources import ProtocoloResource, ListaProtocolosResource
from .resources import DiscenteVacinacaoResource, DiscenteVacinadosPorCursoResource
from .resources import PontoVerificacaoResource, ListaPontoVerificacaoResource
from .resources import DisciplinaResource, ListaDisciplinaResource
from .resources import NotificacaoCovidResource, ListaNotificacaoCovidResource, NotificacaoCovidQuantidadePorCampusResource, NotificacaoCovidQuantidadePorCursoResource
from .resources import PortariaResource, ListaPortariaResource
from .resources import HomeResource

from .resources import app

from flask_restful import Api

api = Api(app)
api.prefix = '/api.paem'
