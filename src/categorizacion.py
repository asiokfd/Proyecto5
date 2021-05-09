import pandas as pd





def categorizacion(df):
    """
    función que recibe como parámetro un dataframe determinado y categoriza varias de sus columnas y elimina la columna id
    """
    cortes = { "Fair": 1,
                "Good": 2,
                "Very Good": 3,
                "Premium":4,
                "Ideal":5
                }
    claridad = { "I1": 1,
                "SI2": 1.5,
                "SI1": 2,
                "VS2" : 2.5,
                "VS1" : 3,
                "VVS2": 3.5,
                "VVS1": 4,
                "IF" : 5
                }
    color = {
                "J": 1,
                "I": 2,
                "H" : 3,
                "G" : 4,
                "F": 5,
                "E": 6,
                "D" : 7
                }
    df.cut = df.cut.map (cortes)
    df.color = df.color.map (color)
    df.clarity = df.clarity.map (claridad)
    df.drop (["id"], axis=1, inplace = True)
    return df