from flask import Flask, jsonify
import json
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)
# Load the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Define the API route
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

