student_marks = {}
for i in range(5):
    name = input(f"enter the name of student {i + 1} :")
    marks = int(input(f"enter the marks of student {name} :"))
    student_marks[name] = marks


print("student marks : ")
for name, marks in student_marks.items():
    print(f"{name} : {marks}")
while True:
    search_name = input("enter the name to search or 'exit' for end :")
    if search_name.lower() == 'exit':
        break
    else:
        print(f"marks = ", student_marks.get(search_name, "not found"))
