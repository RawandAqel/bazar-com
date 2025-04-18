from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# Server URLs (will be set based on environment)
CATALOG_SERVER = os.getenv('CATALOG_SERVER', 'http://localhost:5001')
ORDER_SERVER = os.getenv('ORDER_SERVER', 'http://localhost:5002')

@app.route('/search/<topic>', methods=['GET'])
def search(topic):
    response = requests.get(f'{CATALOG_SERVER}/search/{topic}')
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Failed to search"}), 500

@app.route('/info/<int:item_number>', methods=['GET'])
def info(item_number):
    response = requests.get(f'{CATALOG_SERVER}/info/{item_number}')
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Book not found"}), 404

@app.route('/purchase/<int:item_number>', methods=['POST'])
def purchase(item_number):
    response = requests.post(f'{ORDER_SERVER}/purchase/{item_number}')
    if response.status_code == 200:
        return jsonify(response.json())
    return jsonify({"error": "Purchase failed"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)