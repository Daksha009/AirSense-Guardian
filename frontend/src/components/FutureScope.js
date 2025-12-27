/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React, { useEffect } from 'react';
import AOS from 'aos';

const FutureScope = () => {
  useEffect(() => {
    AOS.init({ duration: 800, once: true });
  }, []);

  return (
    <section id="future-scope" className="py-24 px-4 relative overflow-hidden">
      <div className="absolute top-0 left-0 w-full h-full bg-brand-green/5 -z-10"></div>
      <div className="absolute -right-20 top-40 w-96 h-96 bg-brand-green/10 blur-[100px] rounded-full"></div>

      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <span className="text-brand-accent font-mono text-sm tracking-widest uppercase mb-2 block">Our Future Vision</span>
          <h2 className="text-4xl md:text-5xl font-display font-bold mb-4">Mobile Sensor Technology</h2>
          <p className="text-gray-400 max-w-2xl mx-auto">We are developing hardware to bridge the data gap. Turning every vehicle into a monitoring station.</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="glass-card p-8 text-center relative border border-brand-green/40 shadow-[0_0_20px_rgba(73,167,96,0.15)] hover:-translate-y-2 transition-transform duration-300" data-aos="fade-up">
            <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-brand-accent text-black text-[10px] font-bold px-3 py-1 rounded-full">PROTOTYPE</div>
            <div className="w-16 h-16 mx-auto bg-brand-green rounded-full flex items-center justify-center text-2xl mb-6 shadow-lg shadow-brand-green/30">
              <i className="fas fa-microchip text-black"></i>
            </div>
            <h3 className="text-xl font-bold mb-3">AirSight IoT Node</h3>
            <p className="text-gray-400 text-sm">A compact, low-cost hardware sensor designed to attach to vehicle roofs. Measures PM2.5, PM10, and NO2 in motion.</p>
          </div>

          <div className="glass-card p-8 text-center relative hover:-translate-y-2 transition-transform duration-300" data-aos="fade-up" data-aos-delay="100">
            <div className="w-16 h-16 mx-auto bg-gray-800 rounded-full flex items-center justify-center text-2xl mb-6 shadow-lg">
              <i className="fas fa-network-wired text-blue-400"></i>
            </div>
            <h3 className="text-xl font-bold mb-3">Mesh Network</h3>
            <p className="text-gray-400 text-sm">Data collected from taxis and buses creates a live heatmap of street-level pollution.</p>
          </div>

          <div className="glass-card p-8 text-center relative hover:-translate-y-2 transition-transform duration-300" data-aos="fade-up" data-aos-delay="200">
            <div className="w-16 h-16 mx-auto bg-gray-800 rounded-full flex items-center justify-center text-2xl mb-6 shadow-lg">
              <i className="fas fa-brain text-purple-400"></i>
            </div>
            <h3 className="text-xl font-bold mb-3">Predictive AI</h3>
            <p className="text-gray-400 text-sm">Our algorithms process this mobile data to predict pollution spikes before they happen.</p>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FutureScope;
