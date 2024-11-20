# Text Analyzer Project

## Project Overview
A comprehensive Flask-based text analysis application with advanced natural language processing capabilities, database integration, and robust architecture.

## Features
- Advanced text analysis metrics
- Word count and character analysis
- Readability score calculation
- Sentiment analysis
- Word frequency distribution
- JWT authentication
- Database persistence
- Docker containerization

## Technology Stack
- Python 3.8+
- Flask
- SQLAlchemy
- PostgreSQL
- NLTK
- TextBlob
- Docker
- JWT Authentication

## Project Structure
```
text-analyzer/
│
├── app/
│   ├── services/
│   ├── models/
│   ├── routes/
│   └── utils/
│
├── config/
├── tests/
└── requirements.txt
```

## Setup Instructions

### Local Development
```bash
# Clone repository
git clone https://github.com/zahidhasann88/text-analyzer.git
cd text-analyzer

# Create virtual environment
python3 -m venv venv
source venv/bin/activate    #gitbash
venv\Scripts\activate   #cmd
.\venv\Scripts\activate  #powershall

# Install dependencies
pip install -r requirements.txt

# Configure database
createdb textanalyzer

# Run migrations
flask db upgrade

# Start application
python run.py

# test application
pytest tests
```

### Docker Deployment
```bash
# Build and run
docker-compose up --build
```

## API Endpoints
- `POST /api/analyze`: Text analysis endpoint
  - Requires JWT authentication
  - Payload: `{"text": "Sample text to analyze"}`

## Key Analysis Metrics
- Total word count
- Unique words
- Sentence count
- Readability scores
- Word frequency
- Sentiment analysis

## Testing
```bash
# Run tests
pytest tests/

# Check coverage
coverage run -m pytest
coverage report
```

## Authentication
- JWT-based authentication
- Secure token management

## Logging
- Rotating file handlers
- Console and file logging
- Configurable log levels