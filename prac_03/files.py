NAMAE_FILENAME = "name.txt"
NUMBER_FILENAME = "numbers.txt"

# 1.
out_file = open(NAMAE_FILENAME, "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open(NAMAE_FILENAME, "r")
name = in_file.read().strip()
print(f"Hi, {name}!")
in_file.close()

# 3.
with open(NUMBER_FILENAME, "r") as in_file:
    line_1 = int(in_file.readline().strip())
    line_2 = int(in_file.readline().strip())
print(line_1 + line_2)

# 4
total_number = 0
with open(NUMBER_FILENAME, "r") as in_file:
    for line in in_file:
        number = int(line.strip())
        total_number += number
print(total_number)
