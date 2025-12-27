/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React from 'react';

const Navigation = () => {
  return (
    <nav className="fixed w-full z-50 py-4 backdrop-blur-md bg-[#050806]/70 border-b border-white/5">
      <div className="max-w-7xl mx-auto px-6 flex justify-between items-center">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-lg overflow-hidden border border-brand-green/50 shadow-[0_0_15px_rgba(73,167,96,0.5)] bg-black flex items-center justify-center">
            <img src="/logo.png" alt="AirSight" className="w-full h-full object-cover" />
          </div>
          <span className="font-display font-bold text-2xl tracking-wide text-white">AirSight</span>
        </div>

        <div className="hidden md:flex gap-8 text-sm font-medium text-gray-400">
          <a href="#dashboard" className="hover:text-brand-accent transition-colors">Dashboard</a>
          <a href="#predictions" className="hover:text-brand-accent transition-colors">Forecast</a>
          <a href="#future-scope" className="text-brand-accent hover:text-white transition-colors border border-brand-green/30 px-3 py-1 rounded-full bg-brand-green/10">
            <i className="fas fa-microchip mr-1"></i> Future Tech
          </a>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;
