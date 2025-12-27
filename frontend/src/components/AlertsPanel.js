/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React from 'react';
import { AlertTriangle, CheckCircle, Clock, Activity } from 'lucide-react';

const AlertsPanel = ({ alerts = [] }) => {
  // Alerts are now passed as props from the main App component

  const getSeverityConfig = (severity) => {
    switch (severity?.toLowerCase()) {
      case 'high':
        return {
          icon: AlertTriangle,
          color: 'from-red-500 to-red-700',
          bgColor: 'bg-red-50',
          borderColor: 'border-red-300',
          textColor: 'text-red-700',
          iconBg: 'bg-red-100',
          iconColor: 'text-red-600',
          badgeColor: 'bg-red-500'
        };
      case 'moderate':
        return {
          icon: AlertTriangle,
          color: 'from-orange-500 to-orange-700',
          bgColor: 'bg-orange-50',
          borderColor: 'border-orange-300',
          textColor: 'text-orange-700',
          iconBg: 'bg-orange-100',
          iconColor: 'text-orange-600',
          badgeColor: 'bg-orange-500'
        };
      default:
        return {
          icon: AlertTriangle,
          color: 'from-yellow-500 to-yellow-700',
          bgColor: 'bg-yellow-50',
          borderColor: 'border-yellow-300',
          textColor: 'text-yellow-700',
          iconBg: 'bg-yellow-100',
          iconColor: 'text-yellow-600',
          badgeColor: 'bg-yellow-500'
        };
    }
  };

  return (
    <div className="glass-strong rounded-3xl p-6 shadow-2xl">
      <div className="mb-6">
        <div className="flex items-center space-x-3 mb-1">
          <div className="p-2 bg-gradient-to-br from-red-500 to-orange-500 rounded-lg">
            <AlertTriangle className="w-6 h-6 text-white" />
          </div>
          <h2 className="text-2xl font-bold text-gray-800">Alerts & Warnings</h2>
        </div>
        <p className="text-sm text-gray-600 ml-12">Real-time pollution alerts for your area</p>
      </div>

      {alerts.length === 0 ? (
        <div className="text-center py-12 bg-gradient-to-br from-green-50 to-emerald-50 rounded-2xl border-2 border-green-200">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-green-100 rounded-full mb-4">
            <CheckCircle className="w-8 h-8 text-green-600" />
          </div>
          <h3 className="text-xl font-bold text-gray-800 mb-2">All Clear!</h3>
          <p className="text-gray-600">No active alerts. Air quality conditions are being monitored.</p>
        </div>
      ) : (
        <div className="space-y-4">
          {alerts.map((alert, index) => {
            const config = getSeverityConfig(alert.severity);
            const Icon = config.icon;

            return (
              <div
                key={index}
                className={`${config.bgColor} rounded-2xl p-5 border-2 ${config.borderColor} transform hover:scale-[1.02] transition-all duration-200 shadow-lg`}
              >
                <div className="flex items-start space-x-4">
                  {/* Icon */}
                  <div className={`${config.iconBg} p-3 rounded-xl flex-shrink-0`}>
                    <Icon className={`w-6 h-6 ${config.iconColor}`} />
                  </div>

                  {/* Content */}
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center justify-between mb-2">
                      <div className="flex items-center space-x-2">
                        <span className={`px-3 py-1 ${config.badgeColor} text-white text-xs font-bold rounded-full uppercase`}>
                          {alert.severity}
                        </span>
                        {alert.aqi && (
                          <span className="px-3 py-1 bg-white/80 text-gray-700 text-xs font-semibold rounded-full">
                            AQI: {Math.round(alert.aqi)}
                          </span>
                        )}
                      </div>
                      <div className="flex items-center space-x-1 text-xs text-gray-500">
                        <Clock className="w-3 h-3" />
                        <span>{new Date(alert.timestamp).toLocaleTimeString()}</span>
                      </div>
                    </div>

                    <p className="text-gray-800 font-medium mb-3 leading-relaxed">{alert.message}</p>

                    <div className="flex items-center space-x-4 text-xs">
                      <div className="flex items-center space-x-1 text-gray-600">
                        <Activity className="w-3 h-3" />
                        <span className="capitalize">
                          {alert.type === 'prediction' ? '🔮 Prediction Alert' : '📊 Current Reading'}
                        </span>
                      </div>
                      <span className="text-gray-400">
                        {new Date(alert.timestamp).toLocaleDateString()}
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
};

export default AlertsPanel;
