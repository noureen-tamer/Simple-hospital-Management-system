import sys
maxsize = 10
hos = {i: [] for i in range(1, 21)}


def add(specialization, name, case):
    if len(hos[specialization]) >= maxsize:
        print("u have more 10 patients")
        return
    newaptient = {"name": name, "case": case}
    if case == 0:
        hos[specialization].append(newaptient)
    elif case == 1:
        for i, x in enumerate(hos[specialization]):
            if x["case"] == 0:
                hos[specialization].insert(i, newaptient)
                break
        else:
            hos[specialization].append(newaptient)
    elif case == 2:
        for i, x in enumerate(hos[specialization]):
            if x["case"] == 0 or x["case"] == 1:
                hos[specialization].insert(i, newaptient)
                break
        else:
            hos[specialization].append(newaptient)
    print1(specialization)


def print1(specialization):
    for i, p in hos.items():
        if i == specialization:
            num = len(p)
            if num == 0:
                continue
            has_patients = True
            print(f'specialization {i}: there are {num} patients')

            for n in p:
                case = "normal" if n["case"] == 0 else "urgent" if n["case"] == 1 else "superurgent"
                print(f'patient: {n["name"]} is {case}')


def printallpatients():
    has_patients = False
    for i, p in hos.items():
        num = len(p)
        if num == 0:
            continue
        has_patients = True
        print(f'specialization {i}: there are {num} patients')
        for n in p:
            case = "normal" if n["case"] == 0 else "urgent" if n["case"] == 1 else "superurgent"
            print(f'patient: {n["name"]} is {case}')
    if not has_patients:
        print("there are no patients currently at any specialization ")


def getnextpatient(specialization):
    for i, p in hos.items():
        if i == specialization:
            print(f"{p[0]['name']} go to the doctor")
            del p[0]


def removepatient(specialization, name):
    for i, p in hos.items():
        if i == specialization:
            for n in p:
                if n["name"] == name:
                    p.remove
while True:
    print(f"program options:\n1) add new patient:\n2) print all patients\n3) "
    f"get next patient\n4) remove next patient\n5) End the program")
    program=int(input("enter your choice form 1 to 5"))
    while program not in range(1,6):
        print("Error: please enter a valid number")
    if program==1: # program 1 is adding new patient
        spec=int(input("enter the specialization please:"))
        name=str(input("enter the name of the patient:"))
        status=int(input("enter the case of the patient:"))
        add(spec,name,status)
        print("-------------------------")
    elif program ==2: # program 2 is to print all patients
        printallpatients()
        print("--------------------------")
    elif program==3: # program 3 is to get the next patient
        spec= int(input("enter the specialization:"))
        getnextpatient()
        print("----------------------------")
    elif program==4:
        spec=int(input("enter the specialization:"))
        name=input("enter the name:")
        removepatient()
    elif program==5:
        print("End of the programs")
        sys.exit()