emoji = {"sad":"🥲" ,"happy":"😊","angry":"😡"}

stmt = input("Enter your message: ")

feeling = stmt.split()


for i in range(len(feeling)):
    if feeling[i] == "sad": 
        feeling[i] = emoji["sad"]  
    elif feeling[i] == "happy": 
        feeling[i] = emoji["happy"]
    elif feeling[i] == "happy": 
        feeling[i] = emoji["angry"]   


stmt = " ".join(feeling)
print(stmt)
            
     

    


 