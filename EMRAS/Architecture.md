# EMRAS Architecture Diagram

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    EMRAS System Architecture                    │
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │   Frontend      │    │   Backend       │    │  Database   │  │
│  │   (Web UI)      │◄──►│   (Flask API)   │◄──►│  (In-Memory)│  │
│  │                 │    │                 │    │             │  │
│  │ • HTML/CSS/JS   │    │ • REST API      │    │ • Patients  │  │
│  │ • Dashboard     │    │ • Business Logic│    │ • Ambulances│  │
│  │ • Real-time     │    │ • Simulation    │    │ • Hospitals │  │
│  │ • Responsive    │    │ • Monitoring    │    │ • Organs    │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
│           │                       │                    │        │
└───────────┼───────────────────────┼────────────────────┼────────┘
            │                       │                    │
            ▼                       ▼                    ▼
    User Interaction         API Endpoints         Data Models
```

## Component Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      Component Architecture                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │  Presentation   │    │  Application    │    │   Domain    │  │
│  │    Layer        │    │    Layer        │    │   Layer     │  │
│  │                 │    │                 │    │             │  │
│  │ • Web Interface │    │ • API Routes    │    │ • Business  │  │
│  │ • UI Components │    │ • Controllers   │    │ • Logic     │  │
│  │ • User Actions  │    │ • Request/Resp  │    │ • Entities  │  │
│  │ • Data Display  │    │ • Validation    │    │ • Rules     │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │ Infrastructure  │    │   External      │    │   Data      │  │
│  │    Layer        │    │   Services      │    │   Access    │  │
│  │                 │    │                 │    │             │  │
│  │ • File System   │    │ • Web Server    │    │ • Repositories│  │
│  │ • Configuration │    │ • HTTP Protocol │    │ • Data Models│  │
│  │ • Logging       │    │ • CORS          │    │ • Validation │  │
│  │ • Error Handling│    │ • Security      │    │ • Persistence│  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Detailed Component Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                    Detailed Component Diagram                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐                                            │
│  │   Web Browser   │                                            │
│  │                 │                                            │
│  │ • HTML/CSS/JS   │                                            │
│  │ • Dashboard UI  │                                            │
│  │ • AJAX Calls    │                                            │
│  └─────────────────┘                                            │
│          │                                                      │
│          │ HTTP Requests                                        │
│          ▼                                                      │
│  ┌─────────────────┐                                            │
│  │   Flask Server  │                                            │
│  │                 │                                            │
│  │ • WSGI App      │                                            │
│  │ • Routes        │                                            │
│  │ • Middleware    │                                            │
│  └─────────────────┘                                            │
│          │                                                      │
│          │ Business Logic                                       │
│          ▼                                                      │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │  Allocation     │    │   Monitoring    │    │   Distance   │  │
│  │   Engine        │    │   System        │    │  Calculator  │  │
│  │                 │    │                 │    │             │  │
│  │ • Priority Sort │    │ • IV Alerts     │    │ • Euclidean  │  │
│  │ • Resource Match│    │ • Organ Alerts  │    │ • Distance   │  │
│  │ • Capacity Check│    │ • Status Update │    │ • Location   │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
│          │                       │                    │        │
│          ▼                       ▼                    ▼        │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │   Data Models   │    │   Data Models   │    │   Data      │  │
│  │   (Patients)    │    │   (Resources)  │    │   Models     │  │
│  │                 │    │                 │    │  (Organs)   │  │
│  │ • Demographics  │    │ • Availability  │    │ • Viability │  │
│  │ • Medical Info  │    │ • Capacity      │    │ • Transport  │  │
│  │ • Requirements  │    │ • Equipment     │    │ • Type       │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      Data Flow Architecture                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  User Action → UI Event → AJAX Request → Flask Route            │
│                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐           │
│  │   Trigger   │───►│  Validate  │───►│   Process   │           │
│  │             │    │            │    │             │           │
│  │ • Button    │    │ • Input     │    │ • Business  │           │
│  │ • Form      │    │ • Security  │    │ • Logic     │           │
│  │ • Timer     │    │ • Sanitize  │    │ • Rules     │           │
│  └─────────────┘    └─────────────┘    └─────────────┘           │
│                                                                 │
│  Process → Access Data → Apply Logic → Generate Response        │
│                                                                 │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐           │
│  │   Retrieve  │───►│   Compute  │───►│   Format    │           │
│  │             │    │            │    │             │           │
│  │ • Database  │    │ • Algorithm │    │ • JSON      │           │
│  │ • Files     │    │ • Calculate │    │ • HTML      │           │
│  │ • Cache     │    │ • Transform │    │ • Status     │           │
│  └─────────────┘    └─────────────┘    └─────────────┘           │
│                                                                 │
│  Response → HTTP → Browser → Update UI → Display Results        │
└─────────────────────────────────────────────────────────────────┘
```

## Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Deployment Architecture                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                    Development Environment                  │ │
│  │                                                             │ │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐       │ │
│  │  │   VS Code   │    │   Python    │    │   Browser   │       │ │
│  │  │   Editor    │    │   Runtime   │    │   (Chrome)  │       │ │
│  │  │             │    │             │    │             │       │ │
│  │  │ • Code      │    │ • Flask     │    │ • Dashboard │       │ │
│  │  │ • Debug     │    │ • Virtual   │    │ • Testing   │       │ │
│  │  │ • Git       │    │ • Env       │    │ • UI        │       │ │
│  │  └─────────────┘    └─────────────┘    └─────────────┘       │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                   Production Environment                     │ │
│  │                                                             │ │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐       │ │
│  │  │   Docker    │    │   Gunicorn  │    │   Nginx     │       │ │
│  │  │  Container  │    │   WSGI      │    │   Reverse   │       │ │
│  │  │             │    │   Server    │    │   Proxy     │       │ │
│  │  │ • Python    │    │ • Flask App │    │ • Static    │       │ │
│  │  │ • App       │    │ • Multiple  │    │ • Files     │       │ │
│  │  │ • Config    │    │ • Workers   │    │ • SSL       │       │ │
│  └─────────────┘    └─────────────┘    └─────────────┘       │ │
│                                                                 │ │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                    Cloud Infrastructure                      │ │
│  │                                                             │ │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐       │ │
│  │  │   AWS/GCP   │    │   Database  │    │   CDN       │       │ │
│  │  │   Compute   │    │   Service   │    │   (CloudFlare│       │ │
│  │  │             │    │             │    │   )         │       │ │
│  │  │ • EC2       │    │ • RDS       │    │ • Assets    │       │ │
│  │  │ • Load      │    │ • MongoDB   │    │ • Caching   │       │ │
│  │  │ • Balancer  │    │ • Redis     │    │ • Global    │       │ │
│  └─────────────┘    └─────────────┘    └─────────────┘       │ │
└─────────────────────────────────────────────────────────────────┘
```

## API Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                       API Architecture                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  RESTful Endpoints:                                             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │ Method │ Endpoint          │ Description                    │ │
│  ├─────────────────────────────────────────────────────────────┤ │
│  │ POST   │ /api/allocate     │ Run allocation algorithm       │ │
│  │ GET    │ /api/status       │ Get all system data            │ │
│  │ GET    │ /api/alerts       │ Get current alerts             │ │
│  │ POST   │ /api/update_sim   │ Advance simulation time        │ │
│  │ GET    │ /                  │ Serve web dashboard           │ │
│  └─────────────────────────────────────────────────────────────┘ │
│                                                                 │
│  Response Formats:                                              │
│  • JSON for API endpoints                                       │
│  • HTML for web interface                                       │
│  • Error codes: 200, 400, 404, 500                              │
│                                                                 │
│  Authentication: None (Development)                             │
│  CORS: Enabled for web interface                                │
└─────────────────────────────────────────────────────────────────┘
```

## Security Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Security Architecture                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │   Input         │    │   Data          │    │   Output    │  │
│  │   Validation    │    │   Sanitization  │    │   Encoding  │  │
│  │                 │    │                 │    │             │  │
│  │ • Type checking │    │ • HTML escape   │    │ • JSON      │  │
│  │ • Range limits  │    │ • SQL injection │    │ • XSS       │  │
│  │ • Format        │    │ • Script tags   │    │ • Injection  │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐  │
│  │   Access        │    │   Session       │    │   Audit     │  │
│  │   Control       │    │   Management   │    │   Logging   │  │
│  │                 │    │                 │    │             │  │
│  │ • Role-based    │    │ • CSRF tokens  │    │ • API calls  │  │
│  │ • Permissions   │    │ • Timeouts     │    │ • User actions│  │
│  │ • IP filtering  │    │ • Secure flags  │    │ • Errors     │  │
│  └─────────────────┘    └─────────────────┘    └─────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

## Performance Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Performance Architecture                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Response Times:                                                │
│  • API calls: <500ms                                            │
│  • Page loads: <2s                                              │
│  • Allocation: <1s                                              │
│                                                                 │
│  Scalability Considerations:                                    │
│  • In-memory data: Fast access                                  │
│  • Algorithm optimization: O(n log n)                           │
│  • Concurrent users: Single-user simulation                     │
│                                                                 │
│  Monitoring Points:                                             │
│  • Memory usage: <100MB                                         │
│  • CPU usage: <20%                                              │
│  • Database queries: N/A (in-memory)                            │
│                                                                 │
│  Caching Strategy:                                              │
│  • Static assets: Browser cache                                 │
│  • API responses: No cache (real-time)                          │
│  • Computed data: Recalculate on demand                         │
└─────────────────────────────────────────────────────────────────┘
```

## Technology Stack Labels

```
Frontend Layer:
├── HTML5
├── CSS3
├── JavaScript (ES6+)
└── Browser APIs (Fetch, LocalStorage)

Backend Layer:
├── Python 3.8+
├── Flask 2.0+
├── Werkzeug
└── Jinja2

Data Layer:
├── In-memory storage
├── JSON serialization
├── File-based persistence
└── Extensible to MongoDB/MySQL

Development Tools:
├── VS Code
├── Git
├── Draw.io
├── Figma
└── Docker

Testing Tools:
├── pytest
├── unittest
├── Postman
└── Browser DevTools

Deployment Tools:
├── Docker
├── docker-compose
├── Gunicorn
└── Nginx
```