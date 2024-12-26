import os
import re

def organize(file):
    filename,file_extension = os.path.splitext(file)
    number = -1
    while filename[number].isdigit():
        number-=1
    key=filename[:number].strip()
    value=filename
    return (key,value)
