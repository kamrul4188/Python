li = []

print ("\nWelcome ! This program we are going to create 'List'")
while True:
    print("===========================================================")
    print("List = ", li)



    number = input ("Please enter your preferancnce [add/remove/sort/reverse/exit] : ")

    if number == "add":
        name = input("Enter a name you want to add: ")
        li.append(name) #Adding to list
    elif number == "rm":
        name = input ("Enter a name you want to remove: ")
        li.remove(name) #Remove from the list
    elif number == "exit":
        print ("Program terminated")
        break
    else:
        print("add = adding new name ")
        print("rm = remove name from the list")
        print("exit = terminate the Program")
