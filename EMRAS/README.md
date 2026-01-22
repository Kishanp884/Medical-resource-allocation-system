# Emergency Medical Resource Allocation System (EMRAS)

## Overview
Advanced Python-based simulation system for intelligent allocation of emergency medical resources. Combines traditional ambulance/hospital allocation with cutting-edge IV drip monitoring and organ safety tracking for comprehensive emergency response management.

## 🎯 Key Features

### 🧠 Smart Resource Allocation Engine
- **Priority-based allocation**: Critical → Serious → Moderate → Minor
- **Multi-factor optimization**: Severity, distance, capacity, ICU availability
- **Advanced matching**: IV-capable ambulances for IV patients, organ-equipped hospitals for transplant cases
- **Conflict prevention**: Prevents resource over-allocation

### 💧 IV Drip Monitoring System (Novel Feature)
- **Digital flow tracking**: Real-time IV flow rate monitoring
- **Automated alerts**:
  - Low remaining time (<30 minutes)
  - Abnormal flow rates (<20 or >100 ml/hr)
- **Status simulation**: Tracks active/finished IV drips
- **Nurse efficiency**: Reduces manual monitoring dependency

### 🫀 Organ Safety Tracking (Unique Feature)
- **Temperature monitoring**: Maintains 2-6°C range
- **Transport time tracking**: Monitors against preservation limits
- **Viability assessment**: Alerts when organs become unusable
- **Transplant management**: Ensures organ quality for procedures

### 🚨 Intelligent Alert System
- **Real-time notifications**: Dashboard alerts for all critical issues
- **Categorized alerts**: IV issues, organ risks, resource shortages
- **Simulation updates**: Time-based status changes

### 📊 Analytics Dashboard
- **Resource utilization graphs**: Ambulance/hospital capacity tracking
- **Patient inflow trends**: Emergency admission patterns
- **ICU usage reports**: Critical care bed management
- **Response time metrics**: Allocation efficiency tracking

### 🔐 Secure Access Control
- **Role-based permissions**: Doctor, Nurse, Admin levels
- **Patient data protection**: Secure handling of medical information
- **Audit logging**: Track all system interactions

## 🏗️ Architecture

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

## 🚀 Installation & Usage

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

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

## 📋 System Scope

### ✅ In Scope
- Resource allocation simulation
- IV drip monitoring alerts
- Organ safety tracking
- Web-based dashboard
- Real-time alerts
- Basic analytics

### ❌ Out of Scope
- Real hardware integration
- AI-based diagnostics
- Insurance processing
- Mobile applications
- Production deployment

## 📈 Success Metrics
- **100% IV monitoring alerts** for critical thresholds
- **Accurate organ tracking** with viability predictions
- **Reduced allocation time** through smart algorithms
- **Improved staff efficiency** via automated monitoring
- **Smooth system performance** under load

## 🔮 Future Enhancements
- **AI priority prediction** using machine learning
- **Mobile app integration** for field access
- **IoT sensor connectivity** for real-time monitoring
- **Cloud analytics** with advanced reporting
- **Voice alerts** for hands-free notifications

## 🤝 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Team
- **Project Lead**: [Your Name]
- **Developers**: [Team Members]
- **Designers**: [UI/UX Team]

## 📞 Support
For questions or issues, please open an issue on GitHub or contact the development team.
