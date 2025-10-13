NAME_FILENAME = "name.txt"
NUMBER_FILENAME = "numbers.txt"

# 1.
out_file = open(NAME_FILENAME, "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open(NAME_FILENAME, "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi, {name}!")

# 3.
total = 0
with open(NUMBER_FILENAME, "r") as in_file:
    for line in range(0, 2):
        number = in_file.readline()
        total += int(number)
    print(total)



# 4
total_number = 0
with open(NUMBER_FILENAME, "r") as in_file:
    for line in in_file:
        number = int(line)
        total_number += number
print(total_number)
