import sys
import traceback

def custom_exception(error):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error in Filename [{0}] line number [{1}] : Error Message: [{2}]".format(
        filename,line_number,str(error)
    )
    return error_message

