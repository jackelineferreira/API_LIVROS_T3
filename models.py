from database import db

class Livro(db.Model):
    __tablename__ = 'livros'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)