/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React from 'react';
import { Canvas } from '@react-three/fiber';
import { Sparkles, OrbitControls } from '@react-three/drei';

const LungCanvas = ({ aqi }) => {
    // Calculate CSS filters based on AQI to simulate damage
    // AQI 0 = Normal
    // AQI 500 = Dark, Low Saturation, High Contrast (Soot/Damage)
    const getFilters = (value) => {
        const brightness = 1 - (value / 1000); // 1 -> 0.5
        const contrast = 1 + (value / 500);    // 1 -> 2
        const grayscale = value / 800;         // 0 -> 0.6
        const sepia = value / 1000;            // 0 -> 0.5 (nicotine/stained look)
        const hue = -(value / 20);             // Slight color shift towards red/brown

        return `brightness(${brightness}) contrast(${contrast}) grayscale(${grayscale}) sepia(${sepia}) hue-rotate(${hue}deg)`;
    };

    const filters = getFilters(aqi);

    // Calculate generic red overlay opacity for inflammation
    const inflammationOpacity = Math.max(0, (aqi - 100) / 800); // Starts showing at 100

    return (
        <div className="w-full h-full min-h-[500px] rounded-3xl overflow-hidden glass-card relative group">

            {/* 1. Sketchfab Iframe (The "Real" Model) */}
            <div
                className="absolute inset-0 z-0 transition-all duration-1000 ease-in-out"
                style={{ filter: filters }}
            >
                <iframe
                    title="Realistic Human Lungs"
                    className="w-full h-full border-0"
                    allowFullScreen
                    mozallowfullscreen="true"
                    webkitallowfullscreen="true"
                    allow="autoplay; fullscreen; xr-spatial-tracking"
                    src="https://sketchfab.com/models/ce09f4099a68467880f46e61eb9a3531/embed?autospin=1&ui_theme=dark&dnt=1&autostart=1&transparent=1&ui_controls=0&ui_infos=0&ui_watermark=0"
                />
            </div>

            {/* 2. Inflammation Overlay (Red Pulse) */}
            <div
                className="absolute inset-0 z-10 pointer-events-none mix-blend-multiply bg-red-600 transition-opacity duration-500"
                style={{ opacity: inflammationOpacity }}
            ></div>

            {/* 3. React Three Fiber Overlay (Particles/Smoke) */}
            <div className="absolute inset-0 z-20 pointer-events-none">
                <Canvas camera={{ position: [0, 0, 5], fov: 45 }} gl={{ alpha: true }}>
                    {aqi > 50 && (
                        <Sparkles
                            count={aqi * 2} // More pollution = more particles
                            scale={10}
                            size={aqi > 200 ? 5 : 2}
                            speed={0.4}
                            opacity={0.8}
                            color={aqi > 150 ? "#333" : "#888"}
                        />
                    )}
                </Canvas>
            </div>

            {/* AQI Overlay Label */}
            <div className="absolute top-4 right-4 glass-strong px-4 py-2 rounded-xl text-white font-bold pointer-events-none z-30">
                Simulated AQI: {aqi}
            </div>

            {/* Interaction Hint */}
            <div className="absolute bottom-4 left-1/2 -translate-x-1/2 text-white/50 text-xs pointer-events-none z-30 opacity-0 group-hover:opacity-100 transition-opacity">
                Click and drag to rotate model
            </div>
        </div>
    );
};

export default LungCanvas;
