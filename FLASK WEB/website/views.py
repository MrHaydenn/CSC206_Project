from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import pandas as pd

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)



df = pd.read_csv("richathletes.csv")
df.to_csv("richathletes.csv")
@views.route('/table')
@login_required
def table():
    data = pd.read_csv("richathletes.csv")
    return render_template("table.html", tables=[data.to_html()], titles=[''], user=current_user)


@views.route('/primesProgram')
@login_required
def primesProgram():
    return render_template("primesProgram.html", user=current_user)
















