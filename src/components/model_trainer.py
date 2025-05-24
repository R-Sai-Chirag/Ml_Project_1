import os
import sys
from src.exception import coustom_execption
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from dataclasses import dataclass
from src.utils import evaluate_models,save_obj
from sklearn.metrics import r2_score

@dataclass
class model_trainer_config:
    trained_model_path:str=os.path.join("artifacts","model.pkl")

class modeltrainer:
    def __init__(self):
        self.modeltrainerconfig=model_trainer_config()

    def initiate_model_training(self,train_arr,test_arr):
        try:
            X_train,y_train,X_test,y_test=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models={
                "randomforest":RandomForestRegressor(),
                "linear reg":LinearRegression(),
                "logistic reg":LogisticRegression(),
                "random forest":RandomForestRegressor(),
                "decision tree":DecisionTreeRegressor(),
                "gradient boost":GradientBoostingRegressor(),
                "ada boost":AdaBoostRegressor(),
                "SVR":SVR(),
                "knn":KNeighborsRegressor()
            }

            model_report:dict=evaluate_models(X_train,X_test,y_train,y_test,models)

            best_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_score)]
            best_model=models[best_model_name]

            if best_score<0.6:
                raise coustom_execption("NO BEST MODEL FOUND!!!")
            

            save_obj(file_path=self.modeltrainerconfig.trained_model_path,
                     object=best_model)
            
            predicted=best_model.predict(X_test)
            r2score=r2_score(y_test,predicted)

            return r2score,best_model_name
        except Exception as e:
            raise coustom_execption(e,sys)
        