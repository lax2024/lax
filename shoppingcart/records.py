# stu_rec = {}

# while True:
#     print("\nStudent Record")  
#     print("1. Add student")
#     print("2. Update student")
#     print("3. Remove student")
#     print("4. View all students")
#     print("5. Search student")
#     print("6. Length of student records")
#     print("7. Exit")
    
#     choice = input("Enter a choice: ")

#     if choice == "1":
#         roll_no = int(input("Enter a Roll Number: "))
#         st_name = input("Enter a name: ")
#         stu_rec[roll_no] = st_name
#         print("Record inserted")
     
#     elif choice == "2":
#         roll_no = int(input("Enter a Roll Number to update: "))
#         if roll_no in stu_rec:
#             new_name = input("Enter a new name: ")
#             stu_rec[roll_no] = new_name
#             print("Name updated")
#         else:
#             print("No such roll number")
    
#     elif choice == "3":
#         roll_no = int(input("Enter a Roll Number to remove: "))
#         if roll_no in stu_rec:
#             stu_rec.pop(roll_no)
#             print("Student removed")
#         else:
#             print("No such roll number")
    
#     elif choice == "4":
#         if stu_rec:
#             print("\nStudent Records:")
#             for roll_no, st_name in stu_rec.items():
#                 print(f"Roll No: {roll_no}, Name: {st_name}")
#         else:
#             print("No student records found")
    
#     elif choice == "5":
#         roll_no = int(input("Enter a Roll Number to search: "))
#         if roll_no in stu_rec:
#             print(f"Student : Roll No: {roll_no}, Name: {stu_rec[roll_no]}")
#         else:
#             print("Student not found")
    
#     elif choice == "6":
#         print(f"Total number of students: {len(stu_rec)}")
    
#     elif choice == "7":
#         print("Exiting program...")
#         break
    
#     else:
        # print("Invalid choice. Please enter a number between 1 and 7.")


# a_hobbies = {"Reading","Writing","Singing","Dancing"}
# b_hobbies = {"Singing","Dancing","Crocheting","Drawing"}

# c_hobbies = a_hobbies.intersection(b_hobbies)
# print(f"common hobbies : {c_hobbies}")

# d_hobbies = a_hobbies.difference(b_hobbies)
# print(f"common hobbies : {d_hobbies}")

# u_hobbies =  a_hobbies.union(b_hobbies)
# print(f"common hobbies : {u_hobbies}")




fruits = {"Mango","Strawberry","Kiwi","Grapes","Guava"}

f_name = input("Enter a fruit: ")

if f_name in fruits:
    print(f"{f_name} is in fruits")
else:
    print("Not found")
