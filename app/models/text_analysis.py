from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TextAnalysis(Base):
    __tablename__ = 'text_analyses'
    
    id = Column(Integer, primary_key=True)
    original_text = Column(Text, nullable=False)
    word_count = Column(Integer, nullable=False)
    character_count = Column(Integer, nullable=False)
    sentence_count = Column(Integer, nullable=False)
    paragraph_count = Column(Integer, nullable=False)
    longest_words = Column(String, nullable=True)