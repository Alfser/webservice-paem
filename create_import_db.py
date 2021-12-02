
# import models to create tables
from app.model import UsuarioModel
from app.model import CursoModel
from app.model import CampusInstitutoModel
from app.model import DiscenteModel
from app.model import TecnicoModel
from app.model import DocenteModel
from app.model import DirecaoModel
from app.model import CoordenacaoModel
from app.model import RecursoCampusModel
from app.model import SolicitacaoAcessoModel
from app.model import AcessoPermitidoModel
from app.model import PortariaModel
from app.model import ReservaRecursoServidoresModel
from app.model import ProtocoloModel
from app.model import PontoVerificacaoModel

from app.database import create_db, db
# libs
from datetime import time, date
from pandas import DataFrame, read_csv
import numpy as np

from app.model.disciplina import DisciplinaModel

def dicts2db(dicts, Model):

    models = list()
    for row in dicts:
        objectModel = Model(**row)
        models.append(objectModel)
    
    db.session.add_all(models)

def import_csv_db():

    campus_dicts = read_csv('app/database/inputs/campus_instituto.csv', parse_dates=["ano_fundacao"], na_filter=True, sep=';', encoding='UTF-8').replace([np.nan], [None]).to_dict(orient='records')
    curso_dicts = read_csv('app/database/inputs/curso.csv', parse_dates=["data_fundacao"], na_filter=True, sep=';', encoding='UTF-8').replace([np.nan], [None]).to_dict(orient='records')
    discente_dicts = read_csv('app/database/inputs/discente.csv', na_filter=True, sep=';', encoding='UTF-8').replace(np.nan, None).replace([np.nan], [None]).to_dict(orient='records')
    docente_dicts = read_csv('app/database/inputs/docente.csv', parse_dates=["data_nascimento"], na_filter=True, sep=';', encoding='UTF-8').replace([np.nan], [None]).to_dict(orient='records')
    recurso_campus_dicts = read_csv('app/database/inputs/recurso_campus.csv', parse_dates=["inicio_horario_funcionamento", "fim_horario_funcionamento"], na_filter=True, sep=';', encoding='UTF-8').replace([np.nan], [None]).to_dict(orient='records')
    tecnico_dicts = read_csv('app/database/inputs/tecnico.csv', parse_dates=["data_nascimento"], na_filter=True, sep=';', encoding='UTF-8').replace([np.nan], [None]).to_dict(orient='records')
    usuario_dicts = read_csv('app/database/inputs/usuario.csv', na_filter=True, sep=';', encoding='UTF-8', keep_default_na=False).replace([np.nan], [None]).to_dict(orient='records')
    solicitacao_acesso_dicts = read_csv('app/database/inputs/solicitacao_acesso.csv', parse_dates=["data", "hora_inicio", "hora_fim"], na_filter=True, sep=';', encoding='UTF-8').replace([np.nan], [None]).to_dict(orient='records')
    acesso_permitido_dicts = read_csv('app/database/inputs/acesso_permitido.csv', parse_dates=["hora_entrada", "hora_saida"], na_filter=True, sep=';', encoding='UTF-8').replace([np.nan], [None]).to_dict(orient='records')
    protocolo_dicts = read_csv('app/database/inputs/protocolo.csv', na_filter=True, sep=';', encoding='UTF-8').replace([np.nan], [None]).to_dict(orient='records')
    disciplinas_dicts = read_csv('app/database/inputs/disciplina.csv', na_filter=True, sep=';', encoding='UTF-8').replace([np.nan], [None]).to_dict(orient='records')

    
    # import campus
    dicts2db(campus_dicts, CampusInstitutoModel)

    # import usuario
    dicts2db(usuario_dicts, UsuarioModel)

    # import curso
    dicts2db(curso_dicts, CursoModel)

    # import recurso_campus
    dicts2db(recurso_campus_dicts, RecursoCampusModel)

    # import docente
    dicts2db(docente_dicts, DocenteModel)

    # import discente
    dicts2db(discente_dicts, DiscenteModel)
    
    # import tecnico
    dicts2db(tecnico_dicts, TecnicoModel)
    
    # import solicitacao_acesso
    dicts2db(solicitacao_acesso_dicts, SolicitacaoAcessoModel)
    
    # import acesso_permitido
    dicts2db(acesso_permitido_dicts, AcessoPermitidoModel)
    
    # import PROTOCOLO
    dicts2db(protocolo_dicts, ProtocoloModel)

    # import DISCIPLINA
    dicts2db(disciplinas_dicts, DisciplinaModel)
    
    # if all data fake was added commit all insertions
    db.session.commit()
    

if __name__=='__main__':
    db.app.config['SQLALCHEMY_ECHO'] = True

    create_db()
    import_csv_db()
