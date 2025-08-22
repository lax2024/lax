my_list = ["Manu","Zama","Zoya","Vignesh"]
# print(my_list)

# print(my_list[0])

# print(my_list[1:3])

my_list.append("Deva")
my_list.append("Arya")
my_list.append("Saya")
my_list.append("Mala")
# print(my_list)

# if "Deva" in my_list:
#     print("yes it is in list")
# else:
#     print("No, It is not in list")

reg = [{"Roll_no":1, "Age":20},{"Roll_no":2, "Age":21},{"Roll_no":3, "Age":21},{"Roll_no":4, "Age":22},{"Roll_no":5, "Age":20},{"Roll_no":6, "Age":20},{"Roll_no":7, "Age":20}]
        
my_dict =   dict(zip(my_list,reg))
print(my_dict)
    
my_list.remove("Mala")
print(my_list)

while True:
    print("\n Menu")
    print("1.Add")
    print("2.View")
    print("3.Exit")
    choice = input("Enter a choice: ")
    
    if choice == "1":
        new = input("Enter name to add: ")
        
        roll_no = int(input("Enter roll no to add: "))
        # if roll_no not in my_dict:
        age = int(input("Enter age to add: "))
        
        my_dict[new] = {"Roll_no":roll_no,"Age":age}
        print("Name added")
        # else :
        #     print("roll no already exists")
            
        # my_list.append(new)
        
        # print(my_dict)
    
    elif choice == "2":
        # print(my_list)
        # for i in my_dict:
        #     print(i)
        
        for name, details in my_dict.items():
           print(f"name: {name}")
           for key, value in details.items():
              print(f"  {key}: {value}")
        
            
        # for i,it in enumerate(my_list,1):
        #     print(i,it)
            
        
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
        


    
    