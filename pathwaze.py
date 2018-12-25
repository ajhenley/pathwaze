from app import app, db
from app.model import  Skill, Pathway


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Skill': Skill, 'Pathway': Pathway}
