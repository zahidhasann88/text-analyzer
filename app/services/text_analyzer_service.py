import re

class TextAnalyzerService:
    @staticmethod
    def count_words(text: str) -> int:
        cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
        return len(cleaned_text.split())
    
    @staticmethod
    def count_characters(text: str) -> int:
        return len(text.replace(' ', ''))
    
    @staticmethod
    def count_sentences(text: str) -> int:
        sentences = re.split(r'[.!?]+', text)
        return len([s for s in sentences if s.strip()])
    
    @staticmethod
    def count_paragraphs(text: str) -> int:
        paragraphs = [p for p in text.split('\n') if p.strip()]
        return len(paragraphs)
    
    @staticmethod
    def find_longest_words(text: str, top_n: int = 5) -> list:
        cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
        words = cleaned_text.split()
        return sorted(set(words), key=len, reverse=True)[:top_n]