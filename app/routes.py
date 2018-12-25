from flask import render_template, redirect, url_for, request
from app import app, db
from app.model import Pathway, Skill
# from requests import request


@app.route('/')
@app.route('/index')
def index():
    pathway = Pathway.query.get(1)
    skill_list = Skill.query.all()
    return render_template('index.html', title='Home', pathway=pathway, skill_list=skill_list)


@app.route('/addskilltopathway', methods=['GET', 'POST'])
def addskilltopathway():
    skill_id = request.form['skill_id']
    pathway_id = request.form['pathway_id']
    s = Skill.query.get(skill_id)
    p = Pathway.query.get(pathway_id)
    p.skills.append(s)
    db.session.add(p)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/removeskillfrompathway/<skill>/<pathway>')
def removeskillfrompathway(skill, pathway):
    s = Skill.query.get(skill)
    p = Pathway.query.get(pathway)
    p.skills.remove(s)
    db.session.add(p)
    db.session.commit()
    return redirect(url_for('index'))

