import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import chi2 , SelectKBest
from scipy import stats
from sklearn.feature_selection import  f_regression
from sklearn import  linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
pd.options.display.max_rows = 1500
pd.options.display.max_columns = 90

# the List selected_categorical_features contains the best categorical features that
# are selected on the bases of chi2 test results
selected_categorical_features = []
eleminated_features = []
final_features = []

# after different correlation tests below are the numerical features that are selected
selected_numerical_features = ['TotalBsmtSF','1stFlrSF','GrLivArea','FullBath','TotRmsAbvGrd','Fireplaces','GarageCars','GarageArea','SalePrice']


def chi2_test_on_categorical_features():
    # this function performs chi2 test on categorical features to find
    # their mutual correlation
    # loading categorical data
    dfc = pd.read_csv('D:\House Price Prediction\Datasets/categorical_data_encoded.csv', na_filter=False)
    column_names = dfc.columns
    # Assigning column names to row index
    chisqmatrix = pd.DataFrame(dfc, columns=column_names, index=column_names)

    for icol in column_names:  # Outer loop
        for jcol in column_names:  # inner loop
            # converting to cross tab as for chi2 test we have to first covert variables into contigency table
            mycrosstab = pd.crosstab(dfc[icol], dfc[jcol])
            # Getting p-value and other usefull information
            stat, p, dof, expected = stats.chi2_contingency(mycrosstab)

            # Rounding very small p-values to zero
            chisqmatrix.loc[icol, jcol] = round(p,5)

            # Expected frequencies should be at
            # least 5 for the majority (80%) of the cells.
            # Here we are checking expected frequency of each group
            cntexpected = expected[expected < 5].size

            # Getting percentage
            perexpected = ((expected.size - cntexpected) / expected.size) * 100
            if perexpected < 20:
                chisqmatrix.loc[icol, jcol] = 2  # Assigning 2

            if icol == jcol:
                chisqmatrix.loc[icol, jcol] = 0.00

    # Saving chi2 results
    chisqmatrix.to_csv('D:\House Price Prediction\Datasets/chi2_result_for_categorical_encoded_data.csv')


def chi2_test_matrix_evaluation():
    # this function traverses the chi2 result matrix to filter best features
    df = pd.read_csv('D:\House Price Prediction\Datasets/chi2_result_for_categorical_encoded_data.csv', na_filter=False, index_col=[0])
    column_names = df.columns
    for icol in column_names:  # Outer loop
        if icol in eleminated_features:
            continue
        else:
            for jcol in column_names:  # inner loop
                check = df.loc[icol, jcol]
                if check == 0 and icol != jcol:
                    eleminated_features.append(jcol)
                    if icol in selected_categorical_features:
                        pass
                    else:
                        selected_categorical_features.append(icol)

    #df.loc[:, selected_categorical_features].to_csv('D:\House Price Prediction\Datasets/selected_cat_features.csv')
    for i in selected_categorical_features:
        print("Selected Features:" + i)
    for x in eleminated_features:
        print("eleminated Features: "+ x)


def correlation_of_numerical_features ():
    # this function calculates correlation between numerical features and 'salesPrice'
    # to find best numerical features
    df = pd.read_csv('D:\House Price Prediction\Datasets/numerical_data.csv', na_filter=False)

    # i used various finding techniques
    corr = df.corr(method= 'pearson')
    print(corr)
    corr = df.corr(method='kendall')
    print(corr)
    corr = df.corr(method='spearman')
    print(corr)
    i = 1
    for colums in df:
        a = stats.pearsonr(df[colums], df['SalePrice'])
        print( str(i) +") correlation of column  " + colums +":--------->"+ "Sales Price :--------->" +str(a))
        i += 1

    # for select Kbest f_regression function is used that returns f_Score
    X_train, X_test, y_train, y_test = train_test_split(df.loc[:, df.columns != 'SalePrice'],df['SalePrice'], test_size=0.3, random_state=100)
    fs = SelectKBest(score_func=f_regression, k = 10 )
    fs.fit(X_train,y_train)
    X_train_fs= fs.transform(X_train)
    x_test_fs = fs.transform(X_test)
    print("regression test results:")
    for i in range(len(fs.scores_)):
        print('Feature %d: %f' % (i, fs.scores_[i]))

    # we observed that all these correlation tests performed above using
    # various methods give almost the same correlation results

def plots():
    # Distribution plot
    df = pd.read_csv('D:\House Price Prediction\Datasets/numerical_data.csv', na_filter=False)
    sb.distplot(df['SalePrice'], color='r')
    plt.title('Sale Price Distribution', fontsize=16)
    plt.xlabel('Sale Price', fontsize=14)
    plt.ylabel('Frequency', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.savefig('D:\House Price Prediction\Plots/distplot_price.png')
    plt.show()

plots()