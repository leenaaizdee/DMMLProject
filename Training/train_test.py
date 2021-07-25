from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_validate
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import Lasso
from numpy import mean
import joblib

def cross_validation_Models_evaluation():
    df = pd.read_csv('D:\House Price Prediction\Datasets/final_feature_set.csv', na_filter=False)
    X_train, X_test, y_train, y_test = train_test_split(df.loc[:, df.columns != 'SalePrice'],
                                                        df['SalePrice'], test_size=0.3, train_size=0.7,
                                                        random_state=np.random.seed(0))
    X_trainn = df.loc[:, df.columns != 'SalePrice']
    y_trainn = df['SalePrice']

    # Regression Model based Multiple Linear Regression Algorithm
    #lm = linear_model.LinearRegression()
    #scores = cross_val_score(lm, X_trainn,y_trainn, scoring='r2', cv= 10)
    #scores = cross_validate(lm, X_trainn,y_trainn, scoring=('r2','neg_mean_absolute_percentage_error','explained_variance'), cv= 10)
    #print(mean(scores['test_neg_mean_absolute_percentage_error']))
    #print(mean(scores['test_r2']))
    #print(mean(scores['test_explained_variance']))

    # fitting model
    #lm.fit(X_train,y_train)

    # making predictions
    #predict_y = lm(X_test)



    #Regression Model based on Random Forest Algorithm
    #ran_forest = RandomForestRegressor(max_depth=2, random_state=0)
    #scores = cross_validate(ran_forest, X_trainn, y_trainn,scoring=('r2', 'neg_mean_absolute_percentage_error', 'explained_variance'), cv=10)
    #print("results for ran_forest")
    #print(mean(scores['test_neg_mean_absolute_percentage_error']))
    #print(mean(scores['test_r2']))
    #print(mean(scores['test_explained_variance']))

    # fitting model
    #ran_forest.fit(X_train,y_train)

    # making predictions
    #predict_y = ran_forest(X_test)

    # Regression based on k-nearest neighbors
    #neigh = KNeighborsRegressor(n_neighbors=10)
    #scores = cross_validate(neigh, X_trainn, y_trainn,scoring=('r2', 'neg_mean_absolute_percentage_error', 'explained_variance'), cv=10)
    #print("results for k-nearest neighbors")
    #print(mean(scores['test_neg_mean_absolute_percentage_error']))
    #print(mean(scores['test_r2']))
    #print(mean(scores['test_explained_variance']))

    # fitting model
    #neigh.fit(X_train,y_train)

    # making predictions
    #predict_y = neigh(X_test)

    # Regression model based on Elastic Net algorithm
    en = ElasticNet(alpha=0.01)
    scores = cross_validate(en, X_trainn, y_trainn,scoring=('r2', 'neg_mean_absolute_percentage_error', 'explained_variance'), cv=10)
    print("results for Elastic Net")
    print(mean(scores['test_neg_mean_absolute_percentage_error']))
    print(mean(scores['test_r2']))
    print(mean(scores['test_explained_variance']))

    # fitting model
    en.fit(X_train,y_train)

    # making predictions
    #predict_y = en(X_test)


    # Linear  Regression model based on Lasso algorithm
    #lasso = Lasso(alpha=0.01)
    #scores = cross_validate(lasso, X_trainn, y_trainn,scoring=('r2', 'neg_mean_absolute_percentage_error', 'explained_variance'), cv=10)
    #print("results for Lasso")
    #print(mean(scores['test_neg_mean_absolute_percentage_error']))
    #print(mean(scores['test_r2']))
    #print(mean(scores['test_explained_variance']))

    # fitting model
    #lasso.fit(X_train, y_train)

    # making predictions
    #predict_y = lasso(X_test)

    # after evaluating Performance metrics of above shown model
    # ElasticNet regression model is most suitable
    # Saving Trained Model
    joblib.dump(en,'D:\House Price Prediction\Frontend/trained_model.pkl')


    # load the model from disk
    #loaded_model = pickle.load(open(filename, 'rb'))
    #result = loaded_model.score(X_test, Y_test)


cross_validation_Models_evaluation()

