from ..database import db


db.Table(
        'disciplina_has_discente',
        db.Column('disciplina_id_disciplina', db.Integer, db.ForeignKey('disciplina.id_disciplina'), primary_key=True), 
        db.Column('discente_id_discente', db.Integer, db.ForeignKey('discente.id_discente'), primary_key=True),
        db.Column('data', db.Date, nullable=False)
)

class DisciplinaModel(db.Model):
    __tablename__='disciplina'

    id_disciplina = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(45), nullable=False)
    codigo_sigaa = db.Column(db.String(45), nullable=False)
    semestre = db.Column(db.Integer, nullable=True)

    curso_id_curso = db.Column(db.Integer, db.ForeignKey('curso.id_curso'), nullable=True)

    discentes = db.relationship('DiscenteModel', secondary='disciplina_has_discente', lazy='subquery', backref=db.backref('disciplinas', lazy=True))

    def __init__(self, nome, codigo_sigaa, semestre=None, id_disciplina=None):
        self.id_disciplina = id_disciplina
        self.nome = nome
        self.codigo_sigaa = codigo_sigaa
        self.semestre = semestre

    def serialize(self):

        discentes_dict = self.discentes.seriaize()

        return {
            "id_disciplina":self.id_disciplina,
            "nome":self.nome,
            "codigo_sigaa":self.codigo_sigaa,
            "semestre":self.semestre,
            'discentes': discentes_dict if discentes_dict else 'nenhum registro' 
        }

    @classmethod
    def query_all_names(cls):
        return super().query_all_names(cls.nome, cls.id_tecnico)

    def __repr__(self):
        return '<disciplina %r>' % self.login

    
