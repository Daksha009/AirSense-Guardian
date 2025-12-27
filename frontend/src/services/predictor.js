/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
/**
 * AQI Prediction Service
 * Uses simple regression model for AQI predictions
 * Can be enhanced with TensorFlow.js or ml.js for more complex models
 */

/**
 * Simple linear regression prediction based on historical patterns
 * In production, this could use a trained TensorFlow.js model
 */
export function predictAQI(currentAQI, windSpeed, humidity, trafficDensity, currentTime, hours = 3) {
  const predictions = [];
  let predictedAQI = currentAQI;

  const hour = currentTime.getHours();
  const dayOfWeek = currentTime.getDay();

  for (let i = 1; i <= hours; i++) {
    const futureTime = new Date(currentTime);
    futureTime.setHours(futureTime.getHours() + i);

    const futureHour = futureTime.getHours();
    const futureDayOfWeek = futureTime.getDay();

    // Simple prediction model based on:
    // - Current AQI (persistence)
    // - Wind speed (dispersal effect)
    // - Traffic patterns (time-based)
    // - Time of day patterns

    // Base prediction starts from current AQI
    let prediction = predictedAQI;

    // Wind effect: higher wind reduces AQI
    prediction -= windSpeed * 1.5;

    // Traffic effect: higher during rush hours
    const isRushHour = (futureHour >= 7 && futureHour <= 9) ||
      (futureHour >= 17 && futureHour <= 19);
    const trafficEffect = isRushHour ? 15 : 5;
    prediction += trafficEffect * trafficDensity;

    // Time of day pattern (sinusoidal)
    const timeEffect = Math.sin((futureHour * Math.PI) / 12) * 20;
    prediction += timeEffect;

    // Weekend effect
    const isWeekend = futureDayOfWeek === 0 || futureDayOfWeek === 6;
    if (isWeekend) {
      prediction -= 10; // Slightly better air quality on weekends
    }

    // Humidity effect: high humidity can trap pollutants
    if (humidity > 70) {
      prediction += 5;
    }

    // Add some randomness for realism
    prediction += (Math.random() * 10 - 5);

    // Clamp to valid AQI range
    prediction = Math.max(0, Math.min(500, prediction));

    predictions.push({
      time: futureTime.toISOString(),
      aqi: Math.round(prediction),
      hours_ahead: i
    });

    // Use predicted AQI for next iteration
    predictedAQI = prediction;
  }

  return predictions;
}

/**
 * Predict AQI for multiple hours ahead
 */
export function predictMultipleHours(currentAQI, windSpeed, humidity, trafficDensity, currentTime, hours = 6) {
  return predictAQI(currentAQI, windSpeed, humidity, trafficDensity, currentTime, hours);
}

/**
 * Get alerts based on current and predicted AQI
 */
export function getAlerts(currentAQI, predictions) {
  const alerts = [];

  // Check current conditions
  if (currentAQI > 150) {
    alerts.push({
      type: 'warning',
      severity: currentAQI > 200 ? 'high' : 'moderate',
      message: `Current AQI is ${Math.round(currentAQI)} - Unhealthy conditions detected`,
      timestamp: new Date().toISOString()
    });
  }

  // Check future predictions
  predictions.forEach(pred => {
    if (pred.aqi > 150) {
      const timeStr = new Date(pred.time).toLocaleTimeString('en-US', {
        hour: '2-digit',
        minute: '2-digit'
      });

      alerts.push({
        type: 'prediction',
        severity: pred.aqi > 200 ? 'high' : 'moderate',
        message: `High AQI (${Math.round(pred.aqi)}) expected at ${timeStr}`,
        timestamp: pred.time,
        aqi: pred.aqi
      });
    }
  });

  return alerts;
}

