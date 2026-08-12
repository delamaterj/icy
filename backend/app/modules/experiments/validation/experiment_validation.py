import uuid 
from app.enums.experiment_model import ExperimentModel 

def validate_create_experiment_request(data):
    errors = []
    if not isinstance(data, dict):
        raise ValueError("Request body must be a JSON object.")

    dataset_id = data.get("dataset_id")
    if not dataset_id:
        errors.append("dataset_id is required.")
    else:
        try:
            uuid.UUID(dataset_id)
        except (ValueError, TypeError, AttributeError):
            errors.append("dataset_id must be a valid UUID.")

    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        errors.append("name is required.")
    elif len(name) > 255:
        errors.append("name must not exceed 255 characters.")

    description = data.get("description")
    if description is not None:
        if not isinstance(description, str):
            errors.append("description must be a string.")

    model = data.get("model")
    if not model:
        errors.append("model is required.")
    elif model not in [model.value for model in ExperimentModel]:
        errors.append("model must be one of: " + ", ".join(model.value for model in ExperimentModel))

    target_column = data.get("target_column")
    if not isinstance(target_column, str) or not target_column.strip():
        errors.append("target_column is required.")
    elif len(target_column) > 255:
        errors.append("target_column must not exceed 255 characters.")

    test_size = data.get("test_size", 0.20)
    if not isinstance(test_size, (int, float)) or isinstance(test_size, bool):
        errors.append("test_size must be a number.")
    elif not 0 < test_size < 1:
        errors.append("test_size must be greater than 0 and less than 1.")

    random_seed = data.get("random_seed", 42)
    if not isinstance(random_seed, int) or isinstance(random_seed, bool):
        errors.append("random_seed must be an integer.")

    return {
        "dataset_id": str(uuid.UUID(dataset_id)),
        "name": name.strip(),
        "description": description,
        "model": ExperimentModel(model),
        "target_column": target_column.strip(),
        "test_size": test_size,
        "random_seed": random_seed,
        "errors": errors
    }