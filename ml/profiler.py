import pandas as pd


class DataProfiler:

    def profile(self, df):

        return {

            "rows": df.shape[0],

            "columns": df.shape[1],

            "column_names": list(df.columns),

            "data_types": df.dtypes.astype(str).to_dict(),

            "missing_values": df.isnull().sum().to_dict(),

            "duplicate_rows": int(df.duplicated().sum()),

            "memory_usage_kb": round(
                df.memory_usage(deep=True).sum() / 1024,
                2
            ),

            "unique_values": df.nunique().to_dict()

        }