"""with open("akhila.txt", "w") as file:
    file.write(" life sucks man \n")
    file.write("welcome")

print("file done")"""

with open("akhila.txt", "r") as file:
    content = file.read()
    print("--- File Contents ---")
    print(content)
    print(file.mode)