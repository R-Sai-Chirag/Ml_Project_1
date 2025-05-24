import os
import sys
import pandas as pd
import numpy as np
from src.exception import coustom_execption
import dill
from sklearn.metrics import r2_score


def save_obj(file_path,object):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(object,file_obj)
    
    except Exception as e:
        raise coustom_execption(e,sys)
    
    
def evaluate_models(X_train,X_test,y_train,y_test,models):
    try:
        report={}

        for name,model in models.items():
            model.fit(X_train,y_train)

            y_pred=model.predict(X_test)

            model_score=r2_score(y_test,y_pred)

            report[name]=model_score

        return report
    
    except Exception as e:
        raise coustom_execption(e,sys)

    