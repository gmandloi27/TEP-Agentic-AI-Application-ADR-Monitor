


# TEP-Agentic-AI-Application-ADR-Monitor
# 🧪 ADR Monitor – Adverse Drug Reaction Monitoring & Pharmacovigilance Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Backend-green.svg)
![SQLite](https://img.shields.io/badge/Database-SQLite-orange.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-blue.svg)
![AI Agent](https://img.shields.io/badge/AI-Agent-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📌 Overview

ADR Monitor is a comprehensive **Pharmacovigilance and Adverse Drug Reaction (ADR) Monitoring System** developed using **Python, Flask, SQLite/PostgreSQL, and AI-powered Agentic Search**.

The platform enables healthcare researchers, pharmaceutical organizations, regulatory agencies, and pharmacovigilance professionals to monitor, analyze, and assess drug safety by tracking adverse drug reactions, identifying drug interaction risks, generating safety alerts, and producing regulatory reports.

The system includes an intelligent AI assistant capable of understanding natural language queries and automatically selecting the appropriate analytical workflow.

---

# 🎯 Objectives

The primary objectives of ADR Monitor are:

- Monitor adverse drug reactions in real-time
- Detect emerging drug safety signals
- Analyze drug interaction risks
- Generate regulatory compliance reports
- Support pharmacovigilance activities
- Provide AI-assisted safety assessments
- Identify high-risk patient demographics
- Track trends in adverse event reporting

---

# ✨ Key Features

## 💊 Drug Management

- Drug database management
- Search by name
- Search by generic name
- Category-based filtering
- Manufacturer information
- Drug profile management

---

## ⚠️ Adverse Reaction Monitoring

- ADR case recording
- Severity classification
- Patient demographics tracking
- Symptoms monitoring
- Source identification
- Status management

Supported Severity Levels:

- Mild
- Moderate
- Severe
- Fatal

---

## 🔗 Drug Interaction Analysis

The system automatically identifies:

- Mild interactions
- Moderate interactions
- Severe interactions
- Contraindicated combinations

Examples:

| Drug Combination | Risk |
|-----------------|-------|
| Warfarin + Clopidogrel | Severe |
| Warfarin + Amoxicillin | Moderate |
| Omeprazole + Clopidogrel | Severe |
| Lisinopril + Amlodipine | Mild |

---

## 📊 Drug Risk Scoring Engine

The platform computes dynamic risk scores based on:

- Number of adverse reactions
- Severe reaction count
- Fatality count
- Drug interaction frequency

Risk Levels:

| Score | Risk Level |
|---------|------------|
| 0 – 19 | Low |
| 20 – 49 | Medium |
| 50 – 74 | High |
| 75 – 100 | Critical |

---

## 🚨 Safety Alert Management

The system generates and tracks:

- New Safety Signals
- Interaction Alerts
- Threshold Violations
- Demographic Risk Alerts
- Cluster Detection Alerts

Alert Status:

- Active
- Acknowledged
- Resolved

---

## 📄 Regulatory Reporting

Generate:

- Periodic Safety Update Reports (PSUR)
- Aggregate Safety Reports
- Expedited Reports
- FAERS Submissions

Report Status:

- Draft
- Submitted
- Accepted

---

## 📈 Dashboard Analytics

The dashboard provides:

### Summary Metrics

- Total ADR Cases
- Active Alerts
- Pending Reports
- Drugs Monitored
- Severe Cases
- New Signals

### Trend Analysis

- Daily ADR Trends
- Severity Trends
- Drug Safety Trends

### Drug Ranking

Top drugs by:

- ADR frequency
- Severity score
- Fatality count

---

## 👥 Demographic Risk Analysis

Analyze ADRs based on:

### Age Groups

- 0–17
- 18–29
- 30–44
- 45–59
- 60–74
- 75+

### Gender Analysis

- Male
- Female

### Comorbidity Assessment

- Diabetes
- Hypertension
- Heart Failure
- Chronic Kidney Disease
- Cardiovascular Disorders

---

# 🤖 Agentic AI Assistant

One of the major features of ADR Monitor is the integrated AI assistant.

The assistant understands natural language queries and automatically performs:

### Drug Search

Example:

```json
{
  "prompt": "Tell me about Crocine"
}
```

### Risk Assessment

```json
{
  "prompt": "What is the risk score of Warfarin?"
}
```

### Drug Interaction Analysis

```json
{
  "prompt": "Show interactions for Clopidogrel"
}
```

### Safety Alerts

```json
{
  "prompt": "Show active alerts"
}
```

### Regulatory Reports

```json
{
  "prompt": "Latest regulatory reports"
}
```

### Dashboard Summary

```json
{
  "prompt": "Provide dashboard summary"
}
```

---

# 🏗️ System Architecture

```text
+---------------------------------------------------+
|                   Frontend UI                     |
+---------------------------------------------------+
                       |
                       ▼
+---------------------------------------------------+
|                 Flask REST API                    |
+---------------------------------------------------+
       |               |                |
       ▼               ▼                ▼

 Drug Service    ADR Service     Alert Service

       |               |                |
       +---------------+----------------+
                       |
                       ▼

+---------------------------------------------------+
|                Agentic AI Engine                  |
+---------------------------------------------------+
                       |
                       ▼

+---------------------------------------------------+
|            SQLite / PostgreSQL Database           |
+---------------------------------------------------+
```

---

# 🗄️ Database Schema

The platform uses the following tables:

### drugs

Stores:

- Drug information
- Generic names
- Categories
- Manufacturers

### adverse_reactions

Stores:

- Patient demographics
- Symptoms
- Severity
- Source
- Status

### drug_interactions

Stores:

- Drug combinations
- Interaction severity
- Mechanism

### alerts

Stores:

- Safety signals
- Alert severity
- Alert status

### regulatory_reports

Stores:

- Report type
- Report status
- Submission history

---

# 📡 REST API Endpoints

## Health

```http
GET /api/healthz
```

---

## Drugs

```http
GET /api/drugs
POST /api/drugs
GET /api/drugs/{id}
GET /api/drugs/{id}/interactions
GET /api/drugs/{id}/risk-score
```

---

## Adverse Reactions

```http
GET /api/reactions
POST /api/reactions
PATCH /api/reactions/{id}
DELETE /api/reactions/{id}
```

---

## Alerts

```http
GET /api/alerts
POST /api/alerts
PATCH /api/alerts/{id}
DELETE /api/alerts/{id}
```

---

## Reports

```http
GET /api/reports
POST /api/reports
GET /api/reports/{id}
PATCH /api/reports/{id}
```

---

## Dashboard

```http
GET /api/dashboard/summary
GET /api/dashboard/trends
GET /api/dashboard/top-drugs
GET /api/demographics/analysis
```

---

## AI Assistant

```http
POST /api/agent/query
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ADR-Monitor.git

cd ADR-Monitor
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment

Create:

```bash
.env
```

Example:

```env
DATABASE_URL=sqlite:///adr_monitor.db
PORT=5000
```

---

# ▶️ Run Application

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

# 🧪 Sample Agent Queries

### Drug Search

```text
Tell me about Crocine
```

### Risk Assessment

```text
What is the risk score of Warfarin?
```

### Drug Interactions

```text
Show interactions for Clopidogrel
```

### Safety Alerts

```text
Show active safety alerts
```

### Dashboard Summary

```text
Provide dashboard summary
```

---

# 🔒 Security Features

- Environment Variable Support
- SQL Parameterized Queries
- CORS Support
- Secure API Design
- Error Handling
- Input Validation

---

# 📁 Project Structure

```text
ADR-Monitor/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── adr_monitor.db
│
├── docs/
│
├── notebooks/
│
├── tests/
│
├── assets/
│
├── dist/
│
└── .github/
    └── workflows/
```

---

# 🔮 Future Enhancements

- Machine Learning Based Signal Detection
- LLM-Based Pharmacovigilance Agent
- Real-Time FAERS Integration
- Drug Safety Prediction Models
- Neo4j Knowledge Graph Integration
- Risk Forecasting Dashboard
- Mobile Application
- Cloud Deployment

---

# 👨‍💻 Technologies Used

### Backend

- Python
- Flask
- Flask-CORS

### Database

- SQLite
- PostgreSQL

### AI Components

- Rule-Based Agent
- Natural Language Query Processing
- Risk Scoring Engine

### Development Tools

- Git
- GitHub
- Jupyter Notebook

---

# 📜 License

This project is licensed under the MIT License.

---

# 🙏 Acknowledgements

- FDA FAERS Pharmacovigilance Concepts
- Drug Safety Monitoring Guidelines
- Flask Community
- Python Open Source Ecosystem

---

## ⭐ Support

If you find this project useful, please consider giving it a ⭐ on GitHub.

It helps researchers and developers discover the project and supports future development.
