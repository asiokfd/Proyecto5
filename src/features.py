import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, SGDRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import metrics
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import ElasticNet, Lars, BayesianRidge, ARDRegression, TweedieRegressor
from sklearn.linear_model import TheilSenRegressor, HuberRegressor, RANSACRegressor
import fmodels




def prueba_features (df, model, target):
    """
    Función que recibe como parámetro un dataframe, un modelo de previsión y un target, y nos devuelve un print de los resultados de la mse
    de aplicar el modelo eliminando los parámetros uno a uno.
    """
    columnas_x = [a for a in (list (df.columns)) if a != (target)]
    
    for feature in columnas_x:
        print (feature)
        df2 = df.drop ([feature], axis=1)
        X = df [columnas_x]
        y= df [target]
        X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2)
        model.fit (X_train, y_train)
        y_pred = gradient_model.predict (X_test)  
        print( "MSE: ", (metrics.mean_squared_error(y_test,y_pred)))


def prueba_features2 (df, model, target):
    """
    Función que recibe como parámetro un dataframe, un modelo de previsión y un target, y nos devuelve primero un print de los resultados(mse)
    de aplicar el modelo eliminando los parámetros uno a uno. y Luego un print con la media de los resultados aplicando cross validation
    
    """
    columnas_x = [a for a in (list (df.columns)) if a != (target)]
    
    for feature in columnas_x:
        print (feature)
        df2 = df.drop ([feature], axis=1)
        X = df [columnas_x]
        y= df [target]
        X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2)
        model.fit (X_train, y_train)
        y_pred = gradient_model.predict (X_test)  
        print( "MSE: ", (metrics.mean_squared_error(y_test,y_pred)))
        scores = cross_val_score(model, X, y, scoring = "neg_mean_scuared_error", cv=5)
        print(f"CROSSMSE {np.mean(scores)}" )

def prueba_features3 (df, model, target):
    """
    Función que recibe como parámetro un dataframe, un modelo de previsión y un target, y nos devuelve primero un print de los resultados
    de aplicar el modelo eliminando los parámetros uno a uno. y Luego un print con la media de los resultados aplicando cross validation
    pero en este caso, el error absoluto
    """
    columnas_x = [a for a in (list (df.columns)) if a != (target)]
    
    for feature in columnas_x:
        print (feature)
        df2 = df.drop ([feature], axis=1)
        X = df [columnas_x]
        y= df [target]
        X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2)
        model.fit (X_train, y_train)
        y_pred = gradient_model.predict (X_test)  
        print( "MSE: ", (metrics.mean_squared_error(y_test,y_pred)))
        scores = cross_val_score(model, X, y, scoring = "neg_mean_absolute_error", cv=5)
        print(f"CROAAMAE {np.mean(scores)}" )