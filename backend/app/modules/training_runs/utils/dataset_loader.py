import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from app.common.exceptions import ValidationException
from app.modules.datasets.utils.dataset_parser import DatasetParser

class DatasetLoader:

    @staticmethod
    def load_and_split(
        file_path: str,
        target_column: str,
        test_size: float,
        random_seed: int
    ):

        dataframe = DatasetParser.load_dataframe(file_path)

        if dataframe.empty:
            raise ValidationException([
                "Dataset is empty."
            ])

        if target_column not in dataframe.columns:
            raise ValidationException([
                f"Target column '{target_column}' was not found."
            ])

        X = dataframe.drop(
            columns=[target_column]
        )

        y = dataframe[target_column]

        if not all(
            pd.api.types.is_numeric_dtype(dtype)
            for dtype in X.dtypes
        ):
            raise ValidationException([
                "Dataset contains non-numeric feature columns."
            ])

        label_encoder = LabelEncoder()
        y = label_encoder.fit_transform(y)
        
        labels = sorted(y.unique())

        label_mapping = {
            label: index
            for index, label in enumerate(labels)
        }

        y = y.map(label_mapping)

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_seed,
            stratify=y
        )

        return {
            "X_train": X_train,
            "X_test": X_test,
            "y_train": y_train,
            "y_test": y_test,
            "label_mapping": label_mapping
        }