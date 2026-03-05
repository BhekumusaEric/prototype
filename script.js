class RouteMateDashboard {
    constructor() {
        this.apiBase = 'http://localhost:5000/api';
        this.vehicles = [];
        this.alerts = [];
        this.buddies = [
            { id: 'SYLVIA', name: 'Sylvia Mathe', status: 'Online', fleet: 'Mathe Fleet', distance: '1.2km' },
            { id: 'JOHN', name: 'John Mathe', status: 'Nearby', fleet: 'Mathe Fleet', distance: '3.5km' },
            { id: 'MIRIAM', name: 'Miriam Mathe', status: 'Driving', fleet: 'Mathe Fleet', distance: '8.1km' },
            { id: 'RON', name: 'Ron Mathe', status: 'Rest Stop', fleet: 'Mathe Fleet', distance: '12km' }
        ];
        this.communityScore = 850;
        this.init();
    }

    async init() {
        await this.loadDashboardData();
        this.renderBuddyList();
        this.setupEventListeners();
        this.startAutoRefresh();
        this.simulateFatigueMonitoring();
    }

    switchView(viewId) {
        // Toggle view sections
        document.querySelectorAll('.view-section').forEach(section => {
            section.classList.add('hidden');
        });
        document.getElementById(`${viewId}View`).classList.remove('hidden');

        // Toggle nav buttons
        document.querySelectorAll('.nav-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        event.currentTarget.classList.add('active');
    }

    async loadDashboardData() {
        try {
            const [summary, vehicles, alerts, insights] = await Promise.all([
                this.fetchData('/dashboard/summary'),
                this.fetchData('/fleet'),
                this.fetchData('/alerts'),
                this.fetchData('/insights')
            ]);

            this.updateHeaderStats(summary);
            this.vehicles = vehicles;
            this.alerts = alerts;

            this.renderAlerts();
            this.renderVehicleList();
            this.renderFleetInsights(insights);
            this.populateRouteVehicles();

        } catch (error) {
            console.error('Error loading dashboard data:', error);
        }
    }

    async fetchData(endpoint) {
        try {
            const response = await fetch(`${this.apiBase}${endpoint}`);
            if (!response.ok) return this.getMockData(endpoint);
            return await response.json();
        } catch (e) {
            return this.getMockData(endpoint);
        }
    }

    getMockData(endpoint) {
        // Fallback mock data for demo purposes
        if (endpoint === '/fleet') return [
            { id: 'V-001', model: 'Scania EV', status: 'active', battery_health: 98, current_charge: 75, location: { address: 'N1 North, Midrand' }, driver_id: 'You' },
            { id: 'V-002', model: 'Volvo Electric', status: 'active', battery_health: 95, current_charge: 40, location: { address: 'M1 South, JHB' }, driver_id: 'Sylvia' }
        ];
        if (endpoint === '/dashboard/summary') return { total_vehicles: 12, active_vehicles: 8, charging_vehicles: 2, maintenance_vehicles: 2, avg_battery_health: 92 };
        if (endpoint === '/insights') return {
            insights: [
                { type: 'Safety', priority: 'high', message: 'High crosswinds detected on N3 route.', action: 'Advise drivers to maintain safe distance.', vehicles: ['V-004', 'V-007'] }
            ]
        };
        return [];
    }

    updateHeaderStats(summary) {
        document.getElementById('activeVehicles').textContent = `${summary.active_vehicles} connected`;
        document.getElementById('communityPoints').textContent = this.communityScore.toLocaleString();
    }

    renderBuddyList() {
        const container = document.getElementById('buddyList');
        container.innerHTML = this.buddies.map(buddy => `
            <div class="buddy-item" onclick="dashboard.contactBuddy('${buddy.id}')">
                <div class="buddy-avatar">${buddy.name.charAt(0)}</div>
                <div class="buddy-info">
                    <span class="buddy-name">${buddy.name}</span>
                    <span class="buddy-status">${buddy.status} • ${buddy.distance}</span>
                </div>
            </div>
        `).join('');
    }

    renderFleetInsights(insightsData) {
        const container = document.getElementById('insightsContainer');
        const insights = insightsData.insights;

        container.innerHTML = insights.map(insight => `
            <div class="insight-item ${insight.priority}">
                <div class="insight-header">
                    <span class="insight-type">${insight.type}</span>
                    <span class="insight-priority ${insight.priority}">${insight.priority}</span>
                </div>
                <div class="insight-message">${insight.message}</div>
                <div class="insight-action">
                    <strong>Human-Centered Action:</strong> ${insight.action}
                </div>
            </div>
        `).join('') || '<div class="no-insights">All drivers reporting optimal focus.</div>';
    }

    renderAlerts() {
        const container = document.getElementById('alertsContainer');
        if (this.alerts.length === 0) {
            container.innerHTML = `
                <div class="alert community">
                    <div class="alert-header"><span class="alert-type">Community</span></div>
                    <div class="alert-message">Sylvia just reached her destination safely! Bravo team.</div>
                </div>
            `;
            return;
        }
        // ... rest of alert rendering
    }

    renderVehicleList(filteredVehicles = null) {
        const container = document.getElementById('vehicleListContainer');
        const vehiclesToShow = filteredVehicles || this.vehicles;

        container.innerHTML = vehiclesToShow.map(vehicle => `
            <div class="vehicle-item" onclick="dashboard.showVehicleDetails('${vehicle.id}')">
                <div class="vehicle-info">
                    <h4>${vehicle.driver_id}'s ${vehicle.model}</h4>
                    <p>Focus Level: High | Range: ${Math.round(vehicle.current_charge * 2.5)} km</p>
                </div>
                <div class="vehicle-status ${vehicle.status}">${vehicle.status}</div>
            </div>
        `).join('');
    }

    populateRouteVehicles() {
        const select = document.getElementById('routeVehicle');
        select.innerHTML = '<option value="">Select Vehicle</option>' +
            this.vehicles.map(vehicle => `<option value="${vehicle.id}">${vehicle.driver_id}'s Fleet</option>`).join('');
    }

    contactBuddy(buddyId) {
        const buddy = this.buddies.find(b => b.id === buddyId);
        alert(`Connecting to ${buddy.name} via Buddy Radio...`);
    }

    simulateFatigueMonitoring() {
        const fatigueEl = document.getElementById('driverFatigue');
        setInterval(() => {
            const focusLevels = ['Optimal', 'High', 'Moderate'];
            const level = focusLevels[Math.floor(Math.random() * focusLevels.length)];
            fatigueEl.textContent = level;
            fatigueEl.className = 'stat-value ' + (level === 'Optimal' ? 'text-success' : 'text-warning');
        }, 8000);
    }

    setupEventListeners() {
        // ... standard listeners
        document.getElementById('optimizeRoute').onclick = () => {
            const results = document.getElementById('routeResults');
            results.innerHTML = `
                <div class="route-info">
                    <h4>Community Optimized Path</h4>
                    <p>Route shared with <strong>John Mathe</strong> for peer-support overlap.</p>
                    <p>ETA reduction: 12 mins via shared traffic data.</p>
                </div>
             `;
            results.classList.add('show');
        };
    }

    startAutoRefresh() {
        setInterval(() => this.loadDashboardData(), 30000);
    }
}

let dashboard;
document.addEventListener('DOMContentLoaded', () => {
    dashboard = new RouteMateDashboard();
});