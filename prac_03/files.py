# 1.
out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi, {name}!")
in_file.close()

# 3.
with open("numbers.txt", "r") as in_file:
    line_1 = int(in_file.readline().strip())
    line_2 = int(in_file.readline().strip())
print(line_1 + line_2)


#4
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line.strip())
        total += number
print(total)