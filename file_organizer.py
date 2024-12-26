import os
import shutil

def organize_directory(path, strategy):
    file_dictionary = dict()
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path,file)):
            continue
        key,value = strategy.organize(file)
        file_dictionary[key] = value
    for key in file_dictionary.keys():
        new_dir = os.path.join(path,key)
        print(new_dir)
        os.makedirs(new_dir,exist_ok=True)
        for file in file_dictionary[key]:
            shutil.move(src=os.path.join(path,file),dst=os.path.join(new_dir,file))

