from flask import Flask
from config.config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    from app.routes import text_analyzer_bp
    app.register_blueprint(text_analyzer_bp, url_prefix='/api')
    
    return app