li = []

print ("Welcome ! This program we are going to create 'List'")
while True:
    print("\n===========================================================")
    print("\nList = ", li)

    print("\nadd = adding new name ")
    print("rm = remove name from the list")
    print("exit = terminate the Program")

    number = input ("\nPlease enter your preferancnce [add/rm/exit] : ")

    if number == "add":
        name = input("Enter a name you want to add: ")
        li.append(name)
    elif number == "rm":
        name = input ("Enter a name you want to remove: ")
        li.remove(name)
    elif number == "exit":
        print ("Program terminated")
        break
