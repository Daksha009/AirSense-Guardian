import React, { useState, useEffect } from 'react';
import './App.css';
import AQICard from './components/AQICard';
import SourceAttribution from './components/SourceAttribution';
import PredictionsChart from './components/PredictionsChart';
import ActionCards from './components/ActionCards';
import AlertsPanel from './components/AlertsPanel';
import { getCompleteAQIData } from './services';

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [location, setLocation] = useState({ lat: 28.6139, lon: 77.2090 }); // Default: Delhi

  useEffect(() => {
    fetchData();
    const interval = setInterval(fetchData, 60000); // Update every minute
    return () => clearInterval(interval);
  }, [location]);

  const fetchData = async () => {
    try {
      setLoading(true);
      // Get weather API key from environment or use null for mock data
      const weatherApiKey = process.env.REACT_APP_WEATHER_API_KEY || null;
      const aqiData = await getCompleteAQIData(location.lat, location.lon, weatherApiKey);
      setData(aqiData);
      setError(null);
    } catch (err) {
      setError(err.message || 'Failed to fetch air quality data');
      console.error('Error fetching data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleLocationChange = (newLocation) => {
    setLocation(newLocation);
  };

  if (loading && !data) {
    return (
      <div className="min-h-screen flex items-center justify-center relative z-10">
        <div className="text-center space-y-6">
          <div className="relative">
            <div className="w-20 h-20 border-4 border-white/30 border-t-white rounded-full animate-spin mx-auto"></div>
            <div className="absolute inset-0 flex items-center justify-center">
              <div className="w-12 h-12 bg-white/20 rounded-full animate-pulse"></div>
            </div>
          </div>
          <p className="text-white text-xl font-medium animate-pulse">Loading air quality data...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen relative z-10">
      {/* Header */}
      <header className="sticky top-0 z-50 glass-strong shadow-lg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <div className="w-12 h-12 bg-gradient-to-br from-purple-500 to-pink-500 rounded-xl flex items-center justify-center text-2xl shadow-lg transform hover:scale-110 transition-transform duration-300">
                🌬️
              </div>
              <div>
                <h1 className="text-3xl font-bold text-gradient">AirSense Guardian</h1>
                <p className="text-sm text-gray-600 italic">From Awareness to Action</p>
              </div>
            </div>
            <div className="hidden md:flex items-center space-x-2 text-sm text-gray-600">
              <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse"></div>
              <span>Live</span>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {error && (
          <div className="mb-6 glass-strong rounded-2xl p-4 border-l-4 border-yellow-500 shadow-lg animate-slide-up">
            <div className="flex items-center space-x-3">
              <span className="text-2xl">⚠️</span>
              <p className="text-gray-800">
                <span className="font-semibold">Connection Error:</span> {error}. Using demo data.
              </p>
            </div>
          </div>
        )}

        {data && (
          <div className="space-y-6 animate-fade-in">
            {/* AQI Card - Full Width */}
            <div className="animate-slide-up" style={{ animationDelay: '0.1s' }}>
              <AQICard 
                current={data.current} 
                weather={data.weather}
                location={location}
                onLocationChange={handleLocationChange}
              />
            </div>

            {/* Grid Layout */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              {/* Source Attribution */}
              <div className="animate-slide-up" style={{ animationDelay: '0.2s' }}>
                <SourceAttribution sources={data.sources} />
              </div>

              {/* Predictions Chart */}
              <div className="animate-slide-up" style={{ animationDelay: '0.3s' }}>
                <PredictionsChart predictions={data.predictions} />
              </div>
            </div>

            {/* Action Cards - Full Width */}
            <div className="animate-slide-up" style={{ animationDelay: '0.4s' }}>
              <ActionCards actions={data.actions} />
            </div>

            {/* Alerts Panel - Full Width */}
            <div className="animate-slide-up" style={{ animationDelay: '0.5s' }}>
              <AlertsPanel alerts={data.alerts || []} />
            </div>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="mt-12 py-6 glass-strong border-t border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-gray-600 text-sm">
            AirSense Guardian - Community-driven air quality intelligence
          </p>
          <p className="text-gray-500 text-xs mt-2">
            Built with ❤️ for cleaner air and healthier communities
          </p>
        </div>
      </footer>
    </div>
  );
}

export default App;
