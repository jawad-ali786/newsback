from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///NewsScrapping.db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from ScrapeNews import routes