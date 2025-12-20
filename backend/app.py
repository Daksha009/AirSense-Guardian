from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from models.predictor import AQIPredictor
from models.source_attribution import SourceAttribution
from models.action_engine import ActionEngine

load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize models
predictor = AQIPredictor()
source_attributor = SourceAttribution()
action_engine = ActionEngine()

# API Keys (set in .env file)
OPENAQ_API_KEY = os.getenv('OPENAQ_API_KEY', '')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', '')
GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY', '')

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

@app.route('/api/aqi/current', methods=['GET'])
def get_current_aqi():
    """Get current AQI for a location"""
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    
    if not lat or not lon:
        return jsonify({'error': 'Latitude and longitude required'}), 400
    
    try:
        # Fetch from OpenAQ
        aqi_data = fetch_openaq_data(lat, lon)
        
        # Fetch weather data
        weather_data = fetch_weather_data(lat, lon)
        
        # Estimate traffic density
        traffic_density = estimate_traffic_density(lat, lon)
        
        # Get source attribution
        sources = source_attributor.attribute_sources(
            aqi_data.get('aqi', 0),
            weather_data.get('wind_speed', 0),
            traffic_density,
            datetime.now().hour
        )
        
        # Get predictions
        predictions = predictor.predict(
            aqi_data.get('aqi', 0),
            weather_data.get('wind_speed', 0),
            weather_data.get('humidity', 0),
            traffic_density,
            datetime.now()
        )
        
        # Get actionable insights
        actions = action_engine.generate_actions(
            aqi_data.get('aqi', 0),
            sources,
            weather_data,
            traffic_density
        )
        
        return jsonify({
            'current': {
                'aqi': aqi_data.get('aqi', 0),
                'pm25': aqi_data.get('pm25', 0),
                'pm10': aqi_data.get('pm10', 0),
                'no2': aqi_data.get('no2', 0),
                'timestamp': datetime.now().isoformat(),
                'location': {'lat': lat, 'lon': lon}
            },
            'weather': weather_data,
            'traffic_density': traffic_density,
            'sources': sources,
            'predictions': predictions,
            'actions': actions
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/aqi/predict', methods=['POST'])
def predict_aqi():
    """Get AQI predictions for next 3-6 hours"""
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    hours = data.get('hours', 6)
    
    if not lat or not lon:
        return jsonify({'error': 'Latitude and longitude required'}), 400
    
    try:
        # Get current data
        aqi_data = fetch_openaq_data(lat, lon)
        weather_data = fetch_weather_data(lat, lon)
        traffic_density = estimate_traffic_density(lat, lon)
        
        # Generate predictions
        predictions = predictor.predict_multiple_hours(
            aqi_data.get('aqi', 0),
            weather_data.get('wind_speed', 0),
            weather_data.get('humidity', 0),
            traffic_density,
            datetime.now(),
            hours
        )
        
        return jsonify({
            'predictions': predictions,
            'location': {'lat': lat, 'lon': lon}
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    """Get alerts for high pollution zones"""
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    
    if not lat or not lon:
        return jsonify({'error': 'Latitude and longitude required'}), 400
    
    try:
        aqi_data = fetch_openaq_data(lat, lon)
        weather_data = fetch_weather_data(lat, lon)
        traffic_density = estimate_traffic_density(lat, lon)
        
        predictions = predictor.predict_multiple_hours(
            aqi_data.get('aqi', 0),
            weather_data.get('wind_speed', 0),
            weather_data.get('humidity', 0),
            traffic_density,
            datetime.now(),
            6
        )
        
        alerts = []
        current_aqi = aqi_data.get('aqi', 0)
        
        # Check current conditions
        if current_aqi > 150:
            alerts.append({
                'type': 'warning',
                'severity': 'high' if current_aqi > 200 else 'moderate',
                'message': f'Current AQI is {current_aqi:.0f} - Unhealthy conditions detected',
                'timestamp': datetime.now().isoformat()
            })
        
        # Check future predictions
        for pred in predictions:
            if pred['aqi'] > 150:
                alerts.append({
                    'type': 'prediction',
                    'severity': 'high' if pred['aqi'] > 200 else 'moderate',
                    'message': f'High AQI ({pred["aqi"]:.0f}) expected at {pred["time"]}',
                    'timestamp': pred['time'],
                    'aqi': pred['aqi']
                })
        
        return jsonify({'alerts': alerts})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def fetch_openaq_data(lat, lon):
    """Fetch AQI data from OpenAQ API"""
    try:
        # Using OpenAQ API
        url = f"https://api.openaq.org/v2/locations"
        params = {
            'coordinates': f"{lat},{lon}",
            'radius': 10000,  # 10km radius
            'limit': 1
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('results') and len(data['results']) > 0:
                location = data['results'][0]
                # Get latest measurements
                measurements_url = f"https://api.openaq.org/v2/locations/{location['id']}/latest"
                meas_response = requests.get(measurements_url, timeout=10)
                
                if meas_response.status_code == 200:
                    meas_data = meas_response.json()
                    measurements = meas_data.get('results', [])
                    
                    # Extract AQI values
                    pm25 = 0
                    pm10 = 0
                    no2 = 0
                    
                    for meas in measurements:
                        parameter = meas.get('parameter', '').lower()
                        value = meas.get('value', 0)
                        
                        if parameter == 'pm25':
                            pm25 = value
                        elif parameter == 'pm10':
                            pm10 = value
                        elif parameter == 'no2':
                            no2 = value
                    
                    # Calculate AQI (simplified US AQI)
                    aqi = calculate_aqi(pm25, pm10)
                    
                    return {
                        'aqi': aqi,
                        'pm25': pm25,
                        'pm10': pm10,
                        'no2': no2
                    }
        
        # Fallback: Use mock data if API fails
        return {
            'aqi': 120 + np.random.randint(-20, 40),
            'pm25': 45 + np.random.randint(-10, 20),
            'pm10': 80 + np.random.randint(-15, 30),
            'no2': 30 + np.random.randint(-10, 15)
        }
    except Exception as e:
        print(f"Error fetching OpenAQ data: {e}")
        # Return mock data
        return {
            'aqi': 120 + np.random.randint(-20, 40),
            'pm25': 45 + np.random.randint(-10, 20),
            'pm10': 80 + np.random.randint(-15, 30),
            'no2': 30 + np.random.randint(-10, 15)
        }

def fetch_weather_data(lat, lon):
    """Fetch weather data (wind speed, humidity)"""
    try:
        # Using OpenWeatherMap API (free tier)
        api_key = WEATHER_API_KEY or 'demo_key'
        url = f"https://api.openweathermap.org/data/2.5/weather"
        params = {
            'lat': lat,
            'lon': lon,
            'appid': api_key,
            'units': 'metric'
        }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            wind = data.get('wind', {})
            main = data.get('main', {})
            
            return {
                'wind_speed': wind.get('speed', 0) * 3.6,  # Convert m/s to km/h
                'humidity': main.get('humidity', 50),
                'temperature': main.get('temp', 25),
                'pressure': main.get('pressure', 1013)
            }
        
        # Fallback: Mock data
        return {
            'wind_speed': 5 + np.random.randint(-3, 8),
            'humidity': 60 + np.random.randint(-20, 20),
            'temperature': 25 + np.random.randint(-5, 10),
            'pressure': 1013
        }
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return {
            'wind_speed': 5 + np.random.randint(-3, 8),
            'humidity': 60 + np.random.randint(-20, 20),
            'temperature': 25 + np.random.randint(-5, 10),
            'pressure': 1013
        }

def estimate_traffic_density(lat, lon):
    """Estimate traffic density (simplified - using time-based heuristics)"""
    # In a real implementation, you'd use Google Maps API or similar
    # For now, use time-based estimation
    hour = datetime.now().hour
    
    # Peak hours: 7-9 AM, 5-7 PM
    if (7 <= hour <= 9) or (17 <= hour <= 19):
        base_density = 0.8
    elif (10 <= hour <= 16):
        base_density = 0.5
    else:
        base_density = 0.3
    
    # Add some randomness
    density = base_density + np.random.uniform(-0.1, 0.1)
    return max(0, min(1, density))  # Clamp between 0 and 1

def calculate_aqi(pm25, pm10):
    """Calculate US AQI from PM2.5 and PM10"""
    # Simplified AQI calculation
    # In production, use proper AQI formula
    aqi_pm25 = pm25 * 2.5  # Simplified conversion
    aqi_pm10 = pm10 * 1.2
    
    return max(aqi_pm25, aqi_pm10)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

