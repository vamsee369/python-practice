file = open("line.txt", "w")
file.write("Hello, Python!\n")
file.close()

line = ["Python is fun\n", "Let's master file handling!\n"]
with open("line.txt", "w") as file:
    file.writelines(line)


new_line = "this is appended line. /n"
with open("line.txt", "a") as file:
    file.write(new_line)

with open("user_input.txt", "w") as file:
    while True:
        line = input("Enter something (or type 'stop' to finish): ")
        if line.lower() == "stop":
            break
        file.write(line + "\n")
