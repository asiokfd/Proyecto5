import pandas as pd




def resultados_gridDT (gsr):
    """
    Funcion que recibe un gridsearch entrenado con decission tree regressor y nos devuelve un dataframe con los resultados ordenados
    """
    gsresults = pd.DataFrame(gsr.cv_results_)
    gsresults = gsresults[['param_max_depth', 'param_max_features', 'param_min_samples_split',
       'mean_test_score', 'mean_train_score']]
    display (gsresults.sort_values("mean_test_score", ascending=False).head(10))
    

def resultados_gridGBR (gsname):
    """
    Funcion que recibe un gridsearch entrenado con gradient boosting regressor y nos devuelve un dataframe con los resultados ordenados
    """
    gsresults = pd.DataFrame (gsname.cv_results_)
    gsresults = gsresults [['param_n_estimators', 'param_learning_rate',
       'mean_test_score', 'mean_train_score']]
    display (gsresults.sort_values( "mean_test_score" , ascending=False).head(10))