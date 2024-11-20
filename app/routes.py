from flask import Blueprint, request, jsonify
from app.services.text_analyzer_service import TextAnalyzerService
from app.services.database_manager import DatabaseManager

text_analyzer_bp = Blueprint('text_analyzer', __name__)
db_manager = DatabaseManager()

@text_analyzer_bp.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    analysis_results = {
        'word_count': TextAnalyzerService.count_words(text),
        'character_count': TextAnalyzerService.count_characters(text),
        'sentence_count': TextAnalyzerService.count_sentences(text),
        'paragraph_count': TextAnalyzerService.count_paragraphs(text),
        'longest_words': TextAnalyzerService.find_longest_words(text)
    }
    
    try:
        analysis_id = db_manager.save_analysis(text, analysis_results)
        analysis_results['analysis_id'] = analysis_id
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    return jsonify(analysis_results)