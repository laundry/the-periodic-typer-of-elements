import os
from flask import Flask
import the_periodic_typer_of_elements as typer

app = Flask(__name__)

@app.route('/')
def home():
    return typer.transform('hello world')
