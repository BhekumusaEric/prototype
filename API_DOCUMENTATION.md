# WesBank FML EV Fleet Analytics - API Documentation

## Overview
This document provides comprehensive API documentation for the WesBank FML EV Fleet Analytics System prototype.

## Base URL
```
http://localhost:5000/api
```

## Authentication
Currently, no authentication is required for this prototype. In production, implement proper API key or OAuth authentication.

## Endpoints

### Fleet Management

#### GET /fleet
Get all vehicles in the fleet with enhanced sustainability metrics.

**Response:**
```json
[
  {
    "id": "EV-1001",
    "model": "Tesla Model 3",
    "battery_capacity_kwh": 75,
    "battery_health": 92.5,
    "current_charge": 78.0,
    "mileage": 25000,
    "last_service": "2024-01-15T10:30:00",
    "location": {
      "lat": -26.1076,
      "lng": 28.0567,
      "address": "Route 15, Johannesburg"
    },
    "driver_id": "D123",
    "status": "active",
    "sustainability_metrics": {
      "co2_saved_kg": 245.8,
      "energy_efficiency_kwh_per_100km": 16.2,
      "cost_savings_vs_ice": 1250.50,
      "renewable_energy_percentage": 85.3
    }
  }
]
```

#### GET /vehicle/{id}
Get specific vehicle details.

**Parameters:**
- `id` (string): Vehicle ID (e.g., "EV-1001")

**Response:**
```json
{
  "id": "EV-1001",
  "model": "Tesla Model 3",
  "battery_capacity_kwh": 75,
  "battery_health": 92.5,
  "current_charge": 78.0,
  "mileage": 25000,
  "last_service": "2024-01-15T10:30:00",
  "location": {
    "lat": -26.1076,
    "lng": 28.0567,
    "address": "Route 15, Johannesburg"
  },
  "driver_id": "D123",
  "status": "active",
  "sustainability_metrics": {
    "co2_saved_kg": 245.8,
    "energy_efficiency_kwh_per_100km": 16.2,
    "cost_savings_vs_ice": 1250.50,
    "renewable_energy_percentage": 85.3
  }
}
```

### Dashboard & Analytics

#### GET /dashboard/summary
Get comprehensive dashboard statistics including sustainability impact.

**Response:**
```json
{
  "total_vehicles": 20,
  "active_vehicles": 15,
  "charging_vehicles": 3,
  "maintenance_vehicles": 2,
  "avg_battery_health": 89.2,
  "avg_charge_level": 67.8,
  "sustainability_impact": {
    "total_co2_saved_kg": 4850.2,
    "avg_energy_efficiency": 17.8,
    "total_monthly_savings": 24500.75,
    "renewable_energy_usage": 82.5,
    "ice_vehicles_equivalent": 20,
    "trees_equivalent": 220
  }
}
```

#### GET /sustainability/impact
Get detailed sustainability metrics for the entire fleet.

**Response:**
```json
{
  "total_co2_saved_kg": 4850.2,
  "avg_energy_efficiency": 17.8,
  "total_monthly_savings": 24500.75,
  "renewable_energy_usage": 82.5,
  "ice_vehicles_equivalent": 20,
  "trees_equivalent": 220
}
```

### Predictive Analytics

#### GET /maintenance/predict/{id}
Get maintenance predictions for a specific vehicle.

**Parameters:**
- `id` (string): Vehicle ID

**Response:**
```json
{
  "vehicle_id": "EV-1001",
  "risk_score": 45,
  "priority": "Medium",
  "predicted_maintenance": ["Battery Check", "General Service"],
  "estimated_days": 21
}
```

#### GET /performance/predict/{id}
Get performance predictions for a specific vehicle.

**Parameters:**
- `id` (string): Vehicle ID

**Response:**
```json
{
  "vehicle_id": "EV-1001",
  "efficiency_score": 87.5,
  "predicted_range": 327,
  "energy_consumption": 16.8,
  "cost_per_km": 1.25,
  "sustainability_score": 92.3
}
```

### Alerts & Insights

#### GET /alerts
Get all active alerts for the fleet.

**Response:**
```json
[
  {
    "id": "alert_EV-1001",
    "vehicle_id": "EV-1001",
    "type": "maintenance",
    "priority": "High",
    "message": "Vehicle EV-1001 requires Battery Check, General Service",
    "timestamp": "2024-01-20T14:30:00"
  },
  {
    "id": "charge_EV-1005",
    "vehicle_id": "EV-1005",
    "type": "charging",
    "priority": "High",
    "message": "Vehicle EV-1005 has low battery (18%)",
    "timestamp": "2024-01-20T14:25:00"
  }
]
```

