from ..controller import app
from .authorization_resource import AuthorizationResource, AuthorizationBotResource
from .usuario_resource import UsuarioResource, ListaUsuarioResource
from .docente_resource import DocenteResource, ListaDocenteResource, DocenteVacinacaoResource
from .discente_resource import DiscenteResource, ListaDiscenteResource, DiscenteVacinacaoResource
from .tecnico_resource import TecnicoResource, ListaTecnicoResource, TecnicoVacinacaoResource
from .direcao_resource import DirecaoResource, ListaDirecaoResource
from .coordenacao_resource import CoordenacaoResource, ListaCoordenacaoResource
from .curso_resource import CursoResource, ListaCursoResource
from .campus_instituto_resource import CampusInstitutoResource, ListaCampusInstitutoResource
from .solicitacao_acesso_resource import SolicitacaoAcessoResource, ListaSolicitacaoAcessoResource
from .acesso_permitido_resource import AcessoPermitidoResource, ListaAcessoPermitidoResource
from .recurso_campus_resource import RecursoCampusResource, ListaRecursoCampusResource
from .reserva_recurso_servidor_resource import ReservaRecursoServidorResource, ListaReservaRecursoServidorResource
from .protocolo_resource import ProtocoloResource, ListaProtocolosResource
from .ponto_verificacao_resource import PontoVerificacaoResource, ListaPontoVerificacaoResource
from .disciplina_resource import DisciplinaResource, ListaDisciplinaResource
from .home import HomeResource