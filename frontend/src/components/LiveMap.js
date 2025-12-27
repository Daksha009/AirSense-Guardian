/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React, { useEffect, useRef } from 'react';
import { MapContainer, TileLayer, CircleMarker, Popup } from 'react-leaflet';
import L from 'leaflet';
import AOS from 'aos';

// Fix for default marker icon in React-Leaflet
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon-2x.png',
  iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-icon.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/images/marker-shadow.png',
});

const LiveMap = () => {
  useEffect(() => {
    AOS.init({ duration: 800, once: true });
  }, []);

  const cities = [
    { lat: 28.6139, lng: 77.2090, aqi: 134, name: "Delhi" },
    { lat: 19.0760, lng: 72.8777, aqi: 85, name: "Mumbai" },
    { lat: 12.9716, lng: 77.5946, aqi: 45, name: "Bangalore" },
    { lat: 22.5726, lng: 88.3639, aqi: 110, name: "Kolkata" }
  ];

  const getMarkerColor = (aqi) => {
    if (aqi > 200) return '#ef4444';
    if (aqi > 100) return '#eab308';
    return '#22c55e';
  };

  return (
    <section id="live-map" className="py-10 px-4">
      <div className="max-w-7xl mx-auto">
        <div className="mb-6" data-aos="fade-up">
          <h2 className="text-2xl font-display font-bold">Global Monitoring Network</h2>
        </div>
        <div className="glass-card p-2 h-[450px] relative overflow-hidden" data-aos="zoom-in">
          <MapContainer
            center={[20.5937, 78.9629]}
            zoom={4}
            style={{ height: '100%', width: '100%', borderRadius: '12px', zIndex: 10 }}
          >
            <TileLayer
              url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
              attribution='&copy; CARTO'
              maxZoom={19}
            />
            {cities.map((city, index) => (
              <CircleMarker
                key={index}
                center={[city.lat, city.lng]}
                radius={6}
                pathOptions={{
                  fillColor: getMarkerColor(city.aqi),
                  color: "#fff",
                  weight: 1,
                  opacity: 1,
                  fillOpacity: 0.8
                }}
              >
                <Popup>
                  <b>{city.name}</b><br />AQI: {city.aqi}
                </Popup>
              </CircleMarker>
            ))}
          </MapContainer>
        </div>
      </div>
    </section>
  );
};

export default LiveMap;
