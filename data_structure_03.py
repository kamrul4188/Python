#Now we are going to use methord called Dictionary

data = {}


while True:
    print("---------------------------------------------------------------")
    selection = input("Data entry type 'e' | Show Data type 's' : ")
    selection = selection.lower()
    print("---------------------------------------------------------------")

    if selection == "e":
        roll = input("Enter roll number : ")
        ban = input("Enter mark for Bangla : ")
        eng = input("Enter mark for English : ")
        math = input("Enter mark for Mathmatics : ")
        print("---------------------------------------------------------------")
        data [roll] = {"Bangla": ban, "English": eng, "Mathmatics": math}
        print("Data = ", data)
    elif selection == "s":
        roll = input("Enter roll number : ")
        print("---------------------------------------------------------------")
        print("mark for Bangla = ", data[roll]["Bangla"])
        print("mark for English = ", data[roll]["English"])
        print("mark all = ", data[roll])

    else:
        print("Wrong selection !!! Terminate program.......")
        break
