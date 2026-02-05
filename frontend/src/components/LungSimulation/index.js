/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React, { useState } from 'react';
import LungCanvas from './LungCanvas';
import { AlertCircle, Wind, Activity } from 'lucide-react';
import AOS from 'aos';

const LiveLungSimulator = () => {
    const [aqi, setAqi] = useState(50);

    const getHealthStatus = (value) => {
        if (value <= 50) return { text: 'Healthy', color: 'text-green-400', desc: 'Respiration is clear. Cilia are active. No inflammation.' };
        if (value <= 100) return { text: 'Moderate', color: 'text-yellow-400', desc: 'Minor irritation in sensitive individuals. Slight mucus production.' };
        if (value <= 150) return { text: 'Unhealthy for Sensitive', color: 'text-orange-400', desc: 'Inflammation begins. Bronchial tubes constrict slightly.' };
        if (value <= 200) return { text: 'Unhealthy', color: 'text-red-400', desc: 'Significant inflammation. Increased heart rate to compensate for lower O2.' };
        if (value <= 300) return { text: 'Very Unhealthy', color: 'text-purple-400', desc: 'Severe distress. Particulates trapped in alveoli. Breathing is labored.' };
        return { text: 'Hazardous', color: 'text-red-700', desc: 'Critical damage. Cilia paralyzed. High risk of respiratory failure.' };
    };

    const status = getHealthStatus(aqi);

    React.useEffect(() => {
        AOS.init({ duration: 800, once: true });
    }, []);

    return (
        <section id="lung-simulator" className="py-20 px-4 relative">
            <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-b from-black via-[#0a0a0a] to-black z-[-1]"></div>

            <div className="max-w-7xl mx-auto">
                <div className="mb-12 text-center" data-aos="fade-up">
                    <h2 className="text-4xl md:text-5xl font-display font-bold mb-4">
                        Live <span className="bg-clip-text text-transparent bg-gradient-to-r from-pink-400 to-red-600">Lung Impact</span> Simulator
                    </h2>
                    <p className="text-gray-400 max-w-2xl mx-auto">
                        Visualize how air quality affects human lungs in real-time. Drag the slider to see the invisible damage caused by pollution.
                    </p>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-2 gap-10 items-center">
                    {/* 3D Canvas */}
                    <div className="h-[500px] lg:h-[600px] w-full" data-aos="fade-right">
                        <LungCanvas aqi={aqi} />
                    </div>

                    {/* Controls & info */}
                    <div data-aos="fade-left">
                        <div className="glass-card p-8 rounded-3xl mb-8">
                            <div className="flex justify-between items-end mb-4">
                                <label className="text-gray-300 font-bold flex items-center gap-2">
                                    <Wind className="w-5 h-5 text-brand-accent" /> Adjust AQI Level
                                </label>
                                <span className="text-4xl font-bold text-white font-display">{aqi}</span>
                            </div>

                            <input
                                type="range"
                                min="0"
                                max="500"
                                value={aqi}
                                onChange={(e) => setAqi(parseInt(e.target.value))}
                                className="w-full h-3 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-brand-green hover:accent-brand-accent transition-all"
                            />
                            <div className="flex justify-between text-xs text-gray-500 mt-2 font-mono">
                                <span>0 (Clean)</span>
                                <span>250 (Danger)</span>
                                <span>500 (Hazardous)</span>
                            </div>
                        </div>

                        {/* Health Impact Card */}
                        <div className="glass-strong p-8 rounded-3xl border-l-4 border-l-brand-accent relative overflow-hidden transition-all duration-300">
                            <div className="absolute top-0 right-0 w-32 h-32 bg-white/5 blur-[50px] rounded-full"></div>

                            <h3 className={`text-3xl font-bold mb-2 ${status.color}`}>
                                {status.text}
                            </h3>
                            <div className="flex items-start gap-4 mt-6">
                                <div className={`p-3 rounded-xl bg-white/10 ${status.color}`}>
                                    <Activity className="w-6 h-6" />
                                </div>
                                <div>
                                    <h4 className="text-lg font-bold text-gray-200 mb-1">Physiological Effect</h4>
                                    <p className="text-gray-400 leading-relaxed">
                                        {status.desc}
                                    </p>
                                </div>
                            </div>

                            {aqi > 150 && (
                                <div className="mt-6 p-4 bg-red-500/10 border border-red-500/30 rounded-xl flex items-center gap-3">
                                    <AlertCircle className="w-6 h-6 text-red-500 flex-shrink-0" />
                                    <p className="text-sm text-red-300 font-medium">
                                        Warning: Long-term exposure to this level can cause permanent respiratory damage.
                                    </p>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </section>
    );
};

export default LiveLungSimulator;