#### GET /insights
Get actionable insights for fleet management.

**Response:**
```json
{
  "insights": [
    {
      "type": "battery_health",
      "priority": "high",
      "message": "3 vehicles have battery health below 80%",
      "action": "Schedule battery diagnostics",
      "vehicles": ["EV-1003", "EV-1007", "EV-1012"]
    },
    {
      "type": "efficiency",
      "priority": "medium",
      "message": "5 vehicles showing poor energy efficiency",
      "action": "Review driving patterns and maintenance",
      "vehicles": ["EV-1002", "EV-1008", "EV-1015", "EV-1018", "EV-1020"]
    }
  ]
}
```

### Charging Management

#### GET /charging/stations
Get all available charging stations.

**Response:**
```json
[
  {
    "id": "CS001",
    "name": "GridCars Sandton City",
    "lat": -26.1076,
    "lng": 28.0567,
    "fast_charge": true,
    "available_slots": 4,
    "total_slots": 6,
    "cost_per_kwh": 2.85
  },
  {
    "id": "CS002",
    "name": "BMW ChargeNow Rosebank",
    "lat": -26.1467,
    "lng": 28.0436,
    "fast_charge": true,
    "available_slots": 2,
    "total_slots": 4,
    "cost_per_kwh": 3.20
  }
]
```

#### POST /charging/predict/{id}
Predict charging needs for a specific route.

**Parameters:**
- `id` (string): Vehicle ID

**Request Body:**
```json
{
  "route_distance_km": 150.5
}
```

**Response:**
```json
{
  "energy_needed_kwh": 25.2,
  "current_energy_kwh": 58.5,
  "charging_needed_kwh": 0,
  "charging_required": false,
  "recommended_stations": [],
  "estimated_charging_time": 0
}
```

### Route Optimization

#### POST /route/optimize
Optimize route for a vehicle with charging considerations.

**Request Body:**
```json
{
  "vehicle_id": "EV-1001",
  "start_location": "Sandton",
  "end_location": "Cape Town"
}
```

**Response:**
```json
{
  "vehicle_id": "EV-1001",
  "route": {
    "distance_km": 142.5,
    "estimated_time": 2.4,
    "energy_required": 28.5,
    "charging_needed": true
  },
  "recommended_stations": [
    {
      "name": "GridCars Sandton",
      "lat": -26.1076,
      "lng": 28.0567,
      "fast_charge": true
    }
  ],
  "alternative_routes": [
    {
      "name": "Fastest Route",
      "time_savings": "15 min",
      "extra_distance": "5 km"
    },
    {
      "name": "Most Efficient",
      "energy_savings": "12%",
      "extra_time": "8 min"
    }
  ]
}
```

## Error Responses

All endpoints return appropriate HTTP status codes:

- `200 OK`: Successful request
- `404 Not Found`: Resource not found
- `400 Bad Request`: Invalid request parameters
- `500 Internal Server Error`: Server error

**Error Response Format:**
```json
{
  "error": "Vehicle not found"
}
```

## Rate Limiting
Currently no rate limiting is implemented in this prototype. For production, implement appropriate rate limiting based on API key or IP address.

## Data Models

### Vehicle Status Values
- `active`: Vehicle is operational and in use
- `charging`: Vehicle is currently charging
- `maintenance`: Vehicle is undergoing maintenance
- `idle`: Vehicle is available but not in use

### Priority Levels
- `High`: Immediate attention required
- `Medium`: Attention needed within a few days
- `Low`: Routine maintenance or monitoring

### Alert Types
- `maintenance`: Maintenance-related alerts
- `charging`: Battery/charging-related alerts
- `performance`: Performance-related alerts

## Testing

Use tools like Postman, curl, or any HTTP client to test the API endpoints:

```bash
# Get all vehicles
curl http://localhost:5000/api/fleet

# Get specific vehicle
curl http://localhost:5000/api/vehicle/EV-1001

# Get dashboard summary
curl http://localhost:5000/api/dashboard/summary

# Optimize route
curl -X POST http://localhost:5000/api/route/optimize \
  -H "Content-Type: application/json" \
  -d '{"vehicle_id":"EV-1001","start_location":"Sandton","end_location":"Cape Town"}'
```

## Future Enhancements

1. **Authentication**: Implement JWT or API key authentication
2. **Real-time Updates**: WebSocket support for live data updates
3. **Geofencing**: Location-based alerts and restrictions
4. **Advanced Analytics**: Machine learning models for better predictions
5. **Integration**: Connect with real vehicle telematics systems
6. **Mobile API**: Optimized endpoints for mobile applications