from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import json
from models import Vehicle, Location, SustainabilityMetrics, EnhancedAnalytics

app = Flask(__name__)
CORS(app)

# Mock EV Model Data
models_data = {
    'Scania 25 P': {'battery_kwh': 300, 'efficiency': 110, 'range': 250},
    'Volvo FH Electric': {'battery_kwh': 540, 'efficiency': 115, 'range': 300},
    'Mercedes eActros': {'battery_kwh': 420, 'efficiency': 105, 'range': 400},
    'DAF CF Electric': {'battery_kwh': 315, 'efficiency': 120, 'range': 220}
}

class EVFleetAnalytics:
    def __init__(self):
        self.vehicles = self.generate_mock_fleet()
        self.enhanced_analytics = EnhancedAnalytics()
        self.community_total = 850

    def generate_mock_fleet(self):
        vehicles = []
        drivers = [
            {'id': 'D-SYLVIA', 'name': 'Sylvia Mathe', 'fleet': 'Mathe Fleet'},
            {'id': 'D-JOHN', 'name': 'John Mathe', 'fleet': 'Mathe Fleet'},
            {'id': 'D-MIRIAM', 'name': 'Miriam Mathe', 'fleet': 'Mathe Fleet'},
            {'id': 'D-RON', 'name': 'Ron Mathe', 'fleet': 'Mathe Fleet'}
        ]
        
        for i in range(20):
            model = random.choice(list(models_data.keys()))
            model_data = models_data[model]
            
            # Use RouteMate drivers for the first 4
            if i < len(drivers):
                driver_info = drivers[i]
                driver_id = driver_info['name']
            else:
                driver_id = f'Driver {random.randint(100, 999)}'

            sustainability = SustainabilityMetrics(
                co2_saved_kg=round(random.uniform(150, 300), 1),
                energy_efficiency_kwh_per_100km=model_data['efficiency'] + random.uniform(-2, 2),
                cost_savings_vs_ice=round(random.uniform(800, 1500), 2),
                renewable_energy_percentage=round(random.uniform(60, 95), 1)
            )
            
            vehicle = {
                'id': f'EV-{1000 + i}',
                'model': model,
                'battery_capacity_kwh': model_data['battery_kwh'],
                'battery_health': round(random.uniform(75, 98), 1),
                'current_charge': round(random.uniform(20, 95), 1),
                'mileage': random.randint(5000, 80000),
                'last_service': (datetime.now() - timedelta(days=random.randint(30, 200))).isoformat(),
                'location': {
                    'lat': round(random.uniform(-26.2, -26.1), 4),
                    'lng': round(random.uniform(28.0, 28.1), 4),
                    'address': f'Route {random.randint(1, 50)}, Johannesburg'
                },
                'driver_id': driver_id,
                'status': random.choice(['active', 'active', 'active', 'active', 'charging']), 
                'sustainability_metrics': sustainability.__dict__,
                'fatigue_level': random.choice(['Optimal', 'Optimal', 'High', 'Moderate']),
                'community_score': random.randint(50, 100)
            }
            vehicles.append(vehicle)
        return vehicles
    
    def predict_maintenance(self, vehicle_id):
        """Predict maintenance needs using mock ML model"""
        vehicle = next((v for v in self.vehicles if v['id'] == vehicle_id), None)
        if not vehicle:
            return None
            
        # Mock predictive model based on battery health, mileage, and last service
        days_since_service = (datetime.now() - datetime.fromisoformat(vehicle['last_service'])).days
        
        risk_score = 0
        if vehicle['battery_health'] < 85:
            risk_score += 30
        if days_since_service > 90:
            risk_score += 25
        if vehicle['mileage'] > 50000:
            risk_score += 20
        if vehicle['current_charge'] < 30:
            risk_score += 15
            
        maintenance_type = []
        if vehicle['battery_health'] < 80:
            maintenance_type.append('Battery Check')
        if days_since_service > 120:
            maintenance_type.append('General Service')
        if vehicle['mileage'] > 60000:
            maintenance_type.append('Brake Inspection')
            
        return {
            'vehicle_id': vehicle_id,
            'risk_score': min(risk_score, 100),
            'priority': 'High' if risk_score > 60 else 'Medium' if risk_score > 30 else 'Low',
            'predicted_maintenance': maintenance_type or ['Routine Check'],
            'estimated_days': max(1, 30 - (risk_score // 3))
        }
    
    def predict_performance(self, vehicle_id):
        """Predict vehicle performance metrics"""
        vehicle = next((v for v in self.vehicles if v['id'] == vehicle_id), None)
        if not vehicle:
            return None
            
        # Mock performance prediction
        efficiency_score = vehicle['battery_health'] * 0.8 + (100 - vehicle['current_charge']) * 0.2
        
        return {
            'vehicle_id': vehicle_id,
            'efficiency_score': round(efficiency_score, 1),
            'predicted_range': round(vehicle['current_charge'] * 4.2, 0),  # Mock: 4.2km per %
            'energy_consumption': round(random.uniform(15, 25), 1),  # kWh/100km
            'cost_per_km': round(random.uniform(0.8, 1.5), 2),
            'sustainability_score': round(random.uniform(85, 98), 1)
        }
    
    def optimize_route(self, start_location, end_location, vehicle_id):
        """Provide route optimization with charging station recommendations"""
        vehicle = next((v for v in self.vehicles if v['id'] == vehicle_id), None)
        
        # Mock route optimization
        distance = random.uniform(50, 200)  # km
        charging_needed = vehicle['current_charge'] < 30 if vehicle else True
        
        charging_stations = [
            {'name': 'GridCars Sandton', 'lat': -26.1076, 'lng': 28.0567, 'fast_charge': True},
            {'name': 'BMW ChargeNow Rosebank', 'lat': -26.1467, 'lng': 28.0436, 'fast_charge': True},
            {'name': 'Jaguar PowerWay Midrand', 'lat': -25.9953, 'lng': 28.1294, 'fast_charge': False}
        ]
        
        return {
            'vehicle_id': vehicle_id,
            'route': {
                'distance_km': round(distance, 1),
                'estimated_time': round(distance / 60, 1),  # hours
                'energy_required': round(distance * 0.2, 1),  # kWh
                'charging_needed': charging_needed
            },
            'recommended_stations': charging_stations[:2] if charging_needed else [],
            'alternative_routes': [
                {'name': 'Fastest Route', 'time_savings': '15 min', 'extra_distance': '5 km'},
                {'name': 'Most Efficient', 'energy_savings': '12%', 'extra_time': '8 min'}
            ]
        }

# Initialize analytics engine
analytics = EVFleetAnalytics()

@app.route('/api/fleet', methods=['GET'])
def get_fleet():
    """Get all vehicles in the fleet"""
    return jsonify(analytics.vehicles)

@app.route('/api/vehicle/<vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    """Get specific vehicle details"""
    vehicle = next((v for v in analytics.vehicles if v['id'] == vehicle_id), None)
    if vehicle:
        return jsonify(vehicle)
    return jsonify({'error': 'Vehicle not found'}), 404

@app.route('/api/maintenance/predict/<vehicle_id>', methods=['GET'])
def predict_maintenance(vehicle_id):
    """Get maintenance predictions for a vehicle"""
    prediction = analytics.predict_maintenance(vehicle_id)
    if prediction:
        return jsonify(prediction)
    return jsonify({'error': 'Vehicle not found'}), 404

@app.route('/api/performance/predict/<vehicle_id>', methods=['GET'])
def predict_performance(vehicle_id):
    """Get performance predictions for a vehicle"""
    prediction = analytics.predict_performance(vehicle_id)
    if prediction:
        return jsonify(prediction)
    return jsonify({'error': 'Vehicle not found'}), 404

@app.route('/api/route/optimize', methods=['POST'])
def optimize_route():
    """Optimize route for a vehicle"""
    data = request.json
    vehicle_id = data.get('vehicle_id')
    start = data.get('start_location')
    end = data.get('end_location')
    
    optimization = analytics.optimize_route(start, end, vehicle_id)
    return jsonify(optimization)

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    """Get all active alerts for the fleet"""
    alerts = []
    for vehicle in analytics.vehicles:
        maintenance = analytics.predict_maintenance(vehicle['id'])
        if maintenance['priority'] in ['High', 'Medium']:
            alerts.append({
                'id': f"alert_{vehicle['id']}",
                'vehicle_id': vehicle['id'],
                'type': 'maintenance',
                'priority': maintenance['priority'],
                'message': f"Vehicle {vehicle['id']} requires {', '.join(maintenance['predicted_maintenance'])}",
                'timestamp': datetime.now().isoformat()
            })
        
        if vehicle['current_charge'] < 25:
            alerts.append({
                'id': f"charge_{vehicle['id']}",
                'vehicle_id': vehicle['id'],
                'type': 'charging',
                'priority': 'High',
                'message': f"Vehicle {vehicle['id']} has low battery ({vehicle['current_charge']}%)",
                'timestamp': datetime.now().isoformat()
            })
    
    return jsonify(alerts)

@app.route('/api/dashboard/summary', methods=['GET'])
def dashboard_summary():
    """Get dashboard summary statistics"""
    total_vehicles = len(analytics.vehicles)
    active_vehicles = len([v for v in analytics.vehicles if v['status'] == 'active'])
    charging_vehicles = len([v for v in analytics.vehicles if v['status'] == 'charging'])
    maintenance_vehicles = len([v for v in analytics.vehicles if v['status'] == 'maintenance'])
    
    avg_battery_health = sum(v['battery_health'] for v in analytics.vehicles) / total_vehicles
    avg_charge_level = sum(v['current_charge'] for v in analytics.vehicles) / total_vehicles
    
    # Calculate sustainability impact
    vehicle_objects = []
    for v_data in analytics.vehicles:
        sustainability = SustainabilityMetrics(**v_data['sustainability_metrics'])
        location = Location(**v_data['location'])
        vehicle = Vehicle(
            id=v_data['id'], model=v_data['model'], 
            battery_capacity_kwh=v_data['battery_capacity_kwh'],
            battery_health=v_data['battery_health'], current_charge=v_data['current_charge'],
            mileage=v_data['mileage'], last_service=datetime.fromisoformat(v_data['last_service']),
            location=location, driver_id=v_data['driver_id'], status=v_data['status'],
            sustainability_metrics=sustainability
        )
        vehicle_objects.append(vehicle)
    
    sustainability_impact = analytics.enhanced_analytics.calculate_sustainability_impact(vehicle_objects)
    
    return jsonify({
        'total_vehicles': total_vehicles,
        'active_vehicles': active_vehicles,
        'charging_vehicles': charging_vehicles,
        'maintenance_vehicles': maintenance_vehicles,
        'avg_battery_health': round(avg_battery_health, 1),
        'avg_charge_level': round(avg_charge_level, 1),
        'sustainability_impact': sustainability_impact,
        'community_points': analytics.community_total if hasattr(analytics, 'community_total') else 850
    })

@app.route('/api/sustainability/impact', methods=['GET'])
def get_sustainability_impact():
    """Get comprehensive sustainability metrics for the fleet"""
    vehicle_objects = []
    for v_data in analytics.vehicles:
        sustainability = SustainabilityMetrics(**v_data['sustainability_metrics'])
        location = Location(**v_data['location'])
        vehicle = Vehicle(
            id=v_data['id'], model=v_data['model'], 
            battery_capacity_kwh=v_data['battery_capacity_kwh'],
            battery_health=v_data['battery_health'], current_charge=v_data['current_charge'],
            mileage=v_data['mileage'], last_service=datetime.fromisoformat(v_data['last_service']),
            location=location, driver_id=v_data['driver_id'], status=v_data['status'],
            sustainability_metrics=sustainability
        )
        vehicle_objects.append(vehicle)
    
    impact = analytics.enhanced_analytics.calculate_sustainability_impact(vehicle_objects)
    return jsonify(impact)

@app.route('/api/charging/stations', methods=['GET'])
def get_charging_stations():
    """Get all available charging stations"""
    return jsonify(analytics.enhanced_analytics.charging_stations)

@app.route('/api/charging/predict/<vehicle_id>', methods=['POST'])
def predict_charging_needs(vehicle_id):
    """Predict charging needs for a specific route"""
    data = request.json
    route_distance = data.get('route_distance_km', 100)
    
    vehicle_data = next((v for v in analytics.vehicles if v['id'] == vehicle_id), None)
    if not vehicle_data:
        return jsonify({'error': 'Vehicle not found'}), 404
    
    # Convert to Vehicle object
    sustainability = SustainabilityMetrics(**vehicle_data['sustainability_metrics'])
    location = Location(**vehicle_data['location'])
    vehicle = Vehicle(
        id=vehicle_data['id'], model=vehicle_data['model'],
        battery_capacity_kwh=vehicle_data['battery_capacity_kwh'],
        battery_health=vehicle_data['battery_health'], current_charge=vehicle_data['current_charge'],
        mileage=vehicle_data['mileage'], last_service=datetime.fromisoformat(vehicle_data['last_service']),
        location=location, driver_id=vehicle_data['driver_id'], status=vehicle_data['status'],
        sustainability_metrics=sustainability
    )
    
    prediction = analytics.enhanced_analytics.predict_charging_needs(vehicle, route_distance)
    return jsonify(prediction)

@app.route('/api/insights', methods=['GET'])
def get_fleet_insights():
    """Get actionable insights for fleet management"""
    vehicle_objects = []
    for v_data in analytics.vehicles:
        sustainability = SustainabilityMetrics(**v_data['sustainability_metrics'])
        location = Location(**v_data['location'])
        vehicle = Vehicle(
            id=v_data['id'], model=v_data['model'],
            battery_capacity_kwh=v_data['battery_capacity_kwh'],
            battery_health=v_data['battery_health'], current_charge=v_data['current_charge'],
            mileage=v_data['mileage'], last_service=datetime.fromisoformat(v_data['last_service']),
            location=location, driver_id=v_data['driver_id'], status=v_data['status'],
            sustainability_metrics=sustainability
        )
        vehicle_objects.append(vehicle)
    
    insights = analytics.enhanced_analytics.generate_fleet_insights(vehicle_objects)
    return jsonify(insights)

if __name__ == '__main__':
    app.run(debug=True, port=5000)