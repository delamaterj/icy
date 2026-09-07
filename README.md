# Welcome to ICY!

ICY is a machine-learning experimentation platform designed to
manage datasets, configure experiments, execute training runs,
and evaluate machine-learning models.

## Milestone 1 (9/7/2026)

ICY currently provides an end-to-end workflow for managing datasets,
experiments, and training runs.

### Dataset Management

- Upload datasets through the application
- Validate uploaded dataset structure and metadata*
- Detect duplicate datasets using checksums
- Store dataset metadata
- View a summary table of available datasets
- View detailed information for individual datasets
- Support a limited selection of dataset file types

### Experiment Management

- Create experiments from validated datasets
- Associate each experiment with a dataset
- Configure a target column for machine-learning tasks (ex. Label)
- Select from a limited set of supported machine-learning models*
- View a summary table of available experiments
- View detailed information for individual experiments

### Training Run Management

- Create training runs for registered experiments
- Configure the test size for each training run
- Configure the random seed for each training run
- Execute training runs using the experiment's configured model
- Track the status of individual training runs
- Store training run results
- View a summary of available training runs
- View detailed information for individual training runs

## Current Limitations*

ICY currently uses a deliberately limited set of supported
configurations while the machine-learning experimentation pipeline
is being developed.

### Supported Dataset Types

- Limited to supported dataset file types (CSV)
- Requires one or more feature columns and one target column
- All feature columns must be numerical, while the target column must be either labeled "BENIGN" or "DDOS"

### Supported Machine-Learning Models

- Limited to a predefined set of machine-learning models
- Users cannot currently add arbitrary models to the application

### Supported Training Parameters

- `test_size`
- `random_seed`

Additional datasets, models,
training parameters, and model-specific hyperparameters,
will be introduced in future development!

## Current Workflow

The current ICY workflow is:

Dataset
→ Validation
→ Experiment
→ Training Run
→ Model Training
→ Evaluation
→ Training Run Results

## Milestone 1 Summary

At the completion of Milestone 1, users can:

1. Upload and manage datasets
2. View dataset summaries and detailed metadata
3. Create and manage experiments based on validated datasets
4. View experiment summaries and detailed information
5. Create and execute training runs for experiments
6. Configure the test size and random seed for individual training runs
7. View training run summaries and detailed information
8. Store and view the results produced by training runs

The current implementation establishes the foundation for future
machine-learning experimentation, model comparison, and research
workflows.
