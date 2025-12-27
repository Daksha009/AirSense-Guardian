/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */
/**
 * AQI Data Service - Fetches data from OpenAQ, Weather APIs directly
 * No backend required - pure JavaScript
 */

/**
 * Fetch AQI data from OpenAQ API
 */
export async function fetchOpenAQData(lat, lon) {
  try {
    // First, find nearby locations
    const locationsUrl = `https://api.openaq.org/v2/locations?coordinates=${lat},${lon}&radius=50000&limit=5&order_by=distance`;
    const locationsResponse = await fetch(locationsUrl);

    if (!locationsResponse.ok) {
      throw new Error('Failed to fetch OpenAQ locations');
    }

    const locationsData = await locationsResponse.json();
    const locations = locationsData.results || [];

    if (locations.length === 0) {
      return generateMockAQIData();
    }

    // Get latest measurements from nearest location
    const nearestLocation = locations[0];
    const measurementsUrl = `https://api.openaq.org/v2/locations/${nearestLocation.id}/latest`;
    const measurementsResponse = await fetch(measurementsUrl);

    if (!measurementsResponse.ok) {
      return generateMockAQIData();
    }

    const measurementsData = await measurementsResponse.json();
    const measurements = measurementsData.results || [];

    // Extract AQI values
    let pm25 = 0;
    let pm10 = 0;
    let no2 = 0;

    measurements.forEach(meas => {
      const parameter = meas.parameter?.toLowerCase();
      const value = meas.value || 0;

      if (parameter === 'pm25') pm25 = value;
      else if (parameter === 'pm10') pm10 = value;
      else if (parameter === 'no2') no2 = value;
    });

    // Calculate AQI from PM2.5 and PM10
    const aqi = calculateAQI(pm25, pm10);

    return {
      aqi: aqi || generateRandomAQI(),
      pm25: pm25 || generateRandomPM25(),
      pm10: pm10 || generateRandomPM10(),
      no2: no2 || generateRandomNO2(),
      timestamp: new Date().toISOString(),
      location: { lat, lon }
    };
  } catch (error) {
    console.error('Error fetching OpenAQ data:', error);
    return generateMockAQIData();
  }
}

/**
 * Fetch weather data from OpenWeatherMap API
 * Note: Requires API key in production, uses mock data for demo
 */
export async function fetchWeatherData(lat, lon, apiKey = null) {
  try {
    if (!apiKey) {
      // Use mock data if no API key
      return generateMockWeatherData();
    }

    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${apiKey}&units=metric`;
    const response = await fetch(url);

    if (!response.ok) {
      return generateMockWeatherData();
    }

    const data = await response.json();
    const wind = data.wind || {};
    const main = data.main || {};

    return {
      wind_speed: (wind.speed || 0) * 3.6, // Convert m/s to km/h
      humidity: main.humidity || 60,
      temperature: main.temp || 25,
      pressure: main.pressure || 1013
    };
  } catch (error) {
    console.error('Error fetching weather data:', error);
    return generateMockWeatherData();
  }
}

/**
 * Estimate traffic density based on time of day
 */
export function estimateTrafficDensity(lat, lon) {
  const hour = new Date().getHours();

  // Peak hours: 7-9 AM, 5-7 PM
  let baseDensity = 0.3;
  if ((hour >= 7 && hour <= 9) || (hour >= 17 && hour <= 19)) {
    baseDensity = 0.8;
  } else if (hour >= 10 && hour <= 16) {
    baseDensity = 0.5;
  }

  // Add some randomness
  const density = baseDensity + (Math.random() * 0.2 - 0.1);
  return Math.max(0, Math.min(1, density));
}

/**
 * Calculate US EPA AQI from PM2.5 and PM10
 */
function calculateAQI(pm25, pm10) {
  const aqiPM25 = pm25ToAQI(pm25);
  const aqiPM10 = pm10ToAQI(pm10);
  return Math.max(aqiPM25, aqiPM10);
}

function pm25ToAQI(pm25) {
  if (pm25 <= 12.0) return (pm25 / 12.0) * 50;
  if (pm25 <= 35.4) return 50 + ((pm25 - 12.0) / (35.4 - 12.0)) * 50;
  if (pm25 <= 55.4) return 100 + ((pm25 - 35.4) / (55.4 - 35.4)) * 50;
  if (pm25 <= 150.4) return 150 + ((pm25 - 55.4) / (150.4 - 55.4)) * 50;
  if (pm25 <= 250.4) return 200 + ((pm25 - 150.4) / (250.4 - 150.4)) * 100;
  return 300 + ((pm25 - 250.4) / (350.4 - 250.4)) * 100;
}

function pm10ToAQI(pm10) {
  if (pm10 <= 54) return (pm10 / 54) * 50;
  if (pm10 <= 154) return 50 + ((pm10 - 54) / (154 - 54)) * 50;
  if (pm10 <= 254) return 100 + ((pm10 - 154) / (254 - 154)) * 50;
  if (pm10 <= 354) return 150 + ((pm10 - 254) / (354 - 254)) * 50;
  if (pm10 <= 424) return 200 + ((pm10 - 354) / (424 - 354)) * 100;
  return 300 + ((pm10 - 424) / (504 - 424)) * 100;
}

/**
 * Generate mock data for demo purposes
 */
function generateMockAQIData() {
  return {
    aqi: generateRandomAQI(),
    pm25: generateRandomPM25(),
    pm10: generateRandomPM10(),
    no2: generateRandomNO2(),
    timestamp: new Date().toISOString()
  };
}

function generateMockWeatherData() {
  return {
    wind_speed: 5 + Math.random() * 10,
    humidity: 60 + (Math.random() * 20 - 10),
    temperature: 25 + (Math.random() * 10 - 5),
    pressure: 1013
  };
}

function generateRandomAQI() {
  return 120 + Math.floor(Math.random() * 40 - 20);
}

function generateRandomPM25() {
  return 45 + Math.floor(Math.random() * 20 - 10);
}

function generateRandomPM10() {
  return 80 + Math.floor(Math.random() * 30 - 15);
}

function generateRandomNO2() {
  return 30 + Math.floor(Math.random() * 15 - 10);
}

/**
 * Main function to get all AQI data
 */
export async function getCurrentAQIData(lat, lon, weatherApiKey = null) {
  const [aqiData, weatherData] = await Promise.all([
    fetchOpenAQData(lat, lon),
    fetchWeatherData(lat, lon, weatherApiKey)
  ]);

  const trafficDensity = estimateTrafficDensity(lat, lon);

  return {
    current: {
      ...aqiData,
      location: { lat, lon }
    },
    weather: weatherData,
    traffic_density: trafficDensity
  };
}

