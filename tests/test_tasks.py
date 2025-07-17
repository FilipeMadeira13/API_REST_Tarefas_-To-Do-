from fastapi import status
from fastapi.testclient import TestClient


def test_create_task(client: TestClient):
    response = client.post(
        "/tasks/",
        json={"title": "Estudar Python", "description": "Aprender FastAPI e SQLModel"},
    )
    data = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert data["title"] == "Estudar Python"
    assert data["description"] == "Aprender FastAPI e SQLModel"
    assert data["completed"] is False
    assert "id" in data


def test_get_tasks(client: TestClient):
    client.post(
        "/tasks/",
        json={
            "title": "Tarefa Temporária",
            "description": "Aprender FastAPI e SQLModel",
        },
    )

    response = client.get("/tasks/")
    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Tarefa Temporária"


def test_get_task_success(client: TestClient):
    create_response = client.post(
        "/tasks/",
        json={
            "title": "Tarefa de Teste",
            "description": "Descrição da tarefa de teste",
        },
    )
    created_task = create_response.json()
    task_id = created_task["id"]
    response = client.get(f"/tasks/{task_id}")
    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert data["id"] == task_id
    assert data["title"] == "Tarefa de Teste"
    assert data["description"] == "Descrição da tarefa de teste"
    assert data["completed"] is False


def test_get_task_not_found(client: TestClient):
    response = client.get("/tasks/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Tarefa não encontrada" in response.json()["detail"]


def test_update_task_success(client: TestClient):
    create_response = client.post(
        "/tasks/",
        json={"title": "Tarefa Original", "description": "Descrição original"},
    )
    created_task = create_response.json()
    task_id = created_task["id"]

    update_data = {
        "title": "Tarefa Atualizada",
        "description": "Descrição atualizada",
        "completed": True,
    }
    response = client.put(f"/tasks/{task_id}", json=update_data)
    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert data["id"] == task_id
    assert data["title"] == "Tarefa Atualizada"
    assert data["description"] == "Descrição atualizada"
    assert data["completed"] is True


def test_update_task_partial_update(client: TestClient):
    create_response = client.post(
        "/tasks/",
        json={"title": "Tarefa Para Atualizar", "description": "Descrição inicial"},
    )
    created_task = create_response.json()
    task_id = created_task["id"]

    update_data = {"title": "Novo Título"}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert data["id"] == task_id
    assert data["title"] == "Novo Título"
    assert data["description"] == "Descrição inicial"
    assert data["completed"] is False


def test_delete_task_success(client: TestClient):
    create_response = client.post(
        "/tasks/",
        json={"title": "Tarefa Para Deletar", "description": "Será deletada"},
    )
    created_task = create_response.json()
    task_id = created_task["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == status.HTTP_204_NO_CONTENT

    get_response = client.get(f"/tasks/{task_id}")

    assert get_response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_task_not_found(client: TestClient):
    response = client.delete("/tasks/999")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Tarefa não encontrada" in response.json()["detail"]
