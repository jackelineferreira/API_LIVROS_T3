# 📚 API de Livros - Projeto Flask

Este projeto é uma **API RESTful simples** desenvolvida com **Python** e **Flask** que permite gerenciar um acervo de livros. Ele permite **cadastrar, listar, atualizar e deletar livros** armazenados em um banco de dados SQLite. É ideal para fins educacionais, estudo de APIs e integração com front-end.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11+**
- **Flask** - Framework web leve para criação de APIs.
- **Flask-CORS** - Permite que o front-end se comunique com a API sem bloqueios de CORS.
- **Flask SQLAlchemy** - ORM (Object Relational Mapper) para interagir com o banco de dados.
- **SQLite** - Banco de dados local simples e leve.
- **Postman** - Para testar as rotas da API.

---

## 📁 Estrutura do Projeto

```
Projeto/
│
├── app.py               # Arquivo principal que inicializa a aplicação
├── routes.py            # Arquivo que contém todas as rotas da API
├── models.py            # Define o modelo (tabela) Livro
├── database.py          # Configuração da conexão com o banco de dados
├── requirements.txt     # Dependências do projeto
└── templates/           # (opcional) Diretório para templates HTML
```

---

## 🛠️ Configuração do Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
python app.py
```

A aplicação ficará disponível em `http://127.0.0.1:5000`

---

## 🔁 Rotas da API

### ✔️ `GET /livros`
Lista todos os livros cadastrados.

### ➕ `POST /livros`
Adiciona um novo livro.

**JSON de exemplo:**
```json
{
  "titulo": "A Menina que Roubava Livros",
  "categoria": "Ficção",
  "autor": "Markus Zusak",
  "imagem_url": "https://link-da-imagem.jpg"
}
```

### ✏️ `PUT /livros/<id>`
Atualiza as informações de um livro.

**Exemplo:** `/livros/2`

### ❌ `DELETE /livros/<id>`
Deleta um livro do banco de dados.

---

## 🧪 Testando no Postman

1. Abra o Postman.
2. Use a URL base: `http://127.0.0.1:5000/livros`
3. Teste as rotas usando os métodos **GET, POST, PUT, DELETE**
4. Certifique-se de estar usando **JSON no corpo das requisições**.

---

## 🖼️ Como as imagens funcionam?

A propriedade `imagem_url` aceita uma URL para exibir a imagem da capa do livro no front-end (quando implementado).
---

## 🤔 Por que essa arquitetura foi escolhida?

- **Blueprints (routes.py)**: ajudam a manter o código organizado e modular.
- **SQLAlchemy ORM**: evita escrever SQL manual e melhora a manutenção.
- **CORS**: habilitado para facilitar a conexão com front-ends locais.
- **SQLite**: fácil de configurar e ideal para projetos simples e de estudo.
- **CRUD completo**: cobre todas as operações básicas para gerenciar recursos.

---

## 👩‍💻 Desenvolvido por

Jackeline  
Estudante - Desenvolvimento FullStack: VAI NA WEB
Apaixonada por tecnologia, inovação e soluções que facilitam a vida das pessoas.