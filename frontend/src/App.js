/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React, { useState } from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import LungSimulatorPage from './pages/LungSimulatorPage';
  
import Chatbot from './components/Chatbot';

function App() {
  const [aqiData, setAqiData] = useState(null);

  const handleDataUpdate = (data) => {
    setAqiData(data);
  };

  return (
    <Router>
      <div className="min-h-screen relative">
        {/* The LiquidEther background has been removed to restore the Dark UI */}

        <Routes>
          <Route
            path="/"
            element={<Home aqiData={aqiData} handleDataUpdate={handleDataUpdate} />}
          />
          <Route
            path="/lung-simulator"
            element={<LungSimulatorPage />}
          />
        </Routes>
        <Chatbot />
      </div>
    </Router>
  );
}

export default App;
