from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from app.enums.experiment_model import ExperimentModel
from app.common.exceptions import ValidationException

class ModelFactory:

    @staticmethod
    def create(model_type: ExperimentModel):

        if model_type == ExperimentModel.LOGISTIC_REGRESSION:

            return LogisticRegression(
                max_iter=1000
            )

        if model_type == ExperimentModel.DECISION_TREE:

            return DecisionTreeClassifier()

        if model_type == ExperimentModel.RANDOM_FOREST:

            return RandomForestClassifier()

        raise ValidationException([
            f"Unsupported experiment model: {model_type.value}"
        ])