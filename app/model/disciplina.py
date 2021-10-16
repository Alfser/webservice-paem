from ..database import db
from .base_model import BaseHasCurso

db.Table(
        'disciplina_has_discente',
        db.Column('disciplina_id_disciplina', db.Integer, db.ForeignKey('disciplina.id_disciplina'), primary_key=True), 
        db.Column('discente_id_discente', db.Integer, db.ForeignKey('discente.id_discente'), primary_key=True),
        db.Column('data', db.Date, nullable=False)
)

class DisciplinaModel(BaseHasCurso, db.Model):
    __tablename__='disciplina'

    id_disciplina = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    codigo_sigaa = db.Column(db.String(45), nullable=False)
    semestre = db.Column(db.Integer, nullable=True)

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)

    discentes = db.relationship('DiscenteModel', secondary='disciplina_has_discente', lazy='select', backref=db.backref('disciplinas', lazy='select'))

    def serialize(self):    
        return {
            "id_disciplina":self.id_disciplina,
            "nome":self.nome,
            "codigo_sigaa":self.codigo_sigaa,
            "semestre":self.semestre,
            "curso_id_curso":self.curso_id_curso
        }

    @classmethod
    def query_all_names(cls, curso_id_curso=None):
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_disciplina.label("id"),
            curso_id_curso 
        )

    def __repr__(self):
        return '<disciplina %r>' % self.login

    
