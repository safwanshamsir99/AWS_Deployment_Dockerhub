from fastapi.testclient import TestClient
from app.main import app
from dotenv import load_dotenv
import json
import os
import sys

load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200, "Response 404, failed"

def test_add():
    response = client.post(
        "/add", 
        headers={"api-key": os.getenv("BACKEND_API_KEY")},
        json={
        "num1": 12.34,
        "num2": 56.78
    })
    assert response.status_code == 200, "Response 404, failed"

    json_data = json.loads(json.dumps(response.json()))
    assert "num3" in json_data

    num3 = json_data["num3"]
    assert isinstance(num3, float)
    assert num3 == 69.12