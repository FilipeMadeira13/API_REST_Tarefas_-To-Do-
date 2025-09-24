# 🧠 API REST de Tarefas (To-Do) com FastAPI

Uma API RESTful simples e eficiente para gerenciamento de tarefas, construída com **FastAPI**, **SQLModel** e **SQLite**, seguindo os princípios da **Clean Architecture** e com cobertura de testes automatizados com **Pytest**.

---

## 🚀 Funcionalidades

- ✅ Criar tarefa (`POST /tasks`)
- 📋 Listar todas as tarefas (`GET /tasks`)
- 🔍 Buscar tarefa por ID (`GET /tasks/{id}`)
- ✏️ Atualizar tarefa (`PUT /tasks/{id}`)
- ❌ Deletar tarefa (`DELETE /tasks/{id}`)

---

## 🧱 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [SQLite](https://www.sqlite.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Pytest](https://docs.pytest.org/)
- [httpx](https://www.python-httpx.org/)

---

---

## ⚙️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/FilipeMadeira13/API_REST_Tarefas_-To-Do-.git
cd API_REST_Tarefas_-To-Do-
```

### 2. Instale as dependências

```bash
poetry install --no-root
```

### 3. Execute a API localmente

```bash
uvicorn app.main:app --reload
```

### 5. Acesse a documentação automática

- [Swagger UI](http://localhost:8000/docs)

- [Redoc](http://localhost:8000/redoc)

## 🧪 Como rodar os testes

```bash
pytest
```

Os testes são executados com um banco de dados em memória (SQLite) para isolamento e performance.

## ✨ Autor

- Carlos Filipe Madeira de Souza
- [GitHub](https://github.com/FilipeMadeira13)
- [LinkedIn](https://www.linkedin.com/in/carlos-filipe-madeira-de-souza-16211922a/)
