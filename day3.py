import re

with open("day3-input.txt", "r") as file:
    programs_memory = file.read()

# PART 1

mul_operations = re.findall(r"mul\((\d+),(\d+)\)", programs_memory)

result = 0
for mul_operation in mul_operations:
    result += int(mul_operation[0]) * int(mul_operation[1])


print(result)


# PART 2
mul_operations = re.subn(r"don't\(\).*?do\(\)", "_" ,programs_memory, flags=re.DOTALL)
mul_operations = re.findall(r"mul\((\d+),(\d+)\)", mul_operations[0])

result = 0
for mul_operation in mul_operations:
    result += int(mul_operation[0]) * int(mul_operation[1])

print(result)