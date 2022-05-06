from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import pandas as pd
import csv


views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)



df = pd.read_csv("richathletes.csv")
df.to_csv("richathletes.csv", index=False)
@views.route('/table')
@login_required
def table():
    data = pd.read_csv("richathletes.csv")
    return render_template("table.html", tables=[data.to_html()], titles=[''], user=current_user)

#from primes import results, found
@views.route('/primesProgram', methods = ['POST',"GET"])
@login_required
def primesProgram():
    results = request.form.to_dict()

    return render_template("primesProgram.html", user=current_user, results = results)


@views.route('/graph')
@login_required
def graph():
    return render_template("graph.html", user=current_user)
















