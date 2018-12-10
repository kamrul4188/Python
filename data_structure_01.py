li = []

print ("\nWelcome ! This program we are going to create 'List'")
while True:
    print("---------------------------------------------------------------------")
    print("List = ", li)
    print("---------------------------------------------------------------------")

    selector = input ("Please enter your preferancnce add/remove/sort/reverse/exit/pop/help : ")
    selector = selector.lower()

    if selector == "add":
        name = input("Enter a name you want to add: ")
        li.append(name) #Adding to list
    elif selector == "rm":
        name = input ("Enter a name you want to remove: ")
        li.remove(name) #Remove from the list
    elif selector == "pop":
        print ("Please add items in to lis first")
        number = input("Please number you want to pop : ")
        number = int(number)
        items = li.pop(number)
        print("The items is pop = ",  items)
    elif selector == "help":
        print("add = adding new name ")
        print("remove = remove name from the list")
        print("sort = sort a to z the list")
        print("reverse = reverse order of list")
        print("exit = terminate the Program")
    elif selector == "exit":
        print ("Program terminated...")
        break
    else:
        print("your input not match! Program terminated...")
        break
