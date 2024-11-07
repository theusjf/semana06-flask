from flask import Flask, render_template, session, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '10105006'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('Informe o seu nome:', validators=[DataRequired()])
    snome = StringField('Informe o seu sobrenome:', validators=[DataRequired()])
    inst = StringField('Informe a sua Instituição de ensino:', validators=[DataRequired()])
    disc = SelectField('Informe a sua disciplina:', choices=[
        ('DSWA5', 'DSWA5'),
        ('DWBA4', 'DWBA4'),
        ('Gestão de Projetos', 'Gestão de Projetos')
    ])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    remote_addr = request.remote_addr;
    remote_host = request.host;
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['snome'] = form.snome.data
        session['inst'] = form.inst.data
        session['disc'] = form.disc.data
        flash('Você alterou seu nome!')

        return redirect(url_for('index'))
    return render_template('index.html', form=form,
                           remote_addr=remote_addr,
                           remote_host=remote_host,
                           current_time=datetime.utcnow(),
                           name=session.get('name'),
                           snome=session.get('snome'),
                           inst=session.get('inst'),
                           disc=session.get('disc'))









