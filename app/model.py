from app import db

skillpath_table = db.Table('skillpath_table', db.Model.metadata,
                     db.Column('pathway_id', db.Integer, db.ForeignKey('pathway.id')),
                     db.Column('skill_id',   db.Integer, db.ForeignKey('skill.id'))
                     )


class Pathway (db.Model):
    __tablename__ = "pathway"
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.Unicode)
    description = db.Column('description', db.Unicode)
    create_at = db.Column('create_at', db.Date)
    skills = db.relationship("Skill", secondary=skillpath_table)


class Skill (db.Model):
    __tablename__ = "skill"
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.Unicode)
    description = db.Column('description', db.Unicode)

    def __repr__(self):
        return '<Skill {}>'.format(self.title)


class Attainment (db.Model):
    __tablename__ = "attainment"
    id = db.Column('id', db.Integer, primary_key = True)
    user_id = db.Column('user_id', db.Integer)
    skill_id = db.Column('skill_id', db.Integer, db.ForeignKey('skill.id'))
    level = db.Column('level', db.Integer)
    created_at = db.Column('created_at', db.Date)

    skills = db.relationship('Skill', foreign_keys=skill_id)



