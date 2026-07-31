import pandas as pd
from pandas.errors import EmptyDataError, ParserError
from app.common.exceptions import ValidationException


class DatasetParser:

    @staticmethod
    def extract_metadata(file_path):
        try:
            dataframe = pd.read_csv(file_path)
            return {
                "row_count": len(dataframe),
                "column_count": len(dataframe.columns),
                "columns": [
                    column.strip()
                    for column in dataframe.columns
                ]
            }
        except EmptyDataError:
            return {
                "row_count": 0,
                "column_count": 0,
                "columns": []
            }
        except ParserError:
            raise ValidationException([
                "Dataset could not be parsed."
            ])
        except UnicodeDecodeError:
            raise ValidationException([
                "Dataset encoding is not supported."
    ]       )