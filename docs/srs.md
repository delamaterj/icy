Software Requirements Specification (SRS)



Version: 1.0

Status: Draft

Author: Joshua Delamater

Project Type: Production-Style Machine Learning Web Application



1\. Introduction

1.1 Purpose



The Intelligent Security Event Analysis Platform (ICY) is a web-based application that assists security analysts in detecting, investigating, and managing suspicious network activity through machine learning.



The platform enables users to upload network traffic datasets, process and validate the data, generate predictions using trained machine learning models, explain prediction results, and visualize security events through an interactive dashboard.



The purpose of this project is to demonstrate production-style software engineering, machine learning engineering, and modern deployment practices.



1.2 Intended Audience



This document is intended for:



Software Developers

Machine Learning Engineers

QA/Test Engineers

Future Contributors

Hiring Managers (portfolio documentation)

1.3 Project Objectives



The system shall:



Process cybersecurity datasets

Detect malicious network traffic

Explain prediction results

Store historical predictions

Provide analyst-friendly dashboards

Support future MLOps integration

Support future deep learning models

2\. Overall Description

2.1 Product Perspective



ICY is a standalone web application consisting of:



React frontend

Flask REST API

PostgreSQL database

Machine learning pipeline

Model inference service



The application follows a layered architecture separating presentation, business logic, machine learning, and persistence.



2.2 User Classes

Security Analyst



Primary user.



Responsibilities:



Upload datasets

Review alerts

Investigate predictions

View analytics

Security Administrator



Responsibilities:



Manage ML models

Retrain models

Review system metrics

Configure application settings

Future Roles



Potential future expansion:



SOC Manager

Read-only Auditor

System Administrator



3\. Assumptions and Constraints

Assumptions

Users possess basic cybersecurity knowledge.

Uploaded datasets follow supported formats.

Network connectivity is available.

Models have been previously trained before inference.

Constraints



Version 1 uses:



CSV datasets only

CIC-IDS2017 dataset

Flask backend

PostgreSQL

REST architecture

Single deployed model at a time

4\. Functional Requirements

FR-1 Authentication

Description



Users shall authenticate before accessing protected resources.



Inputs

Email

Password

Outputs

JWT

User information

Acceptance Criteria

Valid credentials return an access token.

Invalid credentials return an error.

Protected routes require authentication.

FR-2 Dataset Upload

Description



Users shall upload network traffic datasets.



Inputs



CSV file



Outputs



Dataset record



Acceptance Criteria

Reject invalid file types.

Reject malformed datasets.

Store successful uploads.

Display upload status.

FR-3 Data Validation



The system shall:



Validate schema

Validate required columns

Detect duplicates

Detect missing values

Generate validation report

FR-4 Feature Engineering



The system shall:



Normalize features

Encode categorical variables

Handle missing values

Produce model-ready features

FR-5 Model Training



The system shall:



Train supported models

Evaluate performance

Save trained models

Store evaluation metrics



Supported models (initially):



Logistic Regression

Random Forest

Isolation Forest



Future:



XGBoost

Autoencoder

LSTM

FR-6 Prediction



Users shall request predictions.



Inputs:



Uploaded dataset



Outputs:



Prediction

Confidence score

Risk level

FR-7 Explainability



The system shall display:



Confidence

Feature importance

Explanation of prediction

FR-8 Alerts



The system shall:



Generate alerts for:



High-risk events

Critical attacks

Anomalous behavior

FR-9 Dashboard



The dashboard shall display:



Active alerts

Prediction history

Model performance

Dataset statistics

Upload history

FR-10 Model Management



Administrators shall:



View available models

Activate models

Retrain models

Archive models

5\. Non-Functional Requirements

Performance



Prediction latency:



< 500 ms



Scalability



Architecture shall support:



Additional ML algorithms

Larger datasets

Multiple deployed models

Availability



The system shall recover from:



Invalid uploads

Failed predictions

Database connection failures

Maintainability



Business logic shall remain independent of:



UI

Database implementation

ML implementation

Security



The application shall:



Validate uploads

Require authentication

Hash passwords

Protect endpoints

Store secrets in environment variables

Reliability



Model predictions shall be reproducible using the same model version and feature pipeline.



6\. System Use Cases

UC-1 Upload Dataset



Actor:



Security Analyst



Flow:



Select CSV

Upload

Validate

Store

Notify success/failure

UC-2 Train Model



Actor:



Security Administrator



Flow:



Select dataset

Choose algorithm

Train

Evaluate

Save model

Store metrics

UC-3 Generate Prediction



Actor:



Security Analyst



Flow:



Select uploaded dataset

Run prediction

Display results

Display explanations

Store prediction

UC-4 Review Alerts



Actor:



Security Analyst



Flow:



Open dashboard

View alerts

Filter alerts

Inspect event

Review explanation

7\. External Interfaces

User Interface



React dashboard



Pages:



Login

Dashboard

Upload Logs

Alerts

Predictions

Models

Analytics

Settings

API Interface



REST API



Endpoints (initial):



POST   /auth/login

POST   /logs/upload



GET    /logs



POST   /models/train



GET    /models



POST   /predict



GET    /alerts



GET    /predictions



GET    /metrics

Database Interface



PostgreSQL



Initial entities:



Users

Uploaded Logs

Security Events

Predictions

Alerts

Models

Evaluation Metrics

8\. Error Handling Requirements



The system shall gracefully handle:



Invalid CSV uploads

Missing required columns

Corrupted files

Model loading failures

Prediction failures

Database outages

Authentication failures



Each error shall return:



Appropriate HTTP status code

Clear error message

Logged server-side details for debugging

9\. Acceptance Criteria



Version 1 is considered complete when:



Users can authenticate.

CSV datasets can be uploaded and validated.

The preprocessing pipeline produces model-ready features.

At least one trained ML model can generate predictions through the REST API.

Predictions include confidence scores and explainability information.

Results are persisted in PostgreSQL.

Analysts can review predictions and alerts through the React dashboard.

The application is deployed and accessible.

Core functionality is covered by automated tests.

10\. Future Enhancements



Future versions may include:



Real-time network traffic ingestion

Streaming inference

Multiple active model versions

MLflow experiment tracking

Automatic model retraining

Autoencoder-based anomaly detection

LSTM sequence analysis

Role-based access control with granular permissions

SIEM integrations

Email or webhook alerting

Kubernetes deployment

Multi-tenant support

