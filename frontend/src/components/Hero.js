import React, { useEffect } from 'react';
import AOS from 'aos';

const Hero = () => {
  useEffect(() => {
    AOS.init({ duration: 800, once: true });
  }, []);

  const scrollToDashboard = () => {
    document.getElementById('dashboard')?.scrollIntoView({ behavior: 'smooth' });
  };

  const scrollToFuture = () => {
    document.getElementById('future-scope')?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <section className="relative min-h-screen flex flex-col justify-center items-center text-center px-4 overflow-hidden">
      <div className="globe"></div>

      <div className="w-28 h-28 mb-8 animate-float relative z-10" data-aos="zoom-in">
        <img 
          src="/logo.png" 
          alt="AirSight" 
          className="w-full h-full object-contain drop-shadow-[0_0_40px_rgba(73,167,96,0.6)]" 
        />
      </div>

      <h1 className="font-display text-5xl md:text-8xl font-bold mb-6 leading-tight" data-aos="fade-up">
        Intelligent <br/><span className="gradient-text">Air Monitoring.</span>
      </h1>
      <p className="text-lg text-gray-400 max-w-2xl mx-auto mb-10" data-aos="fade-up" data-aos-delay="100">
        Real-time environmental data with AI-powered predictions. <br />The future of clean air starts with better data.
      </p>

      <div className="flex flex-col sm:flex-row gap-4 z-10" data-aos="fade-up" data-aos-delay="200">
        <button
          onClick={scrollToDashboard}
          className="px-8 py-4 bg-brand-green text-white font-bold rounded-xl hover:bg-[#3d8b50] transition-all shadow-[0_0_25px_rgba(73,167,96,0.4)]"
        >
          Check My City
        </button>
        <button
          onClick={scrollToFuture}
          className="px-8 py-4 glass-card hover:bg-white/10 font-medium text-white transition-all"
        >
          Our Solution
        </button>
      </div>
    </section>
  );
};

export default Hero;
