import os

test_directory="/testdata/zadanie_B/slo10b.in"

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


def Permutation(file_dir):
    elephants_count, elephants_masses, current_order, desired_order = DataAssignment(file_dir)
    permutation=[]
    for i in current_order:
        permutation.append(desired_order.index(i))
    return permutation

def SubCycles(file_dir):
    elephants_count, elephants_masses, current_order, desired_order = DataAssignment(file_dir)
    permutation=Permutation(file_dir)
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


def Method1(file_dir):
    AllSubCycles, AllMasses = SubCycles(file_dir)
    Effort=0
    for i in AllMasses:
        suma=sum(i)
        minimal=min(i)
        result=suma+(len(i)-2)*minimal
        Effort=Effort+result
    return Effort
    

def Method2(file_dir):
    AllSubCycles, AllMasses = SubCycles(file_dir)
    Effort=0
    flatMass = [ item for elem in AllMasses for item in elem]
    minimal_global=min(flatMass)
    for i in AllMasses:
        suma=sum(i)
        minimal=min(i)
        result=suma+minimal+(len(i)+1)*minimal_global
        Effort=Effort+result
    return Effort

def Result(file_dir):
    Result=min(Method1(file_dir),Method2(file_dir))
    return Result

print(Result(test_directory))