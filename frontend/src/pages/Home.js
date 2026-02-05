/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React from 'react';
import PollutantCanvas from '../components/PollutantCanvas';
import Navigation from '../components/Navigation';
import Hero from '../components/Hero';
import Dashboard from '../components/Dashboard';
import Predictions from '../components/Predictions';
import LiveMap from '../components/LiveMap';
import FutureScope from '../components/FutureScope';
import Footer from '../components/Footer';
import ActionCards from '../components/ActionCards';

const Home = ({ aqiData, handleDataUpdate }) => {
    return (
        <>
            <PollutantCanvas />
            <Navigation />
            <Hero />
            <Dashboard onDataUpdate={handleDataUpdate} />

            {/* Action Engine Section */}
            {aqiData && (
                <ActionCards
                    actions={aqiData.actions}
                    headline={aqiData.headline_insight}
                />
            )}

            {/* Live Lung Simulator Teaser/CTA can go here if we want, or in Hero */}

            <Predictions predictions={aqiData?.predictions || []} aqiData={aqiData} />
            <LiveMap />
            <FutureScope />
            <Footer />
        </>
    );
};

export default Home;
