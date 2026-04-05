# Emergency Medical Resource Allocation System (EMRAS)

## Overview
Advanced Python-based simulation system for intelligent allocation of emergency medical resources. Combines traditional ambulance/hospital allocation with cutting-edge IV drip monitoring and organ safety tracking for comprehensive emergency response management.

##  Key Features

###  Smart Resource Allocation Engine
- **Priority-based allocation**: Critical → Serious → Moderate → Minor
- **Multi-factor optimization**: Severity, distance, capacity, ICU availability
- **Advanced matching**: IV-capable ambulances for IV patients, organ-equipped hospitals for transplant cases
- **Conflict prevention**: Prevents resource over-allocation

###  IV Drip Monitoring System (Novel Feature)
- **Digital flow tracking**: Real-time IV flow rate monitoring
- **Automated alerts**:
  - Low remaining time (<30 minutes)
  - Abnormal flow rates (<20 or >100 ml/hr)
- **Status simulation**: Tracks active/finished IV drips
- **Nurse efficiency**: Reduces manual monitoring dependency

###  Organ Safety Tracking (Unique Feature)
- **Temperature monitoring**: Maintains 2-6°C range
- **Transport time tracking**: Monitors against preservation limits
- **Viability assessment**: Alerts when organs become unusable
- **Transplant management**: Ensures organ quality for procedures

###  Intelligent Alert System
- **Real-time notifications**: Dashboard alerts for all critical issues
- **Categorized alerts**: IV issues, organ risks, resource shortages
- **Simulation updates**: Time-based status changes

###  Analytics Dashboard
- **Resource utilization graphs**: Ambulance/hospital capacity tracking
- **Patient inflow trends**: Emergency admission patterns
- **ICU usage reports**: Critical care bed management
- **Response time metrics**: Allocation efficiency tracking

###  Secure Access Control
- **Role-based permissions**: Doctor, Nurse, Admin levels
- **Patient data protection**: Secure handling of medical information
- **Audit logging**: Track all system interactions

##  Architecture

### Components
- **Frontend**: HTML/CSS/JavaScript web dashboard
- **Backend**: Python Flask REST API
- **Data Layer**: In-memory simulation (extensible to MongoDB/MySQL)
- **Logic Layer**: Allocation algorithms, monitoring systems
- **Simulation Engine**: Time-based status updates

### Tech Stack
| Layer | Technology |
|-------|------------|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python Flask |
| Database | In-memory (MongoDB/MySQL for production) |
| DevOps | Docker |
| Design | Figma |
| Diagrams | Draw.io |
| Version Control | GitHub |

##  Installation & Usage

### Prerequisites
- Python 3.8+
- Virtual environment 

### Setup
```bash
# Clone repository
git clone <repository-url>
cd EMRAS

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r EMRAS/requirements.txt
```

### Running the Application
```bash
# Web Dashboard (Recommended)
python -m EMRAS.web.app
# Access at http://localhost:5000

# CLI Simulation
python EMRAS/main.py
```

##  System Scope

###  In Scope
- Resource allocation simulation
- IV drip monitoring alerts
- Organ safety tracking
- Web-based dashboard
- Real-time alerts
- Basic analytics

###  Out of Scope
- Real hardware integration
- AI-based diagnostics
- Insurance processing
- Mobile applications
- Production deployment

##  Success Metrics
- **100% IV monitoring alerts** for critical thresholds
- **Accurate organ tracking** with viability predictions
- **Reduced allocation time** through smart algorithms
- **Improved staff efficiency** via automated monitoring
- **Smooth system performance** under load

##  Future Enhancements
- **AI priority prediction** using machine learning
- **Mobile app integration** for field access
- **IoT sensor connectivity** for real-time monitoring
- **Cloud analytics** with advanced reporting
- **Voice alerts** for hands-free notifications

FIGMA SCREENS

<img width="1342" height="803" alt="Screenshot 2026-04-04 144419" src="https://github.com/user-attachments/assets/8f9fc8a1-68e6-410a-98f4-791506b76dbe" />


<img width="1166" height="853" alt="Screenshot 2026-04-04 142908" src="https://github.com/user-attachments/assets/a4df69dc-d625-4ed3-8a27-2cd9a8aa93c5" />

<img width="1153" height="855" alt="Screenshot 2026-04-04 142916" src="https://github.com/user-attachments/assets/e25e178e-6dbe-41d1-89aa-b6fb00c41a1d" />

<img width="1161" height="857" alt="Screenshot 2026-04-04 142926" src="https://github.com/user-attachments/assets/4d962750-2f11-47ab-9f4e-d49f57acf56c" />

<img width="1139" height="866" alt="Screenshot 2026-04-04 142934" src="https://github.com/user-attachments/assets/8259a01f-cf74-42cd-8dbd-72b3a3a19f6d" />

<img width="1146" height="823" alt="Screenshot 2026-04-04 142949" src="https://github.com/user-attachments/assets/542ec239-0dd8-4692-b457-1b3251c6a365" />



