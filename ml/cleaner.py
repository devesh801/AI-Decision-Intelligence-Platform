import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


class DataCleaner:

    def clean(self, df):

        df = df.copy()

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Handle missing values
        for column in df.columns:

            if df[column].dtype == "object":

                imputer = SimpleImputer(strategy="most_frequent")
                df[column] = imputer.fit_transform(df[[column]]).ravel()

                encoder = LabelEncoder()
                df[column] = encoder.fit_transform(df[column])

            else:

                imputer = SimpleImputer(strategy="median")
                df[column] = imputer.fit_transform(df[[column]]).ravel()

        return df