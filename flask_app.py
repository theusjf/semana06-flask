from flask import Flask, render_template_string
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def home():
    current_time = datetime.utcnow()
    html_template = '''
    {% extends "bootstrap/base.html" %}

    {% block title %}Flasky{% endblock %}

    {% block navbar %}
    <div class="navbar navbar-inverse" role="navigation">
        <div class="container">
            <a class="navbar-brand" href="/">Flasky</a>
            <a class="navbar-brand" href="/">Home</a>
        </div>
    </div>
    {% endblock %}

    {% block content %}
    <div class="container">
        <h1>Hello World!</h1>
        <hr>
        <p>The local date and time is {{ moment(current_time).format('LLL') }}.</p>
        <p>That was {{ moment(current_time).fromNow(refresh=True) }}.</p>
    </div>
    {% endblock %}

    {% block scripts %}
    {{ super() }}
    {{ moment.include_moment() }}
    {% endblock %}
    '''
    return render_template_string(html_template, current_time=current_time)

@app.route('/user/<name>')
def identificacao(name):

    html_template = '''
    {% extends "bootstrap/base.html" %}

    {% block title %}Ident{% endblock %}

    {% block navbar %}
    <div class="navbar navbar-inverse" role="navigation">
        <div class="container">
            <a class="navbar-brand" href="/">Flasky</a>
            <a class="navbar-brand" href="/">Home</a>
        </div>
    </div>
    {% endblock %}

    {% block content %}
    <div class="container">
        <h1>Hello, {{ name }}!</h1>
        <hr>
    </div>
    {% endblock %}
    '''

    return render_template_string(html_template, name=name)

@app.errorhandler(404)
def page_not_found(e):

    html_template = '''
    {% extends "bootstrap/base.html" %}

    {% block title %}404{% endblock %}

    {% block navbar %}
    <div class="navbar navbar-inverse" role="navigation">
        <div class="container">
            <a class="navbar-brand" href="/">Flasky</a>
            <a class="navbar-brand" href="/">Home</a>
        </div>
    </div>
    {% endblock %}

    {% block content %}
    <div class="container">
        <h1>Not Found</h1>
        <hr>
    </div>
    {% endblock %}
    '''

    return render_template_string(html_template), 404
