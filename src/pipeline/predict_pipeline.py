import pandas as pd
import sys
from src.exception import coustom_execption
from src.utils import load_object


class predictpipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path="artifacts\model.pkl"
            preprocessor_path="artifacts\preprocessor.pkl"
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            scaled_data=preprocessor.transform(features)
            pred=model.predict(scaled_data)
            return pred
        except Exception as e:
            raise coustom_execption(e,sys)
        

class CoustomData:
    def __init__(self,gender:str,race_ethnicity:str,parental_level_of_education,lunch:str,test_preparation_course:str,reading_score:int,writing_score:int):

        self.gender=gender
        self.race_ethnicity=race_ethnicity
        self.parental_level_of_education=parental_level_of_education
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score
        self.lunch=lunch
        
    def get_data_as_dataframe(self):
        try:
            coustom_data={
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]
                }

            return pd.DataFrame(coustom_data)
            
        except Exception as e:
                raise coustom_execption(e,sys)
                
