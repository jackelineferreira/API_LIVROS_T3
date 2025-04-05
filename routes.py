from flask import Blueprint, request, jsonify
from database import db
from models import Livro

bp = Blueprint('livros', __name__)

# tabela no banco de dados
@bp.before_app_request
def create_tables():
    db.create_all()
    

@bp.route("/", methods=["GET"])
def pagina_inicial():
    return jsonify({
        "mensagem": "📚 Bem-vindo à nossa Biblioteca Virtual! Doe um livro e compartilhe conhecimento."
    }), 200

# listar todos os livros
@bp.route("/livros", methods=["GET"])
def listar_livros():
    livros = Livro.query.all()
    return jsonify([{
        "id": livro.id,
        "titulo": livro.titulo,
        "categoria": livro.categoria,
        "autor": livro.autor,
        "imagem_url": livro.imagem_url
    } for livro in livros]), 200

# adicionar um novo livro
@bp.route("/doar", methods=["POST"])
def doar_livro():
    dados = request.get_json()
    novo_livro = Livro(
        titulo=dados["titulo"],
        categoria=dados["categoria"],
        autor=dados["autor"],
        imagem_url=dados["imagem_url"]
    )
    db.session.add(novo_livro)
    db.session.commit()
    return jsonify({"mensagem": "Livro adicionado com sucesso!"}), 201

@bp.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    dados = request.get_json()
    livro = Livro.query.get(id)

    if not livro:
        return jsonify({"mensagem": "Livro não encontrado"}), 404

    livro.titulo = dados.get("titulo", livro.titulo)
    livro.categoria = dados.get("categoria", livro.categoria)
    livro.autor = dados.get("autor", livro.autor)
    livro.imagem_url = dados.get("imagem_url", livro.imagem_url)

    db.session.commit()
    return jsonify({"mensagem": "Livro atualizado com sucesso!"}), 200

@bp.route("/livros/<int:id>", methods=["DELETE"])
def deletar_livro(id):
    livro = Livro.query.get(id)

    if not livro:
        return jsonify({"mensagem": "Livro não encontrado"}), 404

    db.session.delete(livro)
    db.session.commit()
    return jsonify({"mensagem": "Livro deletado com sucesso!"}), 200