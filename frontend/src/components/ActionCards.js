/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
import React from 'react';
import { Lightbulb, Clock, TrendingDown, CheckCircle, AlertCircle, XCircle } from 'lucide-react';

const ActionCards = ({ actions }) => {
  const getFeasibilityIcon = (feasibility) => {
    switch (feasibility?.toLowerCase()) {
      case 'high':
        return <CheckCircle className="w-5 h-5 text-green-500" />;
      case 'medium':
        return <AlertCircle className="w-5 h-5 text-yellow-500" />;
      case 'low':
        return <XCircle className="w-5 h-5 text-red-500" />;
      default:
        return <AlertCircle className="w-5 h-5 text-gray-500" />;
    }
  };

  const getFeasibilityColor = (feasibility) => {
    switch (feasibility?.toLowerCase()) {
      case 'high':
        return 'from-green-400 to-green-600';
      case 'medium':
        return 'from-yellow-400 to-yellow-600';
      case 'low':
        return 'from-red-400 to-red-600';
      default:
        return 'from-gray-400 to-gray-600';
    }
  };

  if (!actions || actions.length === 0) {
    return (
      <div className="glass-strong rounded-3xl p-8 shadow-2xl text-center">
        <div className="text-6xl mb-4">💡</div>
        <h2 className="text-2xl font-bold text-gray-800 mb-2">Recommended Actions</h2>
        <p className="text-gray-600">No specific actions recommended at this time.</p>
        <p className="text-sm text-gray-500 mt-2">Air quality conditions are stable.</p>
      </div>
    );
  }

  return (
    <div className="glass-strong rounded-3xl p-6 shadow-2xl">
      <div className="mb-6">
        <div className="flex items-center space-x-3 mb-1">
          <div className="p-2 bg-gradient-to-br from-purple-500 to-pink-500 rounded-lg">
            <Lightbulb className="w-6 h-6 text-white" />
          </div>
          <h2 className="text-2xl font-bold text-gray-800">Recommended Actions</h2>
        </div>
        <p className="text-sm text-gray-600 ml-12">Take action to improve air quality in your area</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {actions.map((action, index) => (
          <div
            key={index}
            className="group relative bg-white/80 backdrop-blur-sm rounded-2xl p-6 border-2 border-gray-200 hover:border-purple-300 transform hover:scale-105 hover:shadow-xl transition-all duration-300 overflow-hidden"
          >
            {/* Background Gradient on Hover */}
            <div className={`absolute inset-0 bg-gradient-to-br ${getFeasibilityColor(action.feasibility)} opacity-0 group-hover:opacity-5 transition-opacity duration-300`}></div>

            <div className="relative z-10">
              {/* Header */}
              <div className="flex items-start justify-between mb-4">
                <div className="flex items-center space-x-3">
                  <div className="text-3xl">{action.icon || '💡'}</div>
                  <div>
                    <h3 className="font-bold text-gray-800 text-lg leading-tight">{action.title}</h3>
                  </div>
                </div>
              </div>

              {/* Description */}
              <p className="text-sm text-gray-600 mb-4 leading-relaxed">{action.description}</p>

              {/* Meta Information */}
              <div className="space-y-3">
                {/* Impact */}
                <div className="flex items-center space-x-2 p-2 bg-gradient-to-r from-purple-50 to-pink-50 rounded-lg border border-purple-100">
                  <TrendingDown className="w-4 h-4 text-purple-600" />
                  <div className="flex-1">
                    <div className="text-xs text-gray-600">Impact</div>
                    <div className="text-sm font-bold text-purple-700">{action.impact}</div>
                  </div>
                </div>

                {/* Time to Impact */}
                <div className="flex items-center space-x-2 p-2 bg-blue-50 rounded-lg border border-blue-100">
                  <Clock className="w-4 h-4 text-blue-600" />
                  <div className="flex-1">
                    <div className="text-xs text-gray-600">Time to Impact</div>
                    <div className="text-sm font-bold text-blue-700">{action.time_to_impact}</div>
                  </div>
                </div>

                {/* Feasibility */}
                <div className="flex items-center space-x-2 p-2 bg-gray-50 rounded-lg border border-gray-200">
                  {getFeasibilityIcon(action.feasibility)}
                  <div className="flex-1">
                    <div className="text-xs text-gray-600">Feasibility</div>
                    <div className="text-sm font-bold text-gray-700 capitalize">{action.feasibility}</div>
                  </div>
                </div>
              </div>
            </div>

            {/* Hover Effect Border */}
            <div className={`absolute inset-0 rounded-2xl border-2 border-transparent group-hover:border-gradient-to-br ${getFeasibilityColor(action.feasibility)} opacity-0 group-hover:opacity-20 transition-opacity duration-300 pointer-events-none`}></div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ActionCards;
