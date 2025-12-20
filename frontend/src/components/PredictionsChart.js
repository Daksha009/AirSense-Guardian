import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, Area, AreaChart } from 'recharts';
import { TrendingUp, TrendingDown, Minus } from 'lucide-react';

const PredictionsChart = ({ predictions }) => {
  const chartData = (predictions || []).map(pred => ({
    time: new Date(pred.time).toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }),
    aqi: Math.round(pred.aqi),
    hoursAhead: pred.hours_ahead
  }));

  const getAQIColor = (aqi) => {
    if (aqi <= 50) return '#00e400';
    if (aqi <= 100) return '#ffff00';
    if (aqi <= 150) return '#ff7e00';
    if (aqi <= 200) return '#ff0000';
    if (aqi <= 300) return '#8f3f97';
    return '#7e0023';
  };

  const avgAQI = chartData.length > 0
    ? Math.round(chartData.reduce((sum, d) => sum + d.aqi, 0) / chartData.length)
    : 0;

  const peakAQI = chartData.length > 0 ? Math.max(...chartData.map(d => d.aqi)) : 0;
  const minAQI = chartData.length > 0 ? Math.min(...chartData.map(d => d.aqi)) : 0;
  const trend = chartData.length > 1 
    ? (chartData[chartData.length - 1].aqi > chartData[0].aqi ? 'up' : chartData[chartData.length - 1].aqi < chartData[0].aqi ? 'down' : 'stable')
    : 'stable';

  const TrendIcon = trend === 'up' ? TrendingUp : trend === 'down' ? TrendingDown : Minus;
  const trendColor = trend === 'up' ? 'text-red-500' : trend === 'down' ? 'text-green-500' : 'text-gray-500';

  return (
    <div className="glass-strong rounded-3xl p-6 shadow-2xl transform transition-all duration-300 hover:scale-[1.01]">
      <div className="mb-6">
        <div className="flex items-center justify-between mb-1">
          <h2 className="text-2xl font-bold text-gray-800">AQI Predictions</h2>
          {chartData.length > 1 && (
            <div className={`flex items-center space-x-1 ${trendColor}`}>
              <TrendIcon className="w-5 h-5" />
              <span className="text-sm font-semibold capitalize">{trend}</span>
            </div>
          )}
        </div>
        <p className="text-sm text-gray-600">Next 3-6 hours forecast</p>
      </div>

      {chartData.length > 0 ? (
        <>
          {/* Chart */}
          <div className="mb-6 bg-white/50 rounded-xl p-4 backdrop-blur-sm">
            <ResponsiveContainer width="100%" height={250}>
              <AreaChart data={chartData}>
                <defs>
                  <linearGradient id="colorAqi" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#667eea" stopOpacity={0.4}/>
                    <stop offset="95%" stopColor="#667eea" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#e0e0e0" opacity={0.5} />
                <XAxis 
                  dataKey="time" 
                  stroke="#666"
                  style={{ fontSize: '0.75rem' }}
                  tick={{ fill: '#666' }}
                />
                <YAxis 
                  stroke="#666"
                  label={{ value: 'AQI', angle: -90, position: 'insideLeft', style: { fill: '#666' } }}
                  style={{ fontSize: '0.75rem' }}
                  tick={{ fill: '#666' }}
                />
                <Tooltip 
                  contentStyle={{ 
                    backgroundColor: 'rgba(255, 255, 255, 0.95)',
                    backdropFilter: 'blur(10px)',
                    border: '1px solid rgba(0, 0, 0, 0.1)',
                    borderRadius: '12px',
                    boxShadow: '0 4px 20px rgba(0, 0, 0, 0.1)'
                  }}
                  labelStyle={{ color: '#333', fontWeight: 'bold' }}
                />
                <Area
                  type="monotone"
                  dataKey="aqi"
                  stroke="#667eea"
                  strokeWidth={3}
                  fillOpacity={1}
                  fill="url(#colorAqi)"
                  dot={{ fill: '#667eea', r: 4 }}
                  activeDot={{ r: 6, fill: '#764ba2' }}
                />
              </AreaChart>
            </ResponsiveContainer>
          </div>

          {/* Summary Stats */}
          <div className="grid grid-cols-3 gap-3 mb-4">
            <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl p-3 border border-blue-200">
              <div className="text-xs font-semibold text-blue-700 mb-1">Average</div>
              <div className="text-xl font-bold" style={{ color: getAQIColor(avgAQI) }}>
                {avgAQI}
              </div>
            </div>
            <div className="bg-gradient-to-br from-red-50 to-red-100 rounded-xl p-3 border border-red-200">
              <div className="text-xs font-semibold text-red-700 mb-1">Peak</div>
              <div className="text-xl font-bold" style={{ color: getAQIColor(peakAQI) }}>
                {peakAQI}
              </div>
            </div>
            <div className="bg-gradient-to-br from-green-50 to-green-100 rounded-xl p-3 border border-green-200">
              <div className="text-xs font-semibold text-green-700 mb-1">Lowest</div>
              <div className="text-xl font-bold" style={{ color: getAQIColor(minAQI) }}>
                {minAQI}
              </div>
            </div>
          </div>

          {/* Prediction Timeline */}
          <div className="space-y-2 max-h-40 overflow-y-auto">
            {chartData.map((item, index) => (
              <div
                key={index}
                className="flex items-center justify-between p-3 bg-white/60 rounded-lg backdrop-blur-sm border border-gray-200 hover:bg-white/80 transition-colors"
              >
                <div className="flex items-center space-x-3">
                  <div className="w-2 h-2 rounded-full" style={{ backgroundColor: getAQIColor(item.aqi) }}></div>
                  <span className="text-sm font-medium text-gray-700">{item.time}</span>
                </div>
                <span className="text-sm font-bold" style={{ color: getAQIColor(item.aqi) }}>
                  AQI: {item.aqi}
                </span>
              </div>
            ))}
          </div>
        </>
      ) : (
        <div className="text-center py-12 text-gray-500">
          <div className="text-4xl mb-2">📊</div>
          <p>No prediction data available</p>
        </div>
      )}
    </div>
  );
};

export default PredictionsChart;
