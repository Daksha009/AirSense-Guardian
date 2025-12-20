/**
 * Main service module - exports all services
 * This is the entry point for all backend logic
 */

import { getCurrentAQIData } from './aqiService';
import { attributeSources } from './sourceAttribution';
import { predictAQI, predictMultipleHours, getAlerts } from './predictor';
import { generateActions } from './actionEngine';

/**
 * Get complete AQI data with all analysis
 * This replaces the Flask backend endpoint
 */
export async function getCompleteAQIData(lat, lon, weatherApiKey = null) {
  try {
    // Fetch AQI and weather data
    const { current, weather, traffic_density } = await getCurrentAQIData(lat, lon, weatherApiKey);
    
    const hour = new Date().getHours();
    
    // Get source attribution
    const sources = attributeSources(
      current.aqi,
      weather.wind_speed,
      traffic_density,
      hour
    );
    
    // Get predictions
    const predictions = predictAQI(
      current.aqi,
      weather.wind_speed,
      weather.humidity,
      traffic_density,
      new Date(),
      3
    );
    
    // Get actionable insights
    const actions = generateActions(
      current.aqi,
      sources,
      weather,
      traffic_density
    );
    
    // Get alerts
    const alerts = getAlerts(current.aqi, predictions);
    
    return {
      current: {
        ...current,
        timestamp: new Date().toISOString()
      },
      weather,
      traffic_density,
      sources,
      predictions,
      actions,
      alerts
    };
  } catch (error) {
    console.error('Error getting complete AQI data:', error);
    throw error;
  }
}

/**
 * Get alerts for a location
 */
export async function getLocationAlerts(lat, lon, weatherApiKey = null) {
  try {
    const { current, weather, traffic_density } = await getCurrentAQIData(lat, lon, weatherApiKey);
    const predictions = predictMultipleHours(
      current.aqi,
      weather.wind_speed,
      weather.humidity,
      traffic_density,
      new Date(),
      6
    );
    
    return getAlerts(current.aqi, predictions);
  } catch (error) {
    console.error('Error getting alerts:', error);
    return [];
  }
}

// Export individual services for direct use if needed
export { getCurrentAQIData } from './aqiService';
export { attributeSources } from './sourceAttribution';
export { predictAQI, predictMultipleHours, getAlerts } from './predictor';
export { generateActions } from './actionEngine';

