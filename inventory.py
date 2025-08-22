cart = []

while True:
    print("\n Menu")
    print("1.Add")
    print("2.Search")
    print("3.Update")
    print("4.Remove")
    print("5.Exit")
    choice = input("Enter a choice: ")
    
    if choice == "1":
        name = input("Entert name: ")
        price = input("Enter price: ")
        cart.append({"name":name,"price":price})
        print(f"Added {name} : {price}")
    
    elif choice == "2":
        search = input("Enter name: ")
        for item in cart:
          if item.get("name") == search:
            print("Found")
          else:
            print("Not found")
            
    elif choice == "3":
         for item in cart:
           price = int(item.get("price") )
           name  = item.get("name") 
           if price >= 5000:
                  price = price*10/100
                  print(f"New price : {name}:{price}")
           
    
    elif choice == "4":
        name =  input("Entert name: ")
        for item in cart:
          if item.get("name") == name:
            cart.remove(item)
            print(f"{name} removed")
      
    
    elif choice == "5":
        break
            
                  
              