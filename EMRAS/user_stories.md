# EMRAS User Stories

## Epic 1: Smart Resource Allocation

### US-001: Basic Patient Allocation
As a hospital administrator, I want the system to allocate ambulances and hospitals to patients based on severity so that critical patients get priority resources.

**Acceptance Criteria:**
- Patients sorted by severity (Critical > Serious > Moderate > Minor)
- Nearest available ambulance assigned
- Suitable hospital with capacity assigned

### US-002: Distance Optimization
As an emergency dispatcher, I want ambulances assigned based on proximity to minimize response time.

**Acceptance Criteria:**
- Distance calculation between patient and ambulance locations
- Closest available ambulance selected
- Distance displayed in allocation results

### US-003: Capacity Management
As a hospital manager, I want to track hospital bed capacity to prevent over-allocation.

**Acceptance Criteria:**
- Hospital capacity decremented when patient assigned
- ICU availability checked for critical patients
- Capacity reset functionality for simulation

### US-004: IV-Capable Ambulance Matching
As a paramedic, I want IV-requiring patients assigned to ambulances with IV supplies.

**Acceptance Criteria:**
- Ambulance IV capability tracked
- IV-required patients prioritized for IV-equipped ambulances
- Alert when no IV-capable ambulance available

### US-005: Organ Transplant Matching
As a transplant coordinator, I want patients needing organs assigned to hospitals with matching organs.

**Acceptance Criteria:**
- Hospital organ inventory tracked
- Patient organ needs matched to hospital capabilities
- Priority given to hospitals with required organs

## Epic 2: IV Drip Monitoring

### US-006: IV Status Tracking
As a nurse, I want to monitor IV drip status for all patients.

**Acceptance Criteria:**
- IV required flag on patient records
- Flow rate and remaining time tracked
- Status displayed (active/finished)

### US-007: Low IV Fluid Alerts
As a healthcare worker, I want alerts when IV bags are running low.

**Acceptance Criteria:**
- Alert triggered when remaining time < 30 minutes
- Alert displayed on dashboard
- Patient ID and urgency level included

### US-008: Abnormal Flow Rate Detection
As a medical technician, I want alerts for abnormal IV flow rates.

**Acceptance Criteria:**
- Flow rate monitored against normal range (20-100 ml/hr)
- Alert for rates outside acceptable limits
- Flow rate value included in alert

### US-009: IV Status Updates
As a system administrator, I want IV status to update automatically over time.

**Acceptance Criteria:**
- Time-based simulation decreases remaining IV time
- Status changes from active to finished
- Update button in UI

### US-010: IV Supply Inventory
As an ambulance coordinator, I want to track IV supplies in ambulances.

**Acceptance Criteria:**
- IV supplies flag on ambulance records
- Supplies checked during allocation
- Inventory status displayed

## Epic 3: Organ Safety Tracking

### US-011: Organ Temperature Monitoring
As an organ transport technician, I want to monitor organ temperatures.

**Acceptance Criteria:**
- Temperature tracked for each organ
- Acceptable range: 2-6°C
- Temperature displayed in organ status

### US-012: Transport Time Tracking
As a logistics coordinator, I want to track organ transport duration.

**Acceptance Criteria:**
- Transport time incremented over simulation time
- Time displayed in minutes
- Comparison with preservation limits

### US-013: Organ Viability Alerts
As a transplant surgeon, I want alerts when organs become non-viable.

**Acceptance Criteria:**
- Viability determined by temperature and transport time
- Alert when organ exceeds preservation duration
- Viability status clearly indicated

### US-014: Preservation Duration Limits
As a medical director, I want organs tracked against their preservation limits.

**Acceptance Criteria:**
- Different limits for different organ types
- Time remaining calculated
- Alerts when limits approached

### US-015: Organ Inventory Management
As a hospital administrator, I want to track available organs in hospitals.

**Acceptance Criteria:**
- Organ types stored per hospital
- Inventory updated during allocation
- Organ list displayed in hospital status

## Epic 4: Intelligent Alert System

### US-016: Centralized Alert Dashboard
As a healthcare administrator, I want all alerts displayed in one location.

**Acceptance Criteria:**
- Single alerts view in web interface
- Categorized by type (IV, Organ, Resource)
- Real-time updates

### US-017: Alert Prioritization
As an emergency response coordinator, I want alerts prioritized by urgency.

**Acceptance Criteria:**
- Critical alerts highlighted
- Color coding for different severity levels
- Sorting by priority

### US-018: Resource Shortage Alerts
As a resource manager, I want alerts when resources are running low.

**Acceptance Criteria:**
- Alert when ambulance availability < 50%
- Alert when hospital capacity < 20%
- Thresholds configurable

### US-019: Alert History
As a quality assurance officer, I want to view historical alerts.

**Acceptance Criteria:**
- Alert log maintained
- Timestamp for each alert
- Export functionality

### US-020: Alert Acknowledgment
As a staff member, I want to acknowledge alerts I've seen.

**Acceptance Criteria:**
- Acknowledge button for each alert
- Acknowledged alerts marked
- Unacknowledged alerts remain visible

## Epic 5: Analytics Dashboard

### US-021: Resource Utilization Graphs
As a hospital executive, I want to see resource utilization trends.

**Acceptance Criteria:**
- Charts showing ambulance usage over time
- Hospital capacity utilization graphs
- Time-based data visualization

### US-022: Patient Inflow Analytics
As a planning officer, I want to analyze patient admission patterns.

**Acceptance Criteria:**
- Patient arrival trends by time
- Severity distribution charts
- Peak hour identification

### US-023: Response Time Metrics
As a performance manager, I want to track allocation response times.

**Acceptance Criteria:**
- Average allocation time calculated
- Response time by severity level
- Performance benchmarks

### US-024: ICU Usage Reports
As an ICU director, I want detailed ICU utilization reports.

**Acceptance Criteria:**
- ICU bed occupancy rates
- Critical patient admission trends
- Length of stay analytics

### US-025: Export Analytics Data
As a data analyst, I want to export analytics data for further analysis.

**Acceptance Criteria:**
- CSV/JSON export of all metrics
- Date range selection
- Automated report generation