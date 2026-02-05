/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React from 'react';
import { Link } from 'react-router-dom';
import LiveLungSimulator from '../components/LungSimulation';
import { ArrowLeft } from 'lucide-react';

const LungSimulatorPage = () => {
    return (
        <div className="min-h-screen relative bg-black">
            {/* Background (Gradient matches simulator) */}
            <div className="absolute top-0 left-0 w-full h-full bg-gradient-to-b from-black via-[#0a0a0a] to-black z-0"></div>

            {/* Back Button */}
            <div className="absolute top-6 left-6 z-50">
                <Link to="/" className="flex items-center gap-2 text-white/70 hover:text-brand-green transition-colors bg-white/5 hover:bg-white/10 px-4 py-2 rounded-full backdrop-blur-md border border-white/10">
                    <ArrowLeft className="w-5 h-5" />
                    <span className="font-bold">Back to Dashboard</span>
                </Link>
            </div>

            {/* The Simulator */}
            <div className="relative z-10 pt-10">
                <LiveLungSimulator />
            </div>
        </div>
    );
};

export default LungSimulatorPage;
