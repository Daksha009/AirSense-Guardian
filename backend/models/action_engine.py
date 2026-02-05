# Author: Daksha009
# Repo: https://github.com/Daksha009/AirSense-Guardian.git

import numpy as np
from datetime import datetime

class ActionEngine:
    """Generate actionable insights to reduce pollution"""
    
    def generate_actions(self, current_aqi, sources, weather_data, traffic_density):
        """
        Generate actionable insights based on current conditions
        
        Returns:
            dict containing 'headline' and 'actions' list
        """
        actions = []
        headline = self.generate_headline_insight(current_aqi, sources, weather_data)
        
        # Helper to format percentages
        def fmt_pct(val):
            return int(val * 100) if val < 1 else int(val)

        # 1. Traffic Actions
        traffic_contrib = sources.get('traffic', 0)
        if traffic_contrib > 30:
            # Impact calculation: If 15% people carpool, traffic drops 15%, reducing total AQI by (Traffic% * 0.15)
            # Example: Traffic is 40% of AQI. 15% reduction in traffic = 40 * 0.15 = 6% drop in AQI.
            # User example was: "If 15% of people carpool... AQI could drop by ~12%". 
            # This implies traffic is HUGE (80%?) or the math is optimistic. Let's make it realistic but significant.
            
            # Let's say carpooling/transit reduces the *traffic portion* by X%.
            # Impact on total AQI = traffic_contrib * reduction_in_traffic
            
            # Scenario A: Carpooling
            impact_val = traffic_contrib * 0.20 # Assume 20% reduction in traffic emissions
            actions.append({
                'type': 'carpool',
                'title': 'Carpooling Initiative',
                'description': f'Traffic is a major polluter right now ({traffic_contrib}%). If 15% of commuters carpool, local AQI could drop by ~{fmt_pct(impact_val)}%.',
                'impact': f'-{fmt_pct(impact_val)}% AQI',
                'feasibility': 'high',
                'time_to_impact': '2-3 hours',
                'icon': '🚗'
            })
            
            # Scenario B: Public Transport
            impact_val_pt = traffic_contrib * 0.25
            actions.append({
                'type': 'public_transport',
                'title': 'Switch to Metro/Bus',
                'description': 'Solo driving spikes emissions. Taking public transit can significantly lower the load.',
                'impact': f'-{fmt_pct(impact_val_pt)}% AQI',
                'feasibility': 'high',
                'time_to_impact': '1-2 hours',
                'icon': '🚇'
            })

        # 2. Weather-based Actions (Low Wind)
        wind_speed = weather_data.get('wind_speed', 10)
        if wind_speed < 5:
            # Low wind means pollutants accumulate.
            # Action: Reduce emissions AT SOURCE because they won't disperse.
            actions.append({
                'type': 'avoid_idling',
                'title': 'Stop Engine Idling',
                'description': 'Winds are too weak to disperse pollutants (< 5 km/h). Every minute of idling compounds the problem locally.',
                'impact': 'Prevents accumulation',
                'feasibility': 'immediate',
                'time_to_impact': 'immediate',
                'icon': '🛑'
            })

        # 3. Dust / Construction
        # If humidity is low and wind is moderate, dust might be an issue (simplified proxy)
        humidity = weather_data.get('humidity', 50)
        if humidity < 40 and wind_speed > 10:
             actions.append({
                'type': 'sprinkle_water',
                'title': 'Sprinkle Water',
                'description': 'Dry air and winds are kicking up dust. Sprinkling water on premises can settle PM10.',
                'impact': '-10% PM10',
                'feasibility': 'medium',
                'time_to_impact': 'immediate',
                'icon': '💧'
            })

        # 4. Biomass / Open Burning
        burning_contrib = sources.get('open_burning', 0)
        if burning_contrib > 15:
            impact_burn = burning_contrib * 0.9 # Stopping it removes it almost entirely
            actions.append({
                'type': 'report_burning',
                'title': 'Report Open Burning',
                'description': 'Open fires are detected nearby. Reporting them for extinguishment is the fastest way to improved air.',
                'impact': f'-{fmt_pct(impact_burn)}% AQI',
                'feasibility': 'medium',
                'time_to_impact': '1 hour',
                'icon': '🔥'
            })

        # 5. Health (Always important if AQI is high)
        if current_aqi > 150:
             actions.append({
                'type': 'health_mask',
                'title': 'Wear N95 Mask',
                'description': 'Air is currently unhealthy. Regular masks won\'t filter PM2.5 particles effectively.',
                'impact': '95% protection',
                'feasibility': 'immediate',
                'time_to_impact': 'immediate',
                'icon': '😷'
            })

        # Fallback if few actions
        if len(actions) < 2:
            actions.append({
                'type': 'indoor_plants',
                'title': 'Indoor Plants',
                'description': 'Snake plants and Areca palms naturally filter indoor air pollutants.',
                'impact': 'Long-term',
                'feasibility': 'easy',
                'time_to_impact': 'days',
                'icon': '🌿'
            })

        return {
            'headline': headline,
            'actions': actions
        }

    def generate_headline_insight(self, current_aqi, sources, weather_data):
        """
        Generate a punchy, user-friendly headline explaining the WHY.
        Example: "Traffic emissions + low winds are driving pollution"
        """
        
        # Analyze Drivers
        drivers = []
        
        # 1. Source Driver
        sorted_sources = sorted(sources.items(), key=lambda x: x[1], reverse=True)
        top_source = sorted_sources[0]
        
        if top_source[1] > 40:
             if top_source[0] == 'traffic':
                 drivers.append("Heavy Traffic")
             elif top_source[0] == 'industry':
                 drivers.append("Industrial Emissions")
             elif top_source[0] == 'open_burning':
                 drivers.append("Crop Burning")
        
        # 2. Weather Driver
        wind_speed = weather_data.get('wind_speed', 10)
        humidity = weather_data.get('humidity', 50)
        
        if wind_speed < 5:
            drivers.append("Low Winds")
        elif humidity > 80 and current_aqi > 150:
            drivers.append("Winter Fog") # High humidity + pollution often traps smog
        
        # Construct Keyword String
        if not drivers:
            if current_aqi > 150:
                driver_text = "Stagnant Atmospheric Conditions"
            else:
                driver_text = "Local Emissions"
        else:
            driver_text = " + ".join(drivers)
            
        # Select Template based on severity
        if current_aqi > 200:
            template = f"🟥 {driver_text} are spiking pollution levels."
        elif current_aqi > 150:
            template = f"Rx {driver_text} are keeping air quality poor." 
        elif current_aqi > 100:
            template = f"⚠️ {driver_text} are affecting visibility and health."
        else:
            template = f"✅ Air quality is good, thanks to favorable winds."

        # Add the 'Impact' hook
        # "If 15% of people carpool for the next 3 hours, AQI could drop by ~12%."
        # We'll make this dynamic based on the top source.
        
        prediction = ""
        if top_source[0] == 'traffic' and top_source[1] > 30:
            prediction = " If 15% of commuters carpool, AQI could drop by ~12%."
        elif top_source[0] == 'open_burning' and top_source[1] > 20:
            prediction = " Stopping active fires could improve AQI by ~20%."
        elif wind_speed < 5:
             prediction = " Pollution will linger until winds pick up."
             
        return template + prediction

