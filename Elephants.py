import os
from pathlib import Path
import time
import resource
import tracemalloc

test_directory="/testdata/zadanie_B/slo10b.in"
resource.setrlimit(resource.RLIMIT_AS, (100e+7,100e+7))


def readfile(file_dir):
    path = os.getcwd()+file_dir
    txt_file = open(path, "r")
    content = txt_file.read()
    txt_file.close()
    return content


def DataAssignment(file_dir):
    content=readfile(file_dir)
    lists=content.split('\n')
    elephants_count=int(lists[0])
    elephants_masses=list(map(int, lists[1].split(' ')))
    current_order=list(map(int, lists[2].split(' ')))
    desired_order=list(map(int, lists[3].split(' ')))
    return elephants_count, elephants_masses, current_order, desired_order

def DataAssignmentDict(file_dir):
    elephants_count=int(readfile(file_dir).split('\n')[0])
    elephants_masses=list(map(int, readfile(file_dir).split('\n')[1].split(' ')))
    current_order=list(map(int, readfile(file_dir).split('\n')[2].split(' ')))
    desired_order=list(map(int, readfile(file_dir).split('\n')[3].split(' ')))
    places=range(elephants_count)
    current_dict=dict(zip(places, current_order))
    desired_dict=dict(zip(desired_order, places))
    del current_order
    del desired_order
    return elephants_count, elephants_masses, current_dict, desired_dict



def Permutation(current_order, desired_order):
    permutation=[desired_order.index(i) for i in current_order]
    return permutation


def PermutationDict(Dict1, Dict2, elephants_count):
    permutation=[Dict2.get(Dict1.get(i)) for i in range(elephants_count)]
    return permutation


def SubCycles(current_order, permutation):
    lenght=len(permutation)
    indicator=[False for i in range(lenght)]
    AllSubCycles=[] 
    for i in range(0, lenght):             
        x=i
        if indicator[x]==False:
            SubCycle=[]
            while indicator[x] == False:
                SubCycle.append(current_order[x])
                indicator[x]=True
                x=permutation[x]
            #if len(SubCycle)>1:
            AllSubCycles.append(SubCycle)
    return AllSubCycles


def MakeSubCycle(current_order, permutation,x):
    SubCycle=[]
    while current_order[x] not in SubCycle:
        SubCycle.append(current_order[x])
        x=permutation[x]
    return SubCycle


def MakeMassMinimal(current_order, permutation,x):
    if x == False:
        SubCycle=[]
        while current_order[x] not in SubCycle:
            SubCycle.append(current_order[x])
            indicator[x]=True
            x=permutation[x]
    suma=sum(SubCycle)
    minimal=min(SubCycle)
    vertices=len(SubCycle)
    return suma, minimal, vertices


def Method1(suma, minimal, vertices):
    result=suma+((vertices-2)*minimal)
    return result
    

def Method2(suma, minimal, minimal_global, vertices):
    result=suma+minimal+((vertices+1)*minimal_global)
    return result


def Calc_Effort(AllMasses, minimal_global):
    Effort=0
    for i in AllMasses:
        suma=sum(i)
        minimal=min(i)
        vertices=len(i)
        Result_met1=Method1(suma, minimal, vertices)
        Result_met2=Method2(suma, minimal, minimal_global, vertices)
        Result=min(Result_met1, Result_met2)
        Effort=Effort+Result
    return Effort


def Result(file_dir):
    elephants_count, elephants_masses, current_order, desired_order=DataAssignmentDict(file_dir)
    minimal_global=min(elephants_masses)
    permutation=PermutationDict(current_order, desired_order, elephants_count)
    AllMasses = SubCycles(elephants_masses, permutation)
    AllSubCycles =SubCycles(current_order, permutation)
    Effort=Calc_Effort(AllMasses, minimal_global)
    return Effort

