from .resources import AuthorizationResource, AuthorizationBotResource
from .resources import UsuarioResource, ListaUsuarioResource
from .resources import DocenteResource, ListaDocenteResource
from .resources import DiscenteResource, ListaDiscenteResource
from .resources import TecnicoResource, ListaTecnicoResource
from .resources import DirecaoResource, ListaDirecaoResource
from .resources import CoordenacaoResource, ListaCoordenacaoResource
from .resources import CursoResource, ListaCursoResource
from .resources import DisciplinaResource, ListaDisciplinaResource
from .resources import CampusInstitutoResource, ListaCampusInstitutoResource
from .resources import SolicitacaoAcessoResource, ListaSolicitacaoAcessoResource
from .resources import AcessoPermitidoResource, ListaAcessoPermitidoResource
from .resources import RecursoCampusResource, ListaRecursoCampusResource
from .resources import ProtocoloResource, ListaProtocolosResource
from .resources import DiscenteVacinacaoResource
from .resources import PontoVerificacaoResource, ListaPontoVerificacaoResource
from .resources import DisciplinaResource, ListaDisciplinaResource
from .resources import HomeResource

from .resources import app

from flask_restful import Api

api = Api(app)
api.prefix = '/api.paem'
