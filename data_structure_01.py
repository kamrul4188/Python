li = []

print ("\nWelcome ! This program we are going to create 'List'")
while True:
    print("---------------------------------------------------------------------")
    print("List = ", li)
    print("---------------------------------------------------------------------")

    number = input ("Please enter your preferancnce add/remove/sort/reverse/exit/help : ")
    number = number.lower()

    if number == "add":
        name = input("Enter a name you want to add: ")
        li.append(name) #Adding to list
    elif number == "rm":
        name = input ("Enter a name you want to remove: ")
        li.remove(name) #Remove from the list
    elif number == "help":
        print("add = adding new name ")
        print("remove = remove name from the list")
        print("sort = sort a to z the list")
        print("reverse = reverse order of list")
        print("exit = terminate the Program")
    elif number == "exit":
        print ("Program terminated...")
        break
    else:
        print("your input not match! Program terminated...")
        break
