from app import app, init_db

def test_agent_query():
    init_db()

    with app.test_client() as client:
        response = client.post(
            "/api/agent/query",
            json={"prompt": "Tell me about Crocine"}
        )

        assert response.status_code == 200
