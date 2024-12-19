import math


rules = {}
updates = []

with open("day5-input-sample.txt", mode="r") as f:
    while True:
        line = f.readline()
        if line == "\n":
            break

        k,v = line.split("|")
        key, value = int(k), int(v)
        if key in rules:
            rules[key].append(value)
        else:
            rules[key] = [value]
    
    while line := f.readline():
        update = [int(i) for i in line.split(",")]
        updates.append(update)

# PART1

result = 0
incorrect_update_flag = False
incorrect_updates = []

for update in updates:
    for idx, update_no in enumerate(reversed(update)):
        if incorrect_update_flag:
            break
        for idy, update_no2 in enumerate(reversed(update[:-(1+idx)])):
            # print("compare {} to {}".format(update_no,update_no2))
            if update_no2 in rules.get(update_no,[]):
                print("update {}: {}|{} violated!".format(str(update),update_no, update_no2))
                incorrect_updates.append(update)
                incorrect_update_flag = True
                break
    if not incorrect_update_flag:
        print("update {}: no volations!".format(str(update)))
        idz = math.ceil(len(update)/2) - 1
        result += update[idz]
    incorrect_update_flag = False

print("Result: ", result)


# PART 2
# topological sort todo
print(incorrect_updates)

