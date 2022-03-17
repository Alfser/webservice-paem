from ..database import db
from .base_model import BaseHasUsuarioAndDiscenteModel

db.Table(
        'disciplina_has_discente',
        db.Column('disciplina_id_disciplina', db.Integer, db.ForeignKey('disciplina.id_disciplina'), primary_key=True), 
        db.Column('discente_id_discente', db.Integer, db.ForeignKey('discente.id_discente'), primary_key=True),
        db.Column('data', db.Date, nullable=False)
)

class DisciplinaModel(BaseHasUsuarioAndDiscenteModel, db.Model):
    __tablename__='disciplina'

    id_disciplina = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    codigo_sigaa = db.Column(db.String(45), nullable=False)
    semestre = db.Column(db.Integer, nullable=True)
    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)
    docente_id_docente = db.Column(db.Integer, db.ForeignKey('docente.id_docente'), nullable=True)
    discentes = db.relationship('DiscenteModel', secondary='disciplina_has_discente', lazy='select', backref=db.backref('disciplinas', lazy='select'))
    docente = db.relationship('DocenteModel', uselist=False, lazy='select', backref=db.backref('disciplinas', lazy='select'))
    
    def serialize(self):  
        
        return {
            "id_disciplina":self.id_disciplina,
            "nome":self.nome,
            "codigo_sigaa":self.codigo_sigaa,
            "semestre":self.semestre,
            "curso_id_curso":self.curso_id_curso,
            "docente_id_docente":self.docente_id_docente,
            "solicitacoes_acessos":[solicitacao_acesso.serialize() for solicitacao_acesso in self.solicitacoes_acessos]
        }

    def __repr__(self):
        return '<disciplina %r>' % self.nome
