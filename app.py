from flask import Flask, request, jsonify
from flask_cors import CORS   
import requests

app = Flask(__name__)
CORS(app)  

API_KEY = "8d6bc374e17b41a5a42135330251910"  

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City name is required'}), 400

    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()

    if "error" not in data:
        return jsonify({
            'location': data['location']['name'],
            'country': data['location']['country'],
            'temperature': data['current']['temp_c'],
            'condition': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph']
        })
    else:
        return jsonify({'error': data['error']['message']}), 404


if __name__ == '__main__':
    app.run(debug=True)
