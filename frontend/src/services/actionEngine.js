/**
 * Action Engine Service
 * Generates actionable insights to reduce pollution
 */

/**
 * Generate actionable insights based on current conditions
 * @param {number} currentAQI - Current AQI value
 * @param {Object} sources - Source attribution percentages
 * @param {Object} weatherData - Weather data
 * @param {number} trafficDensity - Traffic density (0-1)
 * @returns {Array} List of action objects
 */
export function generateActions(currentAQI, sources, weatherData, trafficDensity) {
  const actions = [];
  
  // High traffic contribution
  if (sources.traffic > 40) {
    actions.push({
      type: 'carpool',
      title: 'Promote Carpooling',
      description: `If 15% of commuters carpool in the next 2 hours, AQI can drop by ~${Math.round(sources.traffic * 0.12)}%`,
      impact: `${Math.round(sources.traffic * 0.12)}% AQI reduction`,
      feasibility: 'high',
      time_to_impact: '2-3 hours',
      icon: '🚗'
    });
    
    actions.push({
      type: 'public_transport',
      title: 'Use Public Transport',
      description: 'Switching to public transport reduces vehicle emissions by 60-70%',
      impact: `${Math.round(sources.traffic * 0.15)}% AQI reduction`,
      feasibility: 'high',
      time_to_impact: '1-2 hours',
      icon: '🚌'
    });
  }
  
  // Low wind conditions
  if (weatherData.wind_speed < 5) {
    actions.push({
      type: 'reduce_activity',
      title: 'Reduce Outdoor Activities',
      description: 'Low wind speed means pollutants are accumulating. Limit outdoor activities and avoid exercising outside.',
      impact: 'Prevents health issues',
      feasibility: 'immediate',
      time_to_impact: 'immediate',
      icon: '⚠️'
    });
  }
  
  // High AQI overall
  if (currentAQI > 150) {
    actions.push({
      type: 'alert_authorities',
      title: 'Alert Local Authorities',
      description: 'Notify local environmental agencies about high pollution levels for immediate action',
      impact: 'Enables regulatory response',
      feasibility: 'high',
      time_to_impact: '4-6 hours',
      icon: '📢'
    });
    
    actions.push({
      type: 'indoor_air',
      title: 'Improve Indoor Air Quality',
      description: 'Close windows, use air purifiers, and avoid activities that generate indoor pollution',
      impact: 'Protects immediate health',
      feasibility: 'immediate',
      time_to_impact: 'immediate',
      icon: '🏠'
    });
  }
  
  // Industrial contribution
  if (sources.industry > 30) {
    actions.push({
      type: 'report_industry',
      title: 'Report Industrial Emissions',
      description: 'High industrial contribution detected. Report to environmental monitoring authorities.',
      impact: 'Enables source control',
      feasibility: 'medium',
      time_to_impact: '6-12 hours',
      icon: '🏭'
    });
  }
  
  // Open burning contribution
  if (sources.open_burning > 20) {
    actions.push({
      type: 'stop_burning',
      title: 'Stop Open Burning',
      description: 'Open burning detected in area. Report and discourage open waste burning.',
      impact: `${Math.round(sources.open_burning * 0.2)}% AQI reduction`,
      feasibility: 'medium',
      time_to_impact: '1-2 hours',
      icon: '🔥'
    });
  }
  
  // If no specific actions, provide general recommendations
  if (actions.length === 0) {
    actions.push({
      type: 'general',
      title: 'Maintain Good Air Quality',
      description: 'Current air quality is acceptable. Continue monitoring and follow best practices.',
      impact: 'Preventive',
      feasibility: 'high',
      time_to_impact: 'ongoing',
      icon: '✅'
    });
  }
  
  return actions;
}

/**
 * Calculate potential impact of an action
 */
export function calculateActionImpact(actionType, sources) {
  const impactMap = {
    carpool: sources.traffic * 0.12,
    public_transport: sources.traffic * 0.15,
    stop_burning: sources.open_burning * 0.2,
    report_industry: sources.industry * 0.1
  };
  
  return impactMap[actionType] || 0;
}

