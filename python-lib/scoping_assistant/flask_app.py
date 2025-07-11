"""
Flask application for the Scoping Assistant plugin.
Provides REST API endpoints for the frontend.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import dataiku
from .api_handlers import (
    generate_summary,
    fetch_similar_documents,
    generate_service_days,
    generate_assumptions,
    fetch_use_cases,
    generate_blueprints,
    analyze_inputs,
    analyze_transcripts,
    generate_scoping_questions
)


def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    CORS(app)
    
    # Get webapp configuration
    try:
        webapp_config = dataiku.get_webapp_config()
    except Exception:
        # Fallback configuration for development
        webapp_config = {
            "enable_mock_data": True,
            "processing_delay": 3,
            "enable_logging": False
        }
    
    @app.route('/api/hello', methods=['GET'])
    def hello():
        return {"message": "Hello from Scoping Assistant"}

    @app.route('/api/generate-summary', methods=['POST'])
    def generate_summary_endpoint():
        data = request.get_json()
        summary = generate_summary(data)
        return jsonify({
            'status': 'success',
            'message': 'Summary generated successfully',
            'data': {
                'summary': summary
            }
        })

    @app.route('/api/fetch-similar-docs', methods=['POST'])
    def fetch_similar_docs_endpoint():
        data = request.get_json()
        similar_docs = fetch_similar_documents(data)
        return jsonify({
            'status': 'success',
            'message': 'Similar documents fetched successfully',
            'data': {
                'similar_docs': similar_docs
            }
        })

    @app.route('/api/generate-service-days', methods=['POST'])
    def generate_service_days_endpoint():
        data = request.get_json()
        service_days = generate_service_days(data)
        return jsonify({
            'status': 'success',
            'message': 'Service days generated successfully',
            'data': {
                'service_days': service_days
            }
        })

    @app.route('/api/generate-assumptions', methods=['POST'])
    def generate_assumptions_endpoint():
        data = request.get_json()
        assumptions = generate_assumptions(data)
        return jsonify({
            'status': 'success',
            'message': 'Assumptions generated successfully',
            'data': {
                'assumptions': assumptions
            }
        })

    @app.route('/api/fetch-use-cases', methods=['POST'])
    def fetch_use_cases_endpoint():
        data = request.get_json()
        use_cases = fetch_use_cases(data)
        return jsonify({
            'status': 'success',
            'message': 'Use cases fetched successfully',
            'data': {
                'use_cases': use_cases
            }
        })

    @app.route('/api/generate-blueprints', methods=['POST'])
    def generate_blueprints_endpoint():
        data = request.get_json()
        selected_use_cases = data.get('selected_use_cases', [])
        blueprints = generate_blueprints(selected_use_cases)
        return jsonify({
            'status': 'success',
            'message': 'Blueprints generated successfully',
            'data': {
                'blueprints': blueprints
            }
        })

    @app.route('/api/scoping/analyze-inputs', methods=['POST'])
    def analyze_inputs_endpoint():
        data = request.get_json()
        analysis = analyze_inputs(data)
        return jsonify({
            'status': 'success',
            'message': 'Inputs analyzed successfully',
            'data': {
                'analysis': analysis
            }
        })

    @app.route('/api/scoping/analyze-transcripts', methods=['POST'])
    def analyze_transcripts_endpoint():
        data = request.get_json()
        analysis = analyze_transcripts(data)
        return jsonify({
            'status': 'success',
            'message': 'Transcripts analyzed successfully',
            'data': {
                'analysis': analysis
            }
        })

    @app.route('/api/scoping/generate-questions', methods=['POST'])
    def generate_scoping_questions_endpoint():
        data = request.get_json()
        questions = generate_scoping_questions(data)
        return jsonify({
            'status': 'success',
            'message': 'Scoping questions generated successfully',
            'data': {
                'questions': questions
            }
        })

    @app.route('/api/config', methods=['GET'])
    def get_config():
        """Endpoint to get webapp configuration"""
        return jsonify({
            'status': 'success',
            'data': {
                'config': webapp_config
            }
        })

    return app 