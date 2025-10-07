import requests
import pytest

BASE_URL = "https://httpbin.org"


# CREATE (POST)
def test_create_user():
    url = f"{BASE_URL}/post"
    payload = {
        "id": 101,
        "name": "Dhas",
        "age": 25,
        "role": "QA Engineer"
    }
    response = requests.post(url, json=payload)

    assert response.status_code == 200
    data = response.json()

    # Validate the JSON echoed by httpbin.org
    assert data["json"]["name"] == "Dhas"
    assert data["json"]["age"] == 25
    assert data["json"]["role"] == "QA Engineer"
    print("\n POST (Create User):", data["json"])


# READ (GET)
def test_get_user():
    url = f"{BASE_URL}/get"
    params = {"id": 101, "name": "Dhas"}
    response = requests.get(url, params=params)

    assert response.status_code == 200
    data = response.json()

    assert data["args"]["id"] == "101"
    assert data["args"]["name"] == "Dhas"
    print("\n GET (Read User):", data["args"])



# UPDATE (PUT)
def test_update_user():
    url = f"{BASE_URL}/put"
    payload = {
        "id": 101,
        "name": "Dhas",
        "age": 26,
        "role": "Senior QA Engineer"
    }

    response = requests.put(url, json=payload)
    assert response.status_code == 200
    data = response.json()

    assert data["json"]["age"] == 26
    assert data["json"]["role"] == "Senior QA Engineer"
    print("\n PUT (Update User):", data["json"])


# Partial update on role(PATCH)
def test_patch_user():
    url = f"{BASE_URL}/patch"
    payload = {
        "role": "QA Lead"
    }

    response = requests.patch(url, json=payload)
    assert response.status_code == 200
    data = response.json()

    assert data["json"]["role"] == "QA Lead"
    print("\n PATCH (Partial Update):", data["json"])


# DELETE USER
def test_delete_user():
    url = f"{BASE_URL}/delete"
    params = {"id": 101}

    response = requests.delete(url, params=params)
    assert response.status_code == 200
    data = response.json()

    assert data["args"]["id"] == "101"
    print("\n DELETE (Remove User):", data["args"])
