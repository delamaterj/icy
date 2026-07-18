ADR-001: Flask as Backend Framework



Status: Accepted



Context



The backend must expose REST APIs, integrate with ML models, and remain lightweight.



Decision



Use Flask.



Rationale

Lightweight and flexible

Excellent ecosystem for ML integration

Lower overhead than Django

Lets us focus on API and ML architecture

Consequences

We implement authentication and structure ourselves.

Easier to integrate with future MLOps tooling.

ADR-002: PostgreSQL as Database



Status: Accepted



Context



The application requires relational storage for users, uploads, predictions, alerts, and model metadata.



Decision



Use PostgreSQL.



Rationale

ACID compliance

Strong SQL support

Familiar from your previous project

Widely used in production

Consequences

Easier transition from your existing backend experience.

Simplifies relational queries and reporting.

ADR-003: CIC-IDS2017 Dataset



Status: Accepted



Context



We need a public intrusion detection dataset suitable for traditional ML and future deep learning.



Decision



Use CIC-IDS2017.



Rationale

Publicly available

Well documented

Labeled traffic

Common research benchmark

Supports multiple ML approaches

Consequences

Results are reproducible.

Recruiters can evaluate the project using a known dataset.

ADR-004: Classical ML Before Deep Learning



Status: Accepted



Context



The project aims to demonstrate engineering practices while leaving room for advanced ML.



Decision



Begin with traditional models before introducing deep learning.



Rationale

Establishes measurable baselines.

Faster iteration during development.

Easier debugging and explainability.

Reflects common industry practice.

Consequences

Deep learning becomes an enhancement rather than a dependency.

Model comparisons become meaningful.

ADR-005: Shared Feature Pipeline



Status: Accepted



Context



Differences between training and inference preprocessing can lead to inconsistent predictions.



Decision



Use the same preprocessing pipeline for both training and inference.



Rationale

Prevents training/serving skew.

Improves reproducibility.

Simplifies maintenance.

Consequences

Any preprocessing change affects both workflows simultaneously.

Easier to version and test.

