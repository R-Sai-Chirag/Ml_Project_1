import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from dataclasses import dataclass
from src.exception import coustom_execption
import os
from src.utils import save_obj

@dataclass
class datatransformationconfig:
    preprocessor_obj_file_path:str=os.path.join("artifacts","preprocessor.pkl")

class data_transformation:
    def __init__(self):
        self.data_transformation_config=datatransformationconfig()

    def get_data_transformer_objects(self):
        try:
            cate_features=['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            num_features=['reading_score', 'writing_score']

            num_pipe=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("StandardScaler",StandardScaler(with_mean=False))
            ])

            cate_pipe=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("ohe",OneHotEncoder()),
                ("scaler",StandardScaler(with_mean=False))
            ])

            preprocessor=ColumnTransformer([
                ("cate_pipeline",cate_pipe,cate_features),
                ("num_pipeline",num_pipe,num_features)
            ])

            return preprocessor
        

        except Exception as e:
            raise coustom_execption(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            preprocessor_obj=self.get_data_transformer_objects()

            input_feature_train=train_df.drop(columns=["math_score"])
            target_feature_train=train_df["math_score"]

            input_feature_test=test_df.drop(columns=["math_score"])
            target_feature_test=test_df["math_score"]

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test)

            train_arr=np.c_[
                input_feature_train,np.array(target_feature_train)
            ]

            test_arr=np.c_[
                input_feature_test,np.array(target_feature_test)
            ]

            save_obj(file_path=self.data_transformation_config.preprocessor_obj_file_path,object=preprocessor_obj)

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as e:
            raise coustom_execption(e,sys)

            
