students={}
def add_student():
    roll=input("enter roll number:")
    if roll in students:
        print("student already exists")
        return
    
    name=input("enter name:")
    marks=input("enter marks:")
    
    students[roll]={"Name": name,"Marks": marks}
    print("student Added succefully")

def search_students():
    roll=input("enter roll number to search:")
    
    if roll in students:
        print("Roll No:",roll)
        print("Name:",students[roll]["Name"])
        print("marks:",students[roll]["Marks"])
    else:
        print("student not found")

def update_students():
    roll=input("enter roll number to update:")
    
    if roll in students:
        name=input("enter new name:")
        marks=input("enter new marks:")
        
        students[roll]={"Name":name,"Marks":marks}
        print("student updated succesfully")
    else:
        print("student not found")
        
def delete_students():
    roll=input("enter roll number to delete:")
    
    if roll in students():
        if not students:
            print("no records found")
    else:
        print("\n student records:")
        for roll,data in students.item():
            print(f"roll no:{roll},Name: {data['Name']},Marks:{data['Marks']}")

def display_students():
    if not students:
        print("No Records Found")
    else:
        print("\nStudent Records:")
        for roll, data in students.items():
            print(f"Roll No: {roll}, Name: {data['Name']}, Marks: {data['Marks']}")
while True:
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Add student")
    print("2.Search students")
    print("3. Update students")
    print("4. Delete students")
    print("5. Display all students")
    print("6.Exit")
    
    choice=input("enter choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        search_students()
    elif choice=="3":
        update_students()
    elif choice=="4":
        delete_students()
    elif choice=="5":
        display_students()
    elif choice=="6":
        print("thank you")
    else:
        print("invalid choice")
