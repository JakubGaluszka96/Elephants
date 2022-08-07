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


def Permutation(current_order, desired_order):
    permutation=[]
    for i in current_order:
        permutation.append(desired_order.index(i))
    return permutation


def SubCycles(elephants_count, elephants_masses, current_order, desired_order):
    permutation=Permutation(current_order, desired_order)
    indicator=[False for i in range(elephants_count)]
    AllSubCycles=[] 
    AllMasses=[]
    for i in range(0, elephants_count):             
        x=i
        if indicator[x]==False:
            SubCycle=[]
            Masses=[]  
            while indicator[x] == False:
                SubCycle.append(current_order[x])
                Masses.append(elephants_masses[x])
                indicator[x]=True
                x=permutation[x]
            AllSubCycles.append(SubCycle)
            AllMasses.append(Masses)
    return AllSubCycles, AllMasses


def Method1(suma, minimal, vertices):
    result=suma+(vertices-2)*minimal
    return result
    

def Method2(suma, minimal, minimal_global, vertices):
    result=suma+minimal+(vertices+1)*minimal_global
    return result


def Result(file_dir):
    elephants_count, elephants_masses, current_order, desired_order=DataAssignment(file_dir)
    minimal_global=min(elephants_masses)
    AllSubCycles, AllMasses = SubCycles(elephants_count, elephants_masses, current_order, desired_order)
    Effort=0
    for i in AllMasses:
        suma=sum(i)
        minimal=min(i)
        vertices=len(i)
        Result_met1=Method1(suma, minimal, vertices)
        Result_met2=Method2(suma, minimal, minimal_global, vertices)
        Result=min(Result_met1, Result_met2)
        Effort=Effort+Result
        print(Effort)
    return Effort


Result(test_directory)