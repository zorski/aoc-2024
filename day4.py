with open("day4-input.txt", "r") as f:
    word_search = []
    for line in f:
        word_search.append(list(line.strip()))

# horizontally and vertically
for x in range(len(word_search)):
    for y in range(len(word_search[0])):
        if y <= (len(word_search) - 4):
            xmas_horizontal = "".join(word_search[x][y:y+4])
            if xmas_horizontal == "XMAS" or xmas_horizontal == "SAMX":
                print("horizontal | {},{} -> {},{} ({word})".format(x,y,x,y+3,word=xmas_horizontal))
            
            xmas_vertical = word_search[y][x] + word_search[y+1][x] + word_search[y+2][x] + word_search[y+3][x]
            if xmas_vertical == "XMAS" or xmas_vertical == "SAMX":
                print("vertical | {},{} -> {},{} ({word})".format(y,x,y+3,x,word=xmas_vertical))
print("--")

# diagonally \\
print("diagonally \\ #1")
for k in range(len(word_search)):
    for x in range(len(word_search)):
        y = x + k
        if y < len(word_search):
            #print("{},{}".format(x,y))
            if y < len(word_search) - 3:
                xmas_diag = word_search[x][y] + word_search[x+1][y+1] + word_search[x+2][y+2] + word_search[x+3][y+3]
                if xmas_diag == "XMAS" or xmas_diag == "SAMX":
                    print("diagonal | {},{} -> {},{}".format(x,y,x+3,y+3))
print("--")

print('diagonally \\ #2')
for k in range(1,len(word_search)):
    for x in range(len(word_search)):
        if k > len(word_search) - 4:
            break
        x1 = x + k
        y1 = x1 - k
        if x1 < len(word_search) - 3:
            # print("{},{} -> {},{}".format(x1,y1,x1+3,y1+3))
            xmas_diag = word_search[x1][y1] + word_search[x1+1][y1+1] + word_search[x1+2][y1+2] + word_search[x1+3][y1+3]
            if xmas_diag == "XMAS" or xmas_diag == "SAMX":
                print("diagonal | {},{} -> {},{}".format(x1,y1,x1+3,y1+3))
print("--")

# diagonally //
print("diagonally // #1")
for k in range(len(word_search)):
    for x in range(len(word_search)):
        if k < len(word_search) - 3:
            x1 = x + k
            if x1 < len(word_search) - 3:
                y = len(word_search) - 1 - x
                xmas_diag = word_search[x1][y] + word_search[x1+1][y-1] + word_search[x1+2][y-2] + word_search[x1+3][y-3]
                if xmas_diag == "XMAS" or xmas_diag == "SAMX":
                    print("diagonal | {},{} -> {},{}".format(x1,y,x1+3,y-3))
print("--")

print("diagonally // #2")
for k in range(1,len(word_search)-1):
    for x in range(len(word_search)):
        y1 = len(word_search) - x - k - 1
        if y1 >= 0:
            #print("{},{}".format(x,y1))
            pass