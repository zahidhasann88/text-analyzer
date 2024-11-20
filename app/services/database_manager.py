from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import Config
from app.models.text_analysis import Base, TextAnalysis
import json

class DatabaseManager:
    def __init__(self, db_url=Config.SQLALCHEMY_DATABASE_URI):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def save_analysis(self, text, analysis_results):
        session = self.Session()
        try:
            text_analysis = TextAnalysis(
                original_text=text,
                word_count=analysis_results['word_count'],
                character_count=analysis_results['character_count'],
                sentence_count=analysis_results['sentence_count'],
                paragraph_count=analysis_results['paragraph_count'],
                longest_words=json.dumps(analysis_results['longest_words'])
            )
            session.add(text_analysis)
            session.commit()
            return text_analysis.id
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()