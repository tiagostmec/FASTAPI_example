import os 
from services.logger import logger

def size(values, field_name, route):
    if len(values) < 3:
        error_msg = f"{route}: {field_name} expects 3 elements minimum"
        logger.error(error_msg, extra={'route': route})
        raise ValueError(error_msg)
    return values

'''
Validator to check size... in a real environment we MUST need to make more validators.
Example: check if the sizes matches, check negatives.. etc.
'''