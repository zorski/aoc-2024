from collections import Counter
# Reading input into two lists

frequencies = Counter()
with open("day1-input.txt", "r") as f:
    left_list = []
    right_list = []

    for line in f:
        left, right = line.split()
        left, right = int(left), int(right)
        left_list.append(left)
        right_list.append(right)
        # frequencies for task 2
        frequencies[right] += 1


# Sorting
left_list = sorted(left_list)
right_list = sorted(right_list)

# TASK 1
result1 = 0
for l,r in zip(left_list, right_list):
    result1 += abs(l - r)

print(result1)

# TASK 2
result2 = 0
for i in left_list:
    # freq = get_id_frequency(i, right_list)
    result2 += i * frequencies[i]

print(result2)