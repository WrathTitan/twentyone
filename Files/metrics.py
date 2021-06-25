from sklearn.metrics import accuracy_score , recall_score, precision_score, f1_score, cohen_kappa_score, matthews_corrcoef
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,mean_squared_log_error


class Matrics:

    def calculate_metrics(modelname,model_type,metrics,prediction,y): # nested list
    
        if model_type=="classification":
            metrics.loc[len(metrics.index)]=[modelname,accuracy_score(y,prediction),recall_score(y,prediction),precision_score(y,prediction),f1_score(y,prediction),cohen_kappa_score(y,prediction),matthews_corrcoef(y,prediction)]

        elif model_type=="regression":
            metrics.loc[len(metrics.index)]=[modelname,mean_absolute_error(y,prediction),mean_squared_error(y,prediction),r2_score(y,prediction),mean_squared_log_error(y,prediction)]