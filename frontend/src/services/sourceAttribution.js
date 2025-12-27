/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
/**
 * Source Attribution Service
 * Identifies pollution sources based on AQI, weather, and traffic patterns
 */

/**
 * Attribute pollution sources based on current conditions
 * @param {number} aqi - Current AQI
 * @param {number} windSpeed - Wind speed in km/h
 * @param {number} trafficDensity - Traffic density (0-1)
 * @param {number} hour - Current hour (0-23)
 * @returns {Object} Source percentages
 */
export function attributeSources(aqi, windSpeed, trafficDensity, hour) {
  // Base attribution
  const sources = {
    traffic: 0.0,
    industry: 0.0,
    open_burning: 0.0,
    other: 0.0
  };

  // High traffic + low wind = vehicle pollution
  if (trafficDensity > 0.6 && windSpeed < 5) {
    sources.traffic = Math.min(0.6, 0.3 + trafficDensity * 0.3);
  }

  // Night spikes (10 PM - 6 AM) = industrial activity
  if ((hour >= 22 || hour < 6) && aqi > 100) {
    sources.industry = Math.min(0.4, 0.2 + (aqi - 100) / 200);
  }

  // Low wind + high AQI = open burning / stagnant air
  if (windSpeed < 3 && aqi > 120) {
    sources.open_burning = Math.min(0.3, 0.15 + (aqi - 120) / 300);
  }

  // Normalize to ensure total is reasonable
  const total = Object.values(sources).reduce((sum, val) => sum + val, 0);

  if (total < 0.5) {
    // If attribution is low, distribute based on AQI level
    if (aqi > 150) {
      sources.traffic = 0.5;
      sources.industry = 0.2;
      sources.open_burning = 0.2;
      sources.other = 0.1;
    } else {
      sources.traffic = 0.4;
      sources.industry = 0.2;
      sources.open_burning = 0.2;
      sources.other = 0.2;
    }
  } else {
    // Normalize to 100%
    const factor = 1.0 / total;
    Object.keys(sources).forEach(key => {
      sources[key] *= factor;
    });
  }

  // Round to 1 decimal place and convert to percentage
  Object.keys(sources).forEach(key => {
    sources[key] = Math.round(sources[key] * 100 * 10) / 10;
  });

  return sources;
}

/**
 * Get human-readable description of primary source
 */
export function getSourceDescription(sources) {
  const entries = Object.entries(sources);
  const maxSource = entries.reduce((max, current) =>
    current[1] > max[1] ? current : max
  );

  const sourceName = maxSource[0].replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
  const percentage = maxSource[1];

  return `${sourceName} contributes ${percentage}% to current pollution levels`;
}

