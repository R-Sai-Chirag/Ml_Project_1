import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.exception import coustom_execption
from sklearn.model_selection import train_test_split

@dataclass
class data_ingestion_config:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")


class dataingestion:
    def __init__(self):
        self.ingestionconfig=data_ingestion_config()

    def initiate_data_ingestion(self):
        try:
            df=pd.read_csv("stud.csv")
            os.makedirs(os.path.dirname(self.ingestionconfig.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestionconfig.raw_data_path,index=False,header=True)

            train_data,test_data=train_test_split(df,random_state=10,test_size=0.25)

            test_data.to_csv(self.ingestionconfig.train_data_path,index=False,header=True)
            train_data.to_csv(self.ingestionconfig.test_data_path,index=False,header=True)

            return(
                self.ingestionconfig.train_data_path,
                self.ingestionconfig.test_data_path
            )

        except Exception as e:
            raise coustom_execption(e,sys)
        


