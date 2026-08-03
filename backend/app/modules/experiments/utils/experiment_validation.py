class ExperimentValidation:

    @staticmethod
    def validate_create(data):

        errors = []

        if not data.get("dataset_id"):
            errors.append("Dataset ID is required.")

        if not data.get("name"):
            errors.append("Experiment name is required.")

        return errors