from flask import Flask
from flask_cors import CORS  # type: ignore
from database import db
from routes import bp

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///livros.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)