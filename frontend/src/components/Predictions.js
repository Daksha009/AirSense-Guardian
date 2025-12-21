import React, { useEffect, useRef } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import AOS from 'aos';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  Filler
);

const Predictions = ({ predictions, aqiData }) => {
  const chartRef = useRef(null);

  useEffect(() => {
    AOS.init({ duration: 800, once: true });
  }, []);

  const getHealthRecommendations = (aqi) => {
    if (aqi > 150) {
      return {
        alert: { level: 'Unhealthy', color: 'red', message: 'Everyone should limit prolonged outdoor exertion.' },
        mask: 'Required',
        ventilation: 'Not Recommended',
        sports: 'Avoid',
        purifier: 'High Mode'
      };
    } else if (aqi > 100) {
      return {
        alert: { level: 'Unhealthy for Sensitive', color: 'orange', message: 'Sensitive groups should limit prolonged outdoor exertion.' },
        mask: 'Recommended',
        ventilation: 'Limited',
        sports: 'Moderate',
        purifier: 'Medium Mode'
      };
    } else if (aqi > 50) {
      return {
        alert: { level: 'Moderate', color: 'yellow', message: 'Sensitive groups should limit prolonged outdoor exertion.' },
        mask: 'Optional',
        ventilation: 'Recommended',
        sports: 'Safe',
        purifier: 'Low Mode'
      };
    } else {
      return {
        alert: { level: 'Good', color: 'green', message: 'Air quality is satisfactory.' },
        mask: 'Not Needed',
        ventilation: 'Recommended',
        sports: 'Safe',
        purifier: 'Not Needed'
      };
    }
  };

  const currentAQI = aqiData?.current?.aqi ? Math.round(aqiData.current.aqi) : 134;
  const health = getHealthRecommendations(currentAQI);

  const chartData = {
    labels: predictions && predictions.length > 0
      ? predictions.slice(0, 7).map(p => {
          const date = new Date(p.time);
          return date.toLocaleTimeString('en-US', { hour: 'numeric', hour12: true });
        })
      : ['Now', '2 PM', '4 PM', '6 PM', '8 PM', '10 PM', '12 AM'],
    datasets: [{
      label: 'Predicted AQI',
      data: predictions && predictions.length > 0
        ? predictions.slice(0, 7).map(p => Math.round(p.aqi || 0))
        : [134, 140, 155, 160, 145, 130, 120],
      borderColor: '#49a760',
      backgroundColor: (context) => {
        const ctx = context.chart.ctx;
        const gradient = ctx.createLinearGradient(0, 0, 0, 300);
        gradient.addColorStop(0, 'rgba(73, 167, 96, 0.4)');
        gradient.addColorStop(1, 'rgba(73, 167, 96, 0.0)');
        return gradient;
      },
      fill: true,
      tension: 0.4,
      pointBackgroundColor: '#000',
      pointBorderColor: '#00ff9d',
    }]
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false }
    },
    scales: {
      x: { grid: { display: false } },
      y: { grid: { color: 'rgba(255,255,255,0.05)' } }
    }
  };

  return (
    <section id="predictions" className="py-10 px-4">
      <div className="max-w-7xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="glass-card p-8" data-aos="fade-up">
          <h3 className="text-xl font-display font-bold mb-6 flex items-center gap-2">
            <i className="fas fa-chart-line text-brand-accent"></i> 24-Hour AI Forecast
          </h3>
          <div className="h-64 w-full">
            <Line ref={chartRef} data={chartData} options={chartOptions} />
          </div>
        </div>

        <div className="glass-card p-8" data-aos="fade-up" data-aos-delay="100">
          <h3 className="text-xl font-display font-bold mb-6 flex items-center gap-2">
            <i className="fas fa-heart-pulse text-red-400"></i> Health Alerts
          </h3>
          
          <div className={`p-4 mb-6 rounded-r-lg border-l-4 ${
            health.alert.color === 'red' ? 'bg-red-500/10 border-red-500' :
            health.alert.color === 'orange' ? 'bg-orange-500/10 border-orange-500' :
            health.alert.color === 'yellow' ? 'bg-yellow-500/10 border-yellow-500' :
            'bg-green-500/10 border-green-500'
          }`}>
            <h4 className={`font-bold mb-1 ${
              health.alert.color === 'red' ? 'text-red-500' :
              health.alert.color === 'orange' ? 'text-orange-500' :
              health.alert.color === 'yellow' ? 'text-yellow-500' :
              'text-green-500'
            }`}>{health.alert.level} Air Quality</h4>
            <p className="text-sm text-gray-400">{health.alert.message}</p>
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div className="bg-white/5 p-4 rounded-xl text-center hover:bg-white/10 transition-colors">
              <i className="fas fa-mask text-2xl text-gray-400 mb-2"></i>
              <p className="text-sm font-bold text-gray-300">Mask</p>
              <p className="text-xs text-gray-500">{health.mask}</p>
            </div>
            <div className="bg-white/5 p-4 rounded-xl text-center hover:bg-white/10 transition-colors">
              <i className="fas fa-door-open text-2xl text-brand-green mb-2"></i>
              <p className="text-sm font-bold text-gray-300">Ventilation</p>
              <p className="text-xs text-gray-500">{health.ventilation}</p>
            </div>
            <div className="bg-white/5 p-4 rounded-xl text-center hover:bg-white/10 transition-colors">
              <i className="fas fa-person-running text-2xl text-blue-400 mb-2"></i>
              <p className="text-sm font-bold text-gray-300">Sports</p>
              <p className="text-xs text-gray-500">{health.sports}</p>
            </div>
            <div className="bg-white/5 p-4 rounded-xl text-center hover:bg-white/10 transition-colors">
              <i className="fas fa-fan text-2xl text-gray-400 mb-2"></i>
              <p className="text-sm font-bold text-gray-300">Purifier</p>
              <p className="text-xs text-gray-500">{health.purifier}</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Predictions;
