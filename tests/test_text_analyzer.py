import pytest
from app import create_app
from app.services.text_analyzer_service import TextAnalyzerService

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_word_count():
    text = "The quick brown fox jumps over the lazy dog."
    assert TextAnalyzerService.count_words(text) == 10

def test_character_count():
    text = "The quick brown fox jumps over the lazy dog."
    assert TextAnalyzerService.count_characters(text) == 44

def test_text_analysis_endpoint(client):
    response = client.post('/api/analyze', json={
        'text': 'The quick brown fox jumps over the lazy dog.'
    })
    assert response.status_code == 200
    data = response.get_json()
    assert 'word_count' in data