import pandas as pd


class DatasetParser:

    @staticmethod
    def extract_metadata(file_path):

        dataframe = pd.read_csv(file_path)

        return {
            "row_count": len(dataframe),
            "column_count": len(dataframe.columns)
        }