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
    elephants_count=int(lists[0])
    elephants_masses=list(map(int, lists[1].split(' ')))
    current_order=lists[2].split(' ')
    desired_order=lists[3].split(' ')
    return elephants_count, elephants_masses, current_order, desired_order

def Method1():
    elephants_count, elephants_masses, current_order, desired_order = DataAssignment(test_directory)
    suma=sum(elephants_masses)
    minimal=min(elephants_masses)
    result=suma+(elephants_count-2)*minimal
    return result
    
def Method2():
    elephants_count, elephants_masses, current_order, desired_order = DataAssignment(test_directory)
    suma=sum(elephants_masses)
    minimal=min(elephants_masses)
    result=suma+minimal+(elephants_count+1)*minimal
    return result

elephants_count, elephants_masses, current_order, desired_order = DataAssignment(test_directory)
print(Method1())
print(Method2())
