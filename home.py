import os
from flask import Flask
import the_periodic_typer_of_elements as typer

app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    return typer.transform('hello world') + '<br><br><a href="typer/type.something.in.the.url.bar">' + typer.transform('click here') + '</a>'

@app.route('/typer/<q>')
def type(q):
    return typer.transform(q)

