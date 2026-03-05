from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import random
import numpy as np

@dataclass
class Location:
    lat: float
    lng: float
    address: str

@dataclass
class SustainabilityMetrics:
    co2_saved_kg: float
    energy_efficiency_kwh_per_100km: float
    cost_savings_vs_ice: float
    renewable_energy_percentage: float

@dataclass
class Vehicle:
    id: str
    model: str
    battery_capacity_kwh: float
    battery_health: float
    current_charge: float
    mileage: int
    last_service: datetime
    location: Location
    driver_id: str
    status: str
    sustainability_metrics: SustainabilityMetrics

class EnhancedAnalytics:
    def __init__(self):
        self.charging_stations = self._generate_charging_stations()
        
    def _generate_charging_stations(self) -> List[Dict]:
        """Generate realistic charging station data for South Africa"""
        stations = [
            {"id": "CS001", "name": "GridCars Sandton City", "lat": -26.1076, "lng": 28.0567, 
             "fast_charge": True, "available_slots": 4, "total_slots": 6, "cost_per_kwh": 2.85},
            {"id": "CS002", "name": "BMW ChargeNow Rosebank", "lat": -26.1467, "lng": 28.0436,
             "fast_charge": True, "available_slots": 2, "total_slots": 4, "cost_per_kwh": 3.20},
            {"id": "CS003", "name": "Jaguar PowerWay Midrand", "lat": -25.9953, "lng": 28.1294,
             "fast_charge": False, "available_slots": 3, "total_slots": 3, "cost_per_kwh": 2.45},
            {"id": "CS004", "name": "Tesla Supercharger Menlyn", "lat": -25.7879, "lng": 28.2772,
             "fast_charge": True, "available_slots": 8, "total_slots": 12, "cost_per_kwh": 3.50},
            {"id": "CS005", "name": "Audi Charging Hub Centurion", "lat": -25.8601, "lng": 28.1828,
             "fast_charge": True, "available_slots": 1, "total_slots": 8, "cost_per_kwh": 3.15}
        ]
        return stations
    
    def calculate_sustainability_impact(self, vehicles: List[Vehicle]) -> Dict:
        """Calculate fleet-wide sustainability metrics"""
        total_co2_saved = sum(v.sustainability_metrics.co2_saved_kg for v in vehicles)
        avg_efficiency = np.mean([v.sustainability_metrics.energy_efficiency_kwh_per_100km for v in vehicles])
        total_cost_savings = sum(v.sustainability_metrics.cost_savings_vs_ice for v in vehicles)
        avg_renewable = np.mean([v.sustainability_metrics.renewable_energy_percentage for v in vehicles])
        
        return {
            "total_co2_saved_kg": round(total_co2_saved, 1),
            "avg_energy_efficiency": round(avg_efficiency, 1),
            "total_monthly_savings": round(total_cost_savings, 2),
            "renewable_energy_usage": round(avg_renewable, 1),
            "ice_vehicles_equivalent": len(vehicles),
            "trees_equivalent": round(total_co2_saved / 22, 0)  # 1 tree absorbs ~22kg CO2/year
        }
    
    def predict_charging_needs(self, vehicle: Vehicle, route_distance_km: float) -> Dict:
        """Predict charging requirements for a route"""
        energy_needed = route_distance_km * (vehicle.sustainability_metrics.energy_efficiency_kwh_per_100km / 100)
        current_energy = (vehicle.current_charge / 100) * vehicle.battery_capacity_kwh
        
        charging_needed = max(0, energy_needed - current_energy + 10)  # 10kWh buffer
        
        if charging_needed > 0:
            recommended_stations = sorted(
                self.charging_stations,
                key=lambda x: x['available_slots'],
                reverse=True
            )[:3]
        else:
            recommended_stations = []
            
        return {
            "energy_needed_kwh": round(energy_needed, 1),
            "current_energy_kwh": round(current_energy, 1),
            "charging_needed_kwh": round(charging_needed, 1),
            "charging_required": charging_needed > 0,
            "recommended_stations": recommended_stations,
            "estimated_charging_time": round(charging_needed / 50, 1) if charging_needed > 0 else 0  # 50kW charging rate
        }
    
    def generate_fleet_insights(self, vehicles: List[Vehicle]) -> Dict:
        """Generate actionable insights for fleet management"""
        insights = []
        
        # Battery health insights
        low_health_vehicles = [v for v in vehicles if v.battery_health < 80]
        if low_health_vehicles:
            insights.append({
                "type": "battery_health",
                "priority": "high",
                "message": f"{len(low_health_vehicles)} vehicles have battery health below 80%",
                "action": "Schedule battery diagnostics",
                "vehicles": [v.id for v in low_health_vehicles]
            })
        
        # Efficiency insights
        inefficient_vehicles = [v for v in vehicles if v.sustainability_metrics.energy_efficiency_kwh_per_100km > 20]
        if inefficient_vehicles:
            insights.append({
                "type": "efficiency",
                "priority": "medium",
                "message": f"{len(inefficient_vehicles)} vehicles showing poor energy efficiency",
                "action": "Review driving patterns and maintenance",
                "vehicles": [v.id for v in inefficient_vehicles]
            })
        
        # Utilization insights
        idle_vehicles = [v for v in vehicles if v.status == 'idle']
        if len(idle_vehicles) > len(vehicles) * 0.3:
            insights.append({
                "type": "utilization",
                "priority": "medium",
                "message": f"{len(idle_vehicles)} vehicles are idle - consider fleet optimization",
                "action": "Review fleet size and allocation",
                "vehicles": [v.id for v in idle_vehicles]
            })
        
        return {"insights": insights}