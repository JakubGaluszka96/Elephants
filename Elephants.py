import os
import sys


test_directory="/testdata/slo10b.in"
#resource.setrlimit(resource.RLIMIT_AS, (100e+7,100e+7))




###-odczyt pliku
def read_file(file_dir):
    path = os.getcwd()+file_dir
    txt_file = open(path, "r")
    content = txt_file.read()
    txt_file.close()
    return content


###-przypisanie wartosci z pliku do zmiennych
def data_assignment_file(file_dir):
    elephants_count=int(read_file(file_dir).split('\n')[0])
    elephants_masses=list(map(int, read_file(file_dir).split('\n')[1].split(' ')))
    current_dict=dict(zip(range(elephants_count), list(map(int, read_file(file_dir).split('\n')[2].split(' ')))))
    desired_dict=dict(zip(list(map(int, read_file(file_dir).split('\n')[3].split(' '))), range(elephants_count)))
    return elephants_count, elephants_masses, current_dict, desired_dict


def data_assignment_input(input1, input2, input3, input4):
    elephants_count=int(input1)
    elephants_masses=list(map(int,input2.split(' ')))
    current_dict=dict(zip(range(elephants_count), list(map(int, input3.split(' ')))))
    desired_dict=dict(zip(list(map(int, input4.split(' '))), range(elephants_count)))
    return elephants_count, elephants_masses, current_dict, desired_dict


def data_assignment_argument():
    elephants_count=sys.argv[1].split('\n')
    elephants_masses = sys.argv[1].split('\n')[1].split(' ')
    current_dict=dict(zip(range(elephants_count), list(map(int, sys.argv[1].split('\n')[2].split(' ')))))
    desired_dict=dict(zip(list(map(int, sys.argv[1].split('\n')[3].split(' '))), range(elephants_count)))
    return elephants_count, elephants_masses, current_dict, desired_dict

###-stowrzenie listy permutacji
def get_permutation(Dict1, Dict2, elephants_count):
    permutation=[Dict2.get(Dict1.get(i)) for i in range(elephants_count)]
    return permutation


###-stworzenie listy podcykli
def get_subcycles(current_order, permutation):
    lenght=len(permutation)
    indicator=[False for i in range(lenght)]
    all_subcycles=[] 
    for i in range(0, lenght):             
        x=i
        if indicator[x]==False:
            SubCycle=[]
            while indicator[x] == False:
                SubCycle.append(current_order[x])
                indicator[x]=True
                x=permutation[x]
            #if len(SubCycle)>1:
            all_subcycles.append(SubCycle)
    return all_subcycles

###-przypisanie masy kolejnym elementom podcykli
def get_masses_subcycles(elephants_masses, all_subcycles):
    all_masses=[[elephants_masses[x-1] for x in all_subcycles[i]] for i in range(len(all_subcycles))]
    return all_masses


###-obliczenie wysilku przy uzyciu 1 metody dla jednego podcyklu
def method1(suma, minimal, vertices):
    result=suma+((vertices-2)*minimal)
    return result


###-obliczenie wysilku przy uzyciu 2 metody dla jednego podcyklu
def method2(suma, minimal, minimal_global, vertices):
    result=suma+minimal+((vertices+1)*minimal_global)
    return result


###-obliczenie wysilku
def calc_effort(all_masses, minimal_global):
    effort=0
    for i in all_masses:
        suma=sum(i)
        minimal=min(i)
        vertices=len(i)
        result_met1=method1(suma, minimal, vertices)
        result_met2=method2(suma, minimal, minimal_global, vertices)
        result=min(result_met1, result_met2)
        effort=effort+result
    return effort


###-funkcja wywolujaca po koleji metody celem uzyskania wyniku, czyli wysilku
def get_result(input):
    if len(sys.argv) > 1:
        elephants_count, elephants_masses, current_order, desired_order=data_assignment_argument()
    else:
        elephants_count, elephants_masses, current_order, desired_order=data_assignment_file(input)
    minimal_global=min(elephants_masses)
    permutation=get_permutation(current_order, desired_order, elephants_count)
    all_subcycles =get_subcycles(current_order, permutation)
    all_masses=get_masses_subcycles(elephants_masses, all_subcycles)
    effort=calc_effort(all_masses, minimal_global)
    return effort

print(get_result(test_directory))