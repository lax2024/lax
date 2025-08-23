library = [("1001","Cruel Prince","Holly Black",2016),("1002","A Good Girl's Guide To Murder","Holly Jackson",2017),("1003","Fouth Wing","Rebbecca Yarrows",2024)]
def fun():
    while True:
        print("\n Options")
        print("1.Search")
        print("2.Display")
        print("3.Count")
        print("4.Exit")
        
        choice = int(input("Enter a choice: "))
        if choice == 1:
            search = input("Enter book title or id to search: ")
            for item in library:
                id = item.get("id")
                title = item.get("title")
                
                
                i