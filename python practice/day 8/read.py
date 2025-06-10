content = [
    "Australia is wider than the moon.\n",
    "Venus is the only planet to spin clockwise.\n",
    "Allodoxaphobia is the fear of other people’s opinions.\n",
    "Human teeth are the only part of the body that cannot heal themselves.\n",
    "Competitive art used to be an Olympic sport.\n",
    "American flags left on the moon will eventually get bleached white by the sun.\n"
]

with open("example.txt", "w") as file:
    file.writelines(content)
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
with open("example.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("Total words:", len(words))
