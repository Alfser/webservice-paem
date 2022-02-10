from ..database import db
from .base_model import BaseListaDisciplina

db.Table(
        'disciplina_has_discente',
        db.Column('disciplina_id_disciplina', db.Integer, db.ForeignKey('disciplina.id_disciplina'), primary_key=True), 
        db.Column('discente_id_discente', db.Integer, db.ForeignKey('discente.id_discente'), primary_key=True),
        db.Column('data', db.Date, nullable=False)
)

class DisciplinaModel(BaseListaDisciplina, db.Model):
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
            "discentes":[discente.serialize_to_list() for discente in self.discentes]
        }

    @classmethod
    def query_all_names(cls, 
            campus_instituto_id_campus_instituto=None, 
            docente_id_docente=None
            ): 
        return super().query_all_names(
            cls.nome.label("nome"), 
            cls.id_disciplina.label("id"),
            cls.semestre.label("semestre"),
            cls.codigo_sigaa.label("codigo_sigaa"),
            campus_instituto_id_campus_instituto=campus_instituto_id_campus_instituto,
            docente_id_docente=docente_id_docente
        )

    def __repr__(self):
        return '<disciplina %r>' % self.nome
