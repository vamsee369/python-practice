value = input("enter something : ")
if value.isdigit():
    print("you entered : ", value)
    print("the data type is integer")
elif value.replace('.', '', 1) and value.count('.') == 1:
    print("you entered ", value)
    print("the data type is float")
else:
    print("you entered ", value)
    print("the data type is string")
