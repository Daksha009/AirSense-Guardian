import React from 'react';
import { Car, Factory, Flame, Cloud } from 'lucide-react';

const SourceAttribution = ({ sources }) => {
  const sourceConfig = {
    traffic: {
      icon: Car,
      label: 'Traffic',
      color: 'from-red-400 to-red-600',
      bgColor: 'bg-red-50',
      borderColor: 'border-red-200',
      textColor: 'text-red-700',
      iconBg: 'bg-red-100',
      iconColor: 'text-red-600'
    },
    industry: {
      icon: Factory,
      label: 'Industry',
      color: 'from-cyan-400 to-cyan-600',
      bgColor: 'bg-cyan-50',
      borderColor: 'border-cyan-200',
      textColor: 'text-cyan-700',
      iconBg: 'bg-cyan-100',
      iconColor: 'text-cyan-600'
    },
    open_burning: {
      icon: Flame,
      label: 'Open Burning',
      color: 'from-orange-400 to-orange-600',
      bgColor: 'bg-orange-50',
      borderColor: 'border-orange-200',
      textColor: 'text-orange-700',
      iconBg: 'bg-orange-100',
      iconColor: 'text-orange-600'
    },
    other: {
      icon: Cloud,
      label: 'Other',
      color: 'from-gray-400 to-gray-600',
      bgColor: 'bg-gray-50',
      borderColor: 'border-gray-200',
      textColor: 'text-gray-700',
      iconBg: 'bg-gray-100',
      iconColor: 'text-gray-600'
    }
  };

  const total = Object.values(sources || {}).reduce((sum, val) => sum + val, 0);
  const primarySource = Object.entries(sources || {})
    .sort(([, a], [, b]) => b - a)[0];

  return (
    <div className="glass-strong rounded-3xl p-6 shadow-2xl transform transition-all duration-300 hover:scale-[1.01]">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-1">Pollution Sources</h2>
        <p className="text-sm text-gray-600">Current contribution breakdown</p>
      </div>

      <div className="space-y-4 mb-6">
        {Object.entries(sources || {}).map(([key, value]) => {
          const config = sourceConfig[key];
          const Icon = config?.icon || Cloud;
          const percentage = value || 0;
          
          return (
            <div
              key={key}
              className={`${config.bgColor} rounded-xl p-4 border-2 ${config.borderColor} transform hover:scale-[1.02] transition-all duration-200`}
            >
              <div className="flex items-center justify-between mb-3">
                <div className="flex items-center space-x-3">
                  <div className={`${config.iconBg} p-2 rounded-lg`}>
                    <Icon className={`w-5 h-5 ${config.iconColor}`} />
                  </div>
                  <div>
                    <div className="font-semibold text-gray-800">{config.label}</div>
                    <div className="text-xs text-gray-600">Source attribution</div>
                  </div>
                </div>
                <div className="text-right">
                  <div className={`text-2xl font-bold ${config.textColor}`}>{percentage}%</div>
                </div>
              </div>
              
              {/* Progress Bar */}
              <div className="relative h-3 bg-white rounded-full overflow-hidden shadow-inner">
                <div
                  className={`h-full bg-gradient-to-r ${config.color} rounded-full transition-all duration-1000 ease-out relative overflow-hidden`}
                  style={{ width: `${percentage}%` }}
                >
                  <div className="absolute inset-0 bg-white/30 animate-pulse"></div>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Primary Source Summary */}
      {primarySource && (
        <div className="bg-gradient-to-r from-purple-50 to-pink-50 rounded-xl p-4 border-2 border-purple-200">
          <div className="flex items-center justify-between">
            <div>
              <div className="text-xs font-semibold text-purple-700 mb-1">PRIMARY SOURCE</div>
              <div className="text-lg font-bold text-gray-800">
                {sourceConfig[primarySource[0]]?.label || 'N/A'}
              </div>
            </div>
            <div className="text-3xl font-bold text-purple-600">
              {primarySource[1]}%
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default SourceAttribution;
