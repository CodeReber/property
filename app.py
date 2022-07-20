from flask import Flask, jsonify, request, redirect, url_for, render_template
from sqlalchemy import create_engine, func
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)