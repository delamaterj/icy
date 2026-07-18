Intelligent Security Event Analysis Platform (ICY)

Architecture \& Design Document v1.0



Author: Joshua Delamater

Status: Draft v1.0

Project Type: Full-Stack Machine Learning Application

Primary Language: Python



1\. Project Overview



Purpose



The Intelligent Security Event Analysis Platform (ICY) is a production-style web application that assists security analysts in identifying potentially malicious network activity using machine learning.



Rather than acting as a simple intrusion classifier, the system provides an end-to-end workflow for ingesting network traffic logs, engineering features, generating risk predictions, explaining model decisions, and visualizing results through an interactive dashboard.



The project is designed to demonstrate software engineering, machine learning, and MLOps principles within a realistic enterprise architecture.



Goals



Demonstrate:



Python software development

Flask backend development

Machine Learning engineering

Data engineering

REST API design

PostgreSQL integration

React frontend development

Explainable AI

Production deployment

Docker

MLOps



Target Users



Primary User:



Security Analyst



Future Users:



Security Administrator

SOC Manager

System Administrator



2\. Scope



The application will allow analysts to:



Upload network traffic logs

Store uploaded datasets

Process raw data

Generate engineered features

Train machine learning models

Compare model performance

Detect suspicious activity

View predictions

Review model explanations

Track historical alerts

Visualize security trends



Out of Scope (Version 1)



The following will not be included initially:



Live packet capture

SIEM integration

Active Directory integration

Real-time network monitoring

Distributed training

Kubernetes deployment

GPU training

User notifications

Multi-tenant architecture



These remain potential future enhancements once the core platform is stable.



3\. Functional Requirements

Authentication



The system shall:



Allow users to log in

Maintain authenticated sessions

Restrict access to authorized users



Dataset Management



The system shall:



Upload CSV datasets

Validate uploaded files

Reject invalid schemas

Track upload history



Data Processing



The system shall:



Clean datasets

Handle missing values

Remove duplicates

Normalize features

Engineer new features

Machine Learning



The system shall:



Train multiple models

Evaluate performance

Save trained models

Load existing models

Generate predictions

Security Events



The system shall:



Store predictions

Assign risk scores

Generate alerts

Track alert history

Explainability



The system shall:



Display confidence scores

Display contributing features

Explain predictions

Dashboard



The system shall:



Display:



Security metrics

Active alerts

Prediction history

Model performance

Dataset statistics

4\. Non-Functional Requirements

Performance



Prediction latency:



< 500 ms



Reliability



Model loading shall occur once at application startup.



Scalability



The architecture shall support future model replacement without API changes.



Maintainability



Each component shall have a single responsibility.



Security



Uploaded files shall be validated before processing.



Availability



The application shall recover gracefully from invalid datasets.



Extensibility



Additional ML models shall be pluggable without rewriting the prediction pipeline.



5\. Technology Stack

Backend

Python

Flask



Frontend

React

TypeScript

Vite

Machine Learning



Version 1



pandas

NumPy

scikit-learn



Version 2



XGBoost

SHAP



Version 3



PyTorch

Database



PostgreSQL



Testing

pytest

Postman (during development)



Deployment

Docker

Render

Vercel



6\. High-Level Architecture

&#x20;                React Frontend

&#x20;                       │

&#x20;                       ▼

&#x20;               Flask REST API

&#x20;                       │

&#x20;       ┌───────────────┼────────────────┐

&#x20;       │               │                │

&#x20;       ▼               ▼                ▼

&#x20;Authentication   Prediction API   Training API

&#x20;       │               │                │

&#x20;       └───────────────┼────────────────┘

&#x20;                       ▼

&#x20;            ML Service Layer

&#x20;                       │

&#x20;       ┌───────────────┼────────────────┐

&#x20;       ▼               ▼                ▼

&#x20;Feature Pipeline  Model Registry  Evaluation

&#x20;                       │

&#x20;                       ▼

&#x20;                PostgreSQL



7\. Proposed Repository Structure



icy/

│

├── backend/

│   ├── api/

│   ├── routes/

│   ├── services/

│   ├── models/

│   ├── schemas/

│   ├── middleware/

│   ├── config/

│   └── app.py

│

├── frontend/

│

├── ml/

│   ├── data/

│   ├── features/

│   ├── training/

│   ├── inference/

│   ├── evaluation/

│   ├── explainability/

│   ├── models/

│   └── utils/

│

├── database/

│

├── datasets/

│

├── docs/

│

├── tests/

│

├── scripts/

│

├── docker/

│

└── README.md



8\. Development Principles



To keep the project maintainable as it grows, the following guiding principles will be considered:



API-first design: The frontend communicates only through documented REST endpoints.

Separation of concerns: Data ingestion, feature engineering, training, inference, and presentation each live in dedicated modules.

Configuration over hardcoding: Environment variables and configuration files control database connections, model paths, and deployment settings.

Reproducibility: Training pipelines should produce the same results when run against the same data and configuration.

