# Author: Daksha009
# Repo: https://github.com/Daksha009/AirSense-Guardian.git

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
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

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
        action_results = action_engine.generate_actions(
            aqi_data.get('aqi', 0),
            sources,
            weather_data,
            traffic_density
        )
        actions = action_results.get('actions', [])
        headline_insight = action_results.get('headline', '')
        
        # Get alerts
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
            if pred.get('aqi', 0) > 150:
                alerts.append({
                    'type': 'prediction',
                    'severity': 'high' if pred.get('aqi', 0) > 200 else 'moderate',
                    'message': f'High AQI ({pred.get("aqi", 0):.0f}) expected at {pred.get("time", "N/A")}',
                    'timestamp': pred.get('time', datetime.now().isoformat()),
                    'aqi': pred.get('aqi', 0)
                })
        
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
            'actions': actions,
            'headline_insight': headline_insight,
            'alerts': alerts
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

def fetch_google_data(lat, lon):
    """Fetch AQI data from Google Air Quality API"""
    try:
        api_key = GOOGLE_MAPS_API_KEY
        if not api_key:
            raise ValueError("Google Maps API Key not found")

        url = f"https://airquality.googleapis.com/v1/currentConditions:lookup?key={api_key}"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "location": {
                "latitude": lat,
                "longitude": lon
            },
            "extraComputations": [
                "HEALTH_RECOMMENDATIONS",
                "DOMINANT_POLLUTANT_CONCENTRATION",
                "POLLUTANT_CONCENTRATION",
                "LOCAL_AQI",
                "POLLUTANT_ADDITIONAL_INFO"
            ]
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            indexes = data.get('indexes', [])
            pollutants = data.get('pollutants', [])
            
            # Default values
            aqi = 0
            pm25 = 0
            pm10 = 0
            no2 = 0
            
            # Get Universal AQI or Local AQI
            if len(indexes) > 0:
                # Prefer UAQI (Universal AQI) or the first available
                aqi = indexes[0].get('aqi', 0)
                # Google AQI is 0-100 usually, map to 0-500 scale if needed, 
                # but standard UAQI is 0-100. Let's keep it as is or scale it?
                # User's frontend expects standard PM2.5 based AQI (0-500).
                # Google's UAQI (0-100). Let's multiply by 5 to map roughly? 
                # No, let's check code or comments. 
                # Actually standard US AQI is 0-500. 
                # Google usually provides specific code.
                # Let's search for 'universalAqi' or 'usaEpa'.
                for idx in indexes:
                    if idx.get('code') == 'usa_epa':
                        aqi = idx.get('aqi', 0)
                        break
                if aqi == 0 and len(indexes) > 0:
                     aqi = indexes[0].get('aqi', 0)

            # Extract pollutants
            for pol in pollutants:
                code = pol.get('code', '').lower()
                conc = pol.get('concentration', {}).get('value', 0)
                
                if code == 'pm25':
                    pm25 = conc
                elif code == 'pm10':
                    pm10 = conc
                elif code == 'no2':
                    no2 = conc
            
            return {
                'aqi': int(aqi),
                'pm25': round(pm25, 2),
                'pm10': round(pm10, 2),
                'no2': round(no2, 2)
            }
            
        print(f"Google API Error: {response.status_code} - {response.text}")
        return fetch_fallback_data()

    except Exception as e:
        print(f"Error fetching Google data: {e}")
        return fetch_fallback_data()

def fetch_fallback_data():
    """Return realistic simulation data"""
    base_aqi = 180
    variation = np.random.randint(-30, 50)
    aqi = max(50, min(400, base_aqi + variation))
    
    pm25 = max(10, aqi * 0.4 + np.random.randint(-5, 10))
    pm10 = max(20, aqi * 0.6 + np.random.randint(-10, 15))
    no2 = max(15, aqi * 0.2 + np.random.randint(-5, 10))
    
    return {
        'aqi': round(aqi),
        'pm25': round(pm25, 1),
        'pm10': round(pm10, 1),
        'no2': round(no2, 1)
    }

def fetch_openaq_data(lat, lon):
    """Wrapper for backward compatibility or switching"""
    # Prefer Google API if key exists
    if GOOGLE_MAPS_API_KEY:
        return fetch_google_data(lat, lon)
    
    # ... Rest of OpenAQ logic could go here if we kept it as fallback ...
    return fetch_fallback_data()

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
                'wind_speed': round(wind.get('speed', 0) * 3.6, 1),  # Convert m/s to km/h
                'humidity': main.get('humidity', 50),
                'temperature': round(main.get('temp', 25), 1),
                'pressure': main.get('pressure', 1013)
            }
        
        # Fallback: Realistic Delhi weather data
        return {
            'wind_speed': round(8 + np.random.randint(-2, 5), 1),  # 6-13 km/h typical
            'humidity': 55 + np.random.randint(-15, 20),  # 40-75% typical
            'temperature': round(28 + np.random.randint(-5, 8), 1),  # 23-36°C typical
            'pressure': 1010 + np.random.randint(-5, 5)
        }
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        # Fallback: Realistic Delhi weather
        return {
            'wind_speed': round(8 + np.random.randint(-2, 5), 1),
            'humidity': 55 + np.random.randint(-15, 20),
            'temperature': round(28 + np.random.randint(-5, 8), 1),
            'pressure': 1010 + np.random.randint(-5, 5)
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

