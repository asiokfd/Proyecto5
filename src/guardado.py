import pandas as pd


def preparando_submision (df, nombre):
    """funcion que recibe como parámetros un dataframe y un nombre, crea una columna con una prediccion previamente realizada, y guarda un
    csv con el nombre que recibe como parametro, en el csv solo se incluye el index con nombre id, y la nueva columna
    """
    df["price"] = y_pred
    submision=df[["price"]]
    submision.index.rename ("id", inplace=True)
    submision.to_csv ("../Data/" + nombre + ".csv")