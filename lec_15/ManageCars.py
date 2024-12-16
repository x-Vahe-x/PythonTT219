from flask import Flask, jsonify, request, abort, send_from_directory
import json
import os

app = Flask(__name__)

DATA_FILE = os.path.join(os.path.dirname(__file__), 'cars.json')

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

cars = load_data()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars), 200

@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404
    return jsonify(car), 200

@app.route('/cars', methods=['POST'])
def add_car():
    if not request.json or not all(key in request.json for key in ('make', 'model', 'year', 'price')):
        return jsonify({'error': 'Invalid input'}), 400

    new_car = {
        'id': cars[-1]['id'] + 1 if cars else 1,
        'make': request.json['make'],
        'model': request.json['model'],
        'year': request.json['year'],
        'price': request.json['price']
    }

    cars.append(new_car)
    save_data(cars)
    return jsonify(new_car), 201

@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404

    if not request.json:
        return jsonify({'error': 'Invalid input'}), 400

    car['make'] = request.json.get('make', car['make'])
    car['model'] = request.json.get('model', car['model'])
    car['year'] = request.json.get('year', car['year'])
    car['price'] = request.json.get('price', car['price'])

    save_data(cars)
    return jsonify(car), 200

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    global cars
    car = next((car for car in cars if car['id'] == car_id), None)
    if car is None:
        return jsonify({'error': 'Car not found'}), 404

    cars = [c for c in cars if c['id'] != car_id]
    save_data(cars)
    return jsonify({'message': 'Car deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
