import os
import sys
import pandas as pd
import numpy as np
from src.exception import coustom_execption
import dill


def save_obj(file_path,object):
    try:
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(object,file_obj)
    
    except Exception as e:
        raise coustom_execption(e,sys)
    
    

    