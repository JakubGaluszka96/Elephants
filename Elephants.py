import pandas as pd
import os

def readfile(file_dir):
    path = os.getcwd()+file_dir
    print(path)
    txt_file = open(path, "r")
    content = txt_file.read()
    txt_file.close()
    return content;

#print(readfile("/testdata/zadanie_B/slo1.in"))
def DataAssignment(file_dir):
    content=readfile(file_dir)
    lists=content.split('\n')
    El_count=lists[0]
    El_mass=lists[1].split(' ')
    El_primary=lists[2].split(' ')
    El_desired=lists[3].split(' ')
    return El_count, El_mass, El_primary, El_desired;

a, b, c, d = DataAssignment("/testdata/zadanie_B/slo1.in")
print(a)
print(b)
print(c)
print(d)