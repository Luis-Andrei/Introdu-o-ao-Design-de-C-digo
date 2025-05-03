from flask import Blueprint, request, jsonify
from services.calculator_4_service import calculate_average

calculator_4 = Blueprint('calculator_4', __name__)

@calculator_4.route('/calculator_4', methods=['POST'])
def average():
    try:
        data = request.get_json()
        
        if not data or 'numbers' not in data:
            return jsonify({'error': 'A lista de números é obrigatória'}), 400
            
        numbers = data['numbers']
        
        if not isinstance(numbers, list):
            return jsonify({'error': 'O campo numbers deve ser uma lista'}), 400
            
        if not numbers:
            return jsonify({'error': 'A lista de números não pode estar vazia'}), 400
            
        result = calculate_average(numbers)
        return jsonify({'average': result}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500 