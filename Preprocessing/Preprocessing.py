import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Attribute_Selection import chi2_test_on_categorical_features,chi2_test_matrix_evaluation,correlation_of_numerical_features
from Training.train_test import cross_validation_Models_evaluation
list_of_categorical_colums = []
list_of_numerical_colums = []


def load_dataset():
    pd.options.display.max_rows = 1500
    pd.options.display.max_columns = 90
    df = pd.read_csv("D:\House Price Prediction\Datasets/train.csv", na_filter=False)

    # checking null values if any
    print(df.isnull().sum())
    return df


def extracting_categorical_data(df):

    # in this function i first change the data type of some columns
    # encode categorical values to numerical values
    # and then i extract all the categorical columns and save numerical and categorical
    # columns in separate svc file to find there mutual correlation

    dfe = pd.read_csv("D:\House Price Prediction\Datasets/train.csv", na_filter=False)
    dfe.drop('Id', axis=1, inplace=True)
    dfe.drop('MasVnrArea', axis=1, inplace=True)
    dfe['YearBuilt'] = df['YearBuilt'].apply(str)

    # changing data types of below features from int64 to string
    dfe['YearRemodAdd'] = df['YearRemodAdd'].apply(str)
    dfe['OverallQual'] = df['OverallQual'].apply(str)
    dfe['OverallCond'] = df['OverallCond'].apply(str)
    dfe.describe()
    dfe.info()
    for colums in dfe:
        if dfe[colums].dtypes == np.object:
            list_of_categorical_colums.append(colums)
            ordinal_label = {k: i for i, k in enumerate(dfe[colums].unique(), 0)}
            dfe[colums] = dfe[colums].map(ordinal_label)
        else:
            list_of_numerical_colums.append(colums)

    dfe.loc[:, list_of_categorical_colums].to_csv('D:\House Price Prediction\Datasets/categorical_data_encoded.csv')
    dfe.loc[:, list_of_numerical_colums].to_csv('D:\House Price Prediction\Datasets/numerical_data.csv')


df = load_dataset()
extracting_categorical_data(df)
chi2_test_on_categorical_features()
chi2_test_matrix_evaluation()
correlation_of_numerical_features()
cross_validation_Models_evaluation()