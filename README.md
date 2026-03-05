# WesBank FML EV Fleet Analytics System

A comprehensive predictive analytics system for electric vehicle fleet management, designed to provide maintenance alerts, performance predictions, and route optimization for WesBank FML clients.

## Features

### 🔮 Predictive Analytics
- **Maintenance Predictions**: AI-powered maintenance scheduling based on battery health, mileage, and usage patterns
- **Performance Optimization**: Real-time efficiency scoring and range predictions
- **Cost Analysis**: Sustainability metrics and cost savings vs ICE vehicles

### 🚗 Fleet Management
- **Real-time Monitoring**: Live vehicle status, battery levels, and location tracking
- **Alert System**: Proactive notifications for maintenance needs and low battery warnings
- **Driver Management**: Vehicle-driver assignments and performance tracking

### 🗺️ Route Optimization
- **Smart Routing**: Optimized routes considering battery levels and charging infrastructure
- **Charging Station Integration**: Recommendations for charging stops along routes
- **Alternative Routes**: Multiple route options with time/energy trade-offs

### 📊 Dashboard Features
- **Executive Summary**: High-level fleet metrics and KPIs
- **Vehicle Details**: Comprehensive vehicle information and predictions
- **Interactive Filtering**: Search and filter vehicles by status, model, or driver
- **Real-time Updates**: Auto-refreshing data every 30 seconds

## Technology Stack

### Backend
- **Python Flask**: RESTful API server
- **Pandas & NumPy**: Data processing and analytics
- **Scikit-learn**: Machine learning models (mock implementation)

### Frontend
- **HTML5/CSS3**: Responsive web interface
- **Vanilla JavaScript**: Interactive dashboard functionality
- **Font Awesome**: Icons and visual elements

## Quick Start

### Prerequisites
- Python 3.8+
- Modern web browser

### Installation

1. **Clone/Download the project**
   ```bash
   cd /home/wtc/prototype
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend server**
   ```bash
   python app.py
   ```
   Server will start on `http://localhost:5000`

4. **Open the dashboard**
   Open `index.html` in your web browser or serve it via a local server:
   ```bash
   # Option 1: Direct file opening
   open index.html
   
   # Option 2: Simple HTTP server
   python -m http.server 8080
   # Then visit http://localhost:8080
   ```

## API Endpoints

### Fleet Management
- `GET /api/fleet` - Get all vehicles
- `GET /api/vehicle/{id}` - Get specific vehicle details
- `GET /api/dashboard/summary` - Get dashboard statistics

### Predictive Analytics
- `GET /api/maintenance/predict/{id}` - Get maintenance predictions
- `GET /api/performance/predict/{id}` - Get performance metrics
- `GET /api/alerts` - Get active alerts

### Route Optimization
- `POST /api/route/optimize` - Optimize route for vehicle
  ```json
  {
    "vehicle_id": "EV-1001",
    "start_location": "Sandton",
    "end_location": "Cape Town"
  }
  ```

## Mock Data Structure

### Vehicle Data
```json
{
  "id": "EV-1001",
  "model": "Tesla Model 3",
  "battery_health": 92.5,
  "current_charge": 78.0,
  "mileage": 25000,
  "status": "active",
  "location": {
    "lat": -26.1076,
    "lng": 28.0567,
    "address": "Sandton, Johannesburg"
  },
  "driver_id": "D123"
}
```

### Maintenance Prediction
```json
{
  "vehicle_id": "EV-1001",
  "risk_score": 45,
  "priority": "Medium",
  "predicted_maintenance": ["Battery Check", "General Service"],
  "estimated_days": 21
}
```

## Sustainability Features

### Environmental Impact
- **Carbon Footprint Tracking**: Monitor CO2 savings vs traditional vehicles
- **Energy Efficiency**: Track kWh consumption and optimization opportunities
- **Sustainability Scoring**: Overall environmental performance metrics

### Cost Benefits
- **Operational Savings**: Reduced fuel and maintenance costs
- **Incentive Tracking**: Government rebates and tax benefits
- **ROI Analysis**: Return on investment for EV transition

## Figma Integration

This prototype is designed to be easily transferred to Figma:

### Design System
- **Color Palette**: Modern gradient backgrounds with clean white cards
- **Typography**: Segoe UI font family for consistency
- **Icons**: Font Awesome icons (can be replaced with custom SVGs)
- **Layout**: CSS Grid and Flexbox for responsive design

### Component Structure
- **Header**: Logo, navigation, and key metrics
- **Alert Cards**: Color-coded priority system
- **Data Cards**: Modular design for different data types
- **Modal System**: Detailed vehicle information overlay

### Export Recommendations
1. **Screenshots**: Capture different states (alerts, vehicle details, route optimization)
2. **Component Library**: Extract reusable UI components
3. **Responsive Views**: Mobile, tablet, and desktop layouts
4. **Interactive Prototypes**: Use Figma's prototyping features for user flows

## Future Enhancements

### Advanced Analytics
- **Machine Learning**: Real predictive models using historical data
- **IoT Integration**: Direct vehicle telemetry integration
- **Weather Integration**: Route optimization considering weather conditions

### Business Intelligence
- **Advanced Reporting**: Custom dashboards and reports
- **Fleet Optimization**: AI-powered fleet size and composition recommendations
- **Predictive Maintenance**: Integration with OEM maintenance systems

### Integration Capabilities
- **ERP Systems**: SAP, Oracle integration for fleet management
- **Telematics**: Integration with existing fleet tracking systems
- **Charging Networks**: Real-time charging station availability

## Support

This is a prototype system with mock data. For production deployment:
- Replace mock data with real vehicle telemetry
- Implement proper authentication and authorization
- Add database persistence
- Integrate with actual charging station APIs
- Implement proper error handling and logging

## License

Prototype for WesBank FML - Internal Use Only