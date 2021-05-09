import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import metrics
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV




def probando_modelos(dicmodel):
    """
    Función que recibe como parámetro un diccionario con modelos de predicción, y con un split ya definido, 
    nos devuelve el mse para cada modelo
    """
    for name, model in dicmodel.items():
        model.fit (X_train, y_train)
        y_pred =model.predict (X_test)
        print(f"--------{name}--------")
        print("MSE: ", metrics.mean_squared_error(y_test,y_pred))

def probando_modelos_cross(dicmodel):
    """
    Función que recibe como parámetro un diccionario de modelos de predicción y nos devuelve la media del mse después de hacer un
    cross validation en 5 partes
    """
    for name, model in dicmodel.items():
        model.fit (X_train, y_train)
        scores = cross_val_score(model, X_train, y_train, scoring = "neg_mean_squared_error", cv=5)
        print(f"{name} MSE {np.mean(scores)}" )







