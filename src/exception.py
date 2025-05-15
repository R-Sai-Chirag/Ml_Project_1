import sys 

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error in python script [{0}] at line [{1}] and it is a [{2}] error.".format(file_name,exc_tb.tb_lineno,str(error))
    file_name,exc_tb.tb_lineno,str(error)

    return error_message

class coustom_execption(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    try:
        d=1/0

    except Exception as e:
        raise coustom_execption(e,sys)