Intelligent Security Event Analysis Platform (ICY)

Software Design Document (SDD)



Version: 1.0

Status: Draft

Author: Joshua Delamater



1\. Purpose



The Software Design Document defines the internal architecture of ICY, including system components, module responsibilities, data flow, database interactions, machine learning pipeline, API interactions, and deployment architecture.



The design follows a modular, layered architecture to maximize maintainability, extensibility, and testability.



2\. Architectural Principles



The system is built around these principles:



Single Responsibility Principle: Each service has one clearly defined purpose.

Separation of Concerns: UI, API, business logic, ML, and persistence are independent layers.

API-First Design: All frontend interactions occur through documented REST endpoints.

Reusability: Shared logic (e.g., preprocessing) is reused across training and inference.

Reproducibility: ML pipelines are deterministic and version-controlled.

Extensibility: New models and features should be added with minimal changes to existing code.

3\. Layered Architecture

+---------------------------------------------------+

|                  React Frontend                   |

+---------------------------------------------------+

&#x20;                       │

&#x20;                       ▼

+---------------------------------------------------+

|                 Flask REST API                    |

+---------------------------------------------------+

&#x20;                       │

&#x20;                       ▼

+---------------------------------------------------+

|                  Service Layer                    |

|  Auth | Upload | Prediction | Training | Alerts   |

+---------------------------------------------------+

&#x20;                       │

&#x20;                       ▼

+---------------------------------------------------+

|                 ML Pipeline Layer                 |

| Validation | Features | Inference | Evaluation    |

+---------------------------------------------------+

&#x20;                       │

&#x20;                       ▼

+---------------------------------------------------+

|              Persistence Layer                    |

| PostgreSQL | Saved Models | Uploaded Files        |

+---------------------------------------------------+

4\. Module Design

4.1 Authentication Service



Responsibilities



Authenticate users

Verify passwords

Generate JWTs

Validate tokens

Authorize protected endpoints



Inputs



Email

Password



Outputs



JWT

User metadata



Dependencies



Users table

JWT utilities

Password hashing

4.2 Upload Service



Responsibilities



Accept CSV uploads

Validate file type

Store upload metadata

Trigger validation pipeline



Inputs



CSV file



Outputs



Upload record

Validation status



Dependencies



Dataset Validator

PostgreSQL

4.3 Dataset Validation Service



Responsibilities



Validate schema

Check required columns

Detect duplicates

Identify missing values

Generate validation report



Outputs



Validation report

Clean dataset (or validation errors)

4.4 Feature Engineering Service



Responsibilities



Handle missing values

Encode categorical variables

Scale numerical features

Generate model-ready features



Critical Design Decision



The same feature engineering pipeline must be used during:



Training

Inference



This avoids training/serving skew.



4.5 Training Service



Responsibilities



Train baseline models

Evaluate performance

Compare models

Save trained artifacts

Register model metadata



Supported Models (Initial)



Logistic Regression

Random Forest

Isolation Forest



Future



XGBoost

Autoencoder

LSTM

4.6 Prediction Service



Responsibilities



Load active model

Validate input features

Execute inference

Calculate confidence score

Generate risk level

Persist prediction

4.7 Explainability Service



Responsibilities



Calculate feature importance

Generate prediction explanations

Prepare analyst-friendly output



Initial implementation may use built-in feature importances where applicable. Later iterations can incorporate SHAP for model-agnostic explanations.



4.8 Alert Service



Responsibilities



Generate alerts

Assign severity

Track alert lifecycle

Store alert history

5\. Data Flow

Training Workflow

CSV Dataset

&#x20;     │

&#x20;     ▼

Upload Service

&#x20;     │

&#x20;     ▼

Validation

&#x20;     │

&#x20;     ▼

Feature Engineering

&#x20;     │

&#x20;     ▼

Train Models

&#x20;     │

&#x20;     ▼

Evaluate Models

&#x20;     │

&#x20;     ▼

Persist Best Model

&#x20;     │

&#x20;     ▼

Register Model Metadata

Prediction Workflow

Uploaded Dataset

&#x20;      │

&#x20;      ▼

Validation

&#x20;      │

&#x20;      ▼

Feature Engineering

&#x20;      │

&#x20;      ▼

Load Active Model

&#x20;      │

&#x20;      ▼

Inference

&#x20;      │

&#x20;      ▼

Risk Assessment

&#x20;      │

&#x20;      ▼

Explainability

&#x20;      │

&#x20;      ▼

Persist Prediction

&#x20;      │

&#x20;      ▼

Return API Response

6\. Database Design

Initial Entity Relationship

Users

&#x20;  │

&#x20;  ├────────────┐

&#x20;  ▼            ▼

Uploads      Models

&#x20;  │            │

&#x20;  ▼            ▼

Predictions  Training Runs

&#x20;  │

&#x20;  ▼

Alerts

Initial Tables

users



Stores authenticated users.



uploads



Tracks uploaded datasets and validation status.



models



Stores model metadata (name, algorithm, version, status).



training\_runs



Records training execution details and evaluation metrics.



predictions



Stores inference results, confidence scores, and timestamps.



alerts



Stores generated security alerts and lifecycle status.



We'll flesh out column definitions in the implementation phase, but the relationships are now defined.



7\. API Design Principles

Resource-oriented REST endpoints.

JSON request/response bodies.

Consistent error format.

Appropriate HTTP status codes.

Authentication via JWT.



Example error response:



{

&#x20; "error": {

&#x20;   "code": "INVALID\_DATASET",

&#x20;   "message": "Required column 'Flow Duration' is missing."

&#x20; }

}

8\. Logging Strategy



Log levels:



INFO: Startup, uploads, training completion.

WARNING: Validation issues, recoverable errors.

ERROR: Prediction failures, database exceptions.

CRITICAL: Application startup failure, unavailable dependencies.



Logs should include timestamps and request correlation IDs where practical.



9\. Testing Strategy

Unit Tests

Feature engineering

Validation

Prediction service

Training service

Integration Tests

API endpoints

Database interactions

Model loading

End-to-End Tests

Upload → Predict → Alert workflow

ML Validation

Reproducible training

Metric verification

Baseline comparison

10\. Deployment Architecture

&#x20;                User

&#x20;                 │

&#x20;                 ▼

&#x20;         React (Vercel)

&#x20;                 │

&#x20;                 ▼

&#x20;         Flask API (Render)

&#x20;                 │

&#x20;     ┌───────────┴───────────┐

&#x20;     ▼                       ▼

&#x20;PostgreSQL              Saved Models



Future enhancements:



Docker Compose

GitHub Actions

MLflow

Monitoring

