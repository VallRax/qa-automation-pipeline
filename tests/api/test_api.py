import requests

def test_api_status():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert response.status_code == 200

def test_api_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert data["id"] == 1