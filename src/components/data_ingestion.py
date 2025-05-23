import os
import sys
import pandas as pd

from src.exception import coustom_execption
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.components.data_transformation import data_transformation,datatransformationconfig


@dataclass
class dataingestionconfig:
    train_data_path: str=os.path.join("artifacts","train.csv")
    test_data_path: str=os.path.join("artifacts","test.csv")
    raw_data_path: str=os.path.join("artifacts","data.csv")

class dataingestion:
    def __init__(self):
        self.ingestion_config=dataingestionconfig()

    def initiate_data_ingestion(self):
        try:
          df=pd.read_csv("stud.csv")
          os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

          df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

          train_set,test_set=train_test_split(df,random_state=10,test_size=0.25)

          train_set.to_csv(self.ingestion_config.train_data_path,index=False)

          test_set.to_csv(self.ingestion_config.test_data_path,index=False)

          return(
              self.ingestion_config.train_data_path,
              self.ingestion_config.test_data_path
          )
        
        except Exception as e:
            raise coustom_execption(e,sys)
        
if __name__=="__main__":
    obj=dataingestion()
    train_data,test_data=obj.initiate_data_ingestion()

    datatransformation=data_transformation()
    datatransformation.initiate_data_transformation(train_data,test_data)
