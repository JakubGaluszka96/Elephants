import pandas as pd
import os

test_directory="/testdata/zadanie_B/slo1.in"

def readfile(file_dir):
    path = os.getcwd()+file_dir
    print(path)
    txt_file = open(path, "r")
    content = txt_file.read()
    txt_file.close()
    return content


def DataAssignment(file_dir):
    content=readfile(file_dir)
    lists=content.split('\n')
    elephants_count=lists[0]
    elephants_masses=lists[1].split(' ')
    current_order=lists[2].split(' ')
    desired_order=lists[3].split(' ')
    return elephants_count, elephants_masses, current_order, desired_order


elephants_count, elephants_masses, current_order, desired_order = DataAssignment(test_directory)
print(elephants_masses)
