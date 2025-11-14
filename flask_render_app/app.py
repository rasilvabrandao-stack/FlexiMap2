from flask import Flask, jsonify, request
from supabase import create_client, Client
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Supabase setup
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/api/prazos', methods=['GET'])
def get_prazos():
    try:
        response = supabase.table('prazos').select('*').execute()
        # Map Supabase fields back to frontend expected format
        mapped_data = []
        for item in response.data:
            mapped_data.append({
                'id': item['id'],
                'name': item['nome'],
                'description': item['descricao'],
                'type': item['tipo'],
                'startDate': item['data_inicio'],
                'endDate': item['data_fim'],
                'status': item['status'] or 'pending',
                'progress': item['progress'] or 0,
                'completionDate': item['completion_date'],
                'location': {
                    'state': item['estado'],
                    'lat': item['latitude'],
                    'lng': item['longitude']
                },
                'address': item['endereco']
            })
        return jsonify(mapped_data)
    except Exception as e:
        print(f"Error getting prazos: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/prazos', methods=['POST'])
def create_prazo():
    try:
        data = request.json
        print(f"Received data: {data}")
        # Map frontend fields to database fields
        prazo_data = {
            'nome': data['nome'],
            'descricao': data['descricao'],
            'tipo': data['tipo'],
            'data_inicio': data['data_inicio'],
            'data_fim': data['data_fim'],
            'estado': data['estado'],
            'endereco': data['endereco'],
            'latitude': data['latitude'],
            'longitude': data['longitude']
        }
        response = supabase.table('prazos').insert(prazo_data).execute()
        print(f"Insert response: {response}")
        return jsonify(response.data[0])
    except Exception as e:
        print(f"Error creating prazo: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/prazos/<int:id>', methods=['PUT'])
def update_prazo(id):
    try:
        data = request.json
        print(f"Update data for id {id}: {data}")
        # Map frontend fields to database fields
        prazo_data = {}
        if 'nome' in data: prazo_data['nome'] = data['nome']
        if 'descricao' in data: prazo_data['descricao'] = data['descricao']
        if 'tipo' in data: prazo_data['tipo'] = data['tipo']
        if 'data_inicio' in data: prazo_data['data_inicio'] = data['data_inicio']
        if 'data_fim' in data: prazo_data['data_fim'] = data['data_fim']
        if 'estado' in data: prazo_data['estado'] = data['estado']
        if 'endereco' in data: prazo_data['endereco'] = data['endereco']
        if 'latitude' in data: prazo_data['latitude'] = data['latitude']
        if 'longitude' in data: prazo_data['longitude'] = data['longitude']

        response = supabase.table('prazos').update(prazo_data).eq('id', id).execute()
        print(f"Update response: {response}")
        return jsonify(response.data[0])
    except Exception as e:
        print(f"Error updating prazo {id}: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/prazos/<int:id>', methods=['DELETE'])
def delete_prazo(id):
    try:
        response = supabase.table('prazos').delete().eq('id', id).execute()
        print(f"Delete response for id {id}: {response}")
        return jsonify({'message': 'Prazo deletado com sucesso'})
    except Exception as e:
        print(f"Error deleting prazo {id}: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
