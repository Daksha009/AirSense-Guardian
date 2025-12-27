/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React, { useState } from 'react';
import './App.css';
import PollutantCanvas from './components/PollutantCanvas';
import Navigation from './components/Navigation';
import Hero from './components/Hero';
import Dashboard from './components/Dashboard';
import Predictions from './components/Predictions';
import LiveMap from './components/LiveMap';
import FutureScope from './components/FutureScope';
import Footer from './components/Footer';

function App() {
  const [aqiData, setAqiData] = useState(null);

  const handleDataUpdate = (data) => {
    setAqiData(data);
  };

  return (
    <div className="min-h-screen relative">
      <PollutantCanvas />
      <Navigation />
      <Hero />
      <Dashboard onDataUpdate={handleDataUpdate} />
      <Predictions predictions={aqiData?.predictions || []} aqiData={aqiData} />
      <LiveMap />
      <FutureScope />
      <Footer />
    </div>
  );
}

export default App;
