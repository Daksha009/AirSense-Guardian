import React, { useState } from 'react';
import { MapPin, Wind, Droplets, Thermometer, RefreshCw } from 'lucide-react';

const AQICard = ({ current, weather, location, onLocationChange }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [tempLocation, setTempLocation] = useState(location);

  const getAQICategory = (aqi) => {
    if (aqi <= 50) return { label: 'Good', color: '#00e400', bgGradient: 'from-green-400 to-green-600', emoji: '✅' };
    if (aqi <= 100) return { label: 'Moderate', color: '#ffff00', bgGradient: 'from-yellow-400 to-yellow-600', emoji: '⚠️' };
    if (aqi <= 150) return { label: 'Unhealthy for Sensitive', color: '#ff7e00', bgGradient: 'from-orange-400 to-orange-600', emoji: '😷' };
    if (aqi <= 200) return { label: 'Unhealthy', color: '#ff0000', bgGradient: 'from-red-400 to-red-600', emoji: '🚨' };
    if (aqi <= 300) return { label: 'Very Unhealthy', color: '#8f3f97', bgGradient: 'from-purple-500 to-purple-700', emoji: '🔴' };
    return { label: 'Hazardous', color: '#7e0023', bgGradient: 'from-red-700 to-red-900', emoji: '☠️' };
  };

  const category = getAQICategory(current?.aqi || 0);
  const aqiValue = Math.round(current?.aqi || 0);

  const handleLocationSubmit = () => {
    onLocationChange(tempLocation);
    setIsEditing(false);
  };

  return (
    <div className="glass-strong rounded-3xl p-8 shadow-2xl transform transition-all duration-300 hover:scale-[1.01] relative overflow-hidden">
      {/* Background Gradient Effect */}
      <div className={`absolute inset-0 bg-gradient-to-br ${category.bgGradient} opacity-5 pointer-events-none`}></div>
      
      {/* Header */}
      <div className="relative z-10 flex items-center justify-between mb-6">
        <div>
          <h2 className="text-2xl font-bold text-gray-800 mb-1">Current Air Quality</h2>
          <p className="text-sm text-gray-600">Real-time monitoring</p>
        </div>
        <button
          onClick={() => setIsEditing(!isEditing)}
          className="p-2 rounded-lg bg-gray-100 hover:bg-gray-200 transition-colors"
          title="Change location"
        >
          <MapPin className="w-5 h-5 text-gray-600" />
        </button>
      </div>

      {/* Location Input */}
      {isEditing && (
        <div className="relative z-10 mb-6 p-4 bg-gray-50 rounded-xl border-2 border-purple-200 animate-slide-up">
          <div className="grid grid-cols-2 gap-3 mb-3">
            <div>
              <label className="block text-xs font-semibold text-gray-700 mb-1">Latitude</label>
              <input
                type="number"
                value={tempLocation.lat}
                onChange={(e) => setTempLocation({ ...tempLocation, lat: parseFloat(e.target.value) || 0 })}
                step="0.0001"
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                placeholder="28.6139"
              />
            </div>
            <div>
              <label className="block text-xs font-semibold text-gray-700 mb-1">Longitude</label>
              <input
                type="number"
                value={tempLocation.lon}
                onChange={(e) => setTempLocation({ ...tempLocation, lon: parseFloat(e.target.value) || 0 })}
                step="0.0001"
                className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                placeholder="77.2090"
              />
            </div>
          </div>
          <button
            onClick={handleLocationSubmit}
            className="w-full py-2 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-lg font-semibold hover:shadow-lg transform hover:scale-105 transition-all duration-200"
          >
            Update Location
          </button>
        </div>
      )}

      {/* AQI Display */}
      <div className="relative z-10 mb-8">
        <div className="flex items-center justify-center space-x-6">
          <div className="text-center">
            <div className={`text-7xl font-bold mb-2`} style={{ color: category.color }}>
              {aqiValue}
            </div>
            <div className="flex items-center justify-center space-x-2">
              <span className="text-3xl">{category.emoji}</span>
              <span className="text-lg font-semibold text-gray-700">{category.label}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Pollution Metrics */}
      <div className="relative z-10 grid grid-cols-3 gap-4 mb-6">
        <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl p-4 border border-blue-200 transform hover:scale-105 transition-transform duration-200">
          <div className="text-xs font-semibold text-blue-700 mb-1">PM2.5</div>
          <div className="text-2xl font-bold text-blue-900">{current?.pm25?.toFixed(1) || 'N/A'}</div>
          <div className="text-xs text-blue-600">µg/m³</div>
        </div>
        <div className="bg-gradient-to-br from-indigo-50 to-indigo-100 rounded-xl p-4 border border-indigo-200 transform hover:scale-105 transition-transform duration-200">
          <div className="text-xs font-semibold text-indigo-700 mb-1">PM10</div>
          <div className="text-2xl font-bold text-indigo-900">{current?.pm10?.toFixed(1) || 'N/A'}</div>
          <div className="text-xs text-indigo-600">µg/m³</div>
        </div>
        <div className="bg-gradient-to-br from-purple-50 to-purple-100 rounded-xl p-4 border border-purple-200 transform hover:scale-105 transition-transform duration-200">
          <div className="text-xs font-semibold text-purple-700 mb-1">NO₂</div>
          <div className="text-2xl font-bold text-purple-900">{current?.no2?.toFixed(1) || 'N/A'}</div>
          <div className="text-xs text-purple-600">µg/m³</div>
        </div>
      </div>

      {/* Weather Info */}
      <div className="relative z-10 grid grid-cols-3 gap-4">
        <div className="flex items-center space-x-3 p-4 bg-white/60 rounded-xl backdrop-blur-sm border border-gray-200">
          <div className="p-2 bg-blue-100 rounded-lg">
            <Wind className="w-5 h-5 text-blue-600" />
          </div>
          <div>
            <div className="text-xs text-gray-600">Wind Speed</div>
            <div className="text-lg font-bold text-gray-800">{weather?.wind_speed?.toFixed(1) || 'N/A'} km/h</div>
          </div>
        </div>
        <div className="flex items-center space-x-3 p-4 bg-white/60 rounded-xl backdrop-blur-sm border border-gray-200">
          <div className="p-2 bg-cyan-100 rounded-lg">
            <Droplets className="w-5 h-5 text-cyan-600" />
          </div>
          <div>
            <div className="text-xs text-gray-600">Humidity</div>
            <div className="text-lg font-bold text-gray-800">{weather?.humidity || 'N/A'}%</div>
          </div>
        </div>
        <div className="flex items-center space-x-3 p-4 bg-white/60 rounded-xl backdrop-blur-sm border border-gray-200">
          <div className="p-2 bg-orange-100 rounded-lg">
            <Thermometer className="w-5 h-5 text-orange-600" />
          </div>
          <div>
            <div className="text-xs text-gray-600">Temperature</div>
            <div className="text-lg font-bold text-gray-800">{weather?.temperature?.toFixed(1) || 'N/A'}°C</div>
          </div>
        </div>
      </div>

      {/* Timestamp */}
      <div className="relative z-10 mt-6 pt-6 border-t border-gray-200 flex items-center justify-center space-x-2 text-sm text-gray-500">
        <RefreshCw className="w-4 h-4" />
        <span>Last updated: {current?.timestamp ? new Date(current.timestamp).toLocaleTimeString() : 'N/A'}</span>
      </div>
    </div>
  );
};

export default AQICard;
