/*
 * Author: Daksha009
 * Repo: https://github.com/Daksha009/AirSense-Guardian.git
 */

const BACKEND_URL = 'http://localhost:5000/api';

/**
 * Fetch current AQI data from Backend
 */
export async function getCurrentAQIData(lat, lon) {
  try {
    const url = `${BACKEND_URL}/aqi/current?lat=${lat}&lon=${lon}`;
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Backend API error: ${response.statusText}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data from backend:', error);
    // Fallback or re-throw depending on desired behavior
    throw error;
  }
}

export async function getPredictions(lat, lon, hours = 6) {
  try {
    const response = await fetch(`${BACKEND_URL}/aqi/predict`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ lat, lon, hours })
    });

    if (!response.ok) {
      throw new Error('Failed to fetch predictions');
    }
    return await response.json();
  } catch (error) {
    console.error('Error fetching predictions:', error);
    return { predictions: [] };
  }
}

export async function getAlerts(lat, lon) {
  try {
    const response = await fetch(`${BACKEND_URL}/alerts?lat=${lat}&lon=${lon}`);
    if (!response.ok) throw new Error('Failed to fetch alerts');
    return await response.json();
  } catch (error) {
    console.error('Error fetching alerts:', error);
    return { alerts: [] };
  }
}

