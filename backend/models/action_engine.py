import numpy as np
from datetime import datetime

class ActionEngine:
    """Generate actionable insights to reduce pollution"""
    
    def generate_actions(self, current_aqi, sources, weather_data, traffic_density):
        """
        Generate actionable insights based on current conditions
        
        Returns:
            list of action objects with impact estimates
        """
        actions = []
        
        # High traffic contribution
        if sources.get('traffic', 0) > 40:
            actions.append({
                'type': 'carpool',
                'title': 'Promote Carpooling',
                'description': f'If 15% of commuters carpool in the next 2 hours, AQI can drop by ~{int(sources["traffic"] * 0.12)}%',
                'impact': f'{int(sources["traffic"] * 0.12)}% AQI reduction',
                'feasibility': 'high',
                'time_to_impact': '2-3 hours',
                'icon': '🚗'
            })
            
            actions.append({
                'type': 'public_transport',
                'title': 'Use Public Transport',
                'description': 'Switching to public transport reduces vehicle emissions by 60-70%',
                'impact': f'{int(sources["traffic"] * 0.15)}% AQI reduction',
                'feasibility': 'high',
                'time_to_impact': '1-2 hours',
                'icon': '🚌'
            })
        
        # Low wind conditions
        if weather_data.get('wind_speed', 10) < 5:
            actions.append({
                'type': 'reduce_activity',
                'title': 'Reduce Outdoor Activities',
                'description': 'Low wind speed means pollutants are accumulating. Limit outdoor activities and avoid exercising outside.',
                'impact': 'Prevents health issues',
                'feasibility': 'immediate',
                'time_to_impact': 'immediate',
                'icon': '⚠️'
            })
        
        # High AQI overall
        if current_aqi > 150:
            actions.append({
                'type': 'alert_authorities',
                'title': 'Alert Local Authorities',
                'description': 'Notify local environmental agencies about high pollution levels for immediate action',
                'impact': 'Enables regulatory response',
                'feasibility': 'high',
                'time_to_impact': '4-6 hours',
                'icon': '📢'
            })
            
            actions.append({
                'type': 'indoor_air',
                'title': 'Improve Indoor Air Quality',
                'description': 'Close windows, use air purifiers, and avoid activities that generate indoor pollution',
                'impact': 'Protects immediate health',
                'feasibility': 'immediate',
                'time_to_impact': 'immediate',
                'icon': '🏠'
            })
        
        # Industrial contribution
        if sources.get('industry', 0) > 30:
            actions.append({
                'type': 'report_industry',
                'title': 'Report Industrial Emissions',
                'description': 'High industrial contribution detected. Report to environmental monitoring authorities.',
                'impact': 'Enables source control',
                'feasibility': 'medium',
                'time_to_impact': '6-12 hours',
                'icon': '🏭'
            })
        
        # Open burning contribution
        if sources.get('open_burning', 0) > 20:
            actions.append({
                'type': 'stop_burning',
                'title': 'Stop Open Burning',
                'description': 'Open burning detected in area. Report and discourage open waste burning.',
                'impact': f'{int(sources["open_burning"] * 0.2)}% AQI reduction',
                'feasibility': 'medium',
                'time_to_impact': '1-2 hours',
                'icon': '🔥'
            })
        
        # If no specific actions, provide general recommendations
        if len(actions) == 0:
            actions.append({
                'type': 'general',
                'title': 'Maintain Good Air Quality',
                'description': 'Current air quality is acceptable. Continue monitoring and follow best practices.',
                'impact': 'Preventive',
                'feasibility': 'high',
                'time_to_impact': 'ongoing',
                'icon': '✅'
            })
        
        return actions
    
    def calculate_action_impact(self, action_type, current_aqi, sources):
        """Calculate potential impact of an action"""
        impact_map = {
            'carpool': sources.get('traffic', 0) * 0.12,
            'public_transport': sources.get('traffic', 0) * 0.15,
            'stop_burning': sources.get('open_burning', 0) * 0.2,
            'report_industry': sources.get('industry', 0) * 0.1
        }
        
        return impact_map.get(action_type, 0)

