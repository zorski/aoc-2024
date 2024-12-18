import re

with open("day4-input.txt", "r") as f:
    word_search = []
    for line in f:
        word_search.append(list(line.strip()))


count = 0       

# horizontally and vertically
for x in range(len(word_search)):
    for y in range(len(word_search[0])):
        if y <= (len(word_search) - 4):
            xmas_horizontal = "".join(word_search[x][y:y+4])
            if xmas_horizontal == "XMAS" or xmas_horizontal == "SAMX":
                print("horizontal | {},{} -> {},{} ({word})".format(x,y,x,y+3,word=xmas_horizontal))
                count +=1
            
            xmas_vertical = word_search[y][x] + word_search[y+1][x] + word_search[y+2][x] + word_search[y+3][x]
            if xmas_vertical == "XMAS" or xmas_vertical == "SAMX":
                print("vertical | {},{} -> {},{} ({word})".format(y,x,y+3,x,word=xmas_vertical))
                count +=1

# diagonally
for k in range(len(word_search)):
    for x in range(len(word_search)):
        y = x + k
        if y < len(word_search):
            #print("{},{}".format(x,y))
            if y < len(word_search) - 3:
                xmas_diag = word_search[x][y] + word_search[x+1][y+1] + word_search[x+2][y+2] + word_search[x+3][y+3]
                if xmas_diag == "XMAS" or xmas_diag == "SAMX":
                    print("diagonal | {},{} -> {},{}".format(x,y,x+3,y+3))
                    count +=1

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
                count +=1

for k in range(len(word_search)):
    for x in range(len(word_search)):
        if k < len(word_search) - 3:
            x1 = x + k
            if x1 < len(word_search) - 3:
                y = len(word_search) - 1 - x
                xmas_diag = word_search[x1][y] + word_search[x1+1][y-1] + word_search[x1+2][y-2] + word_search[x1+3][y-3]
                if xmas_diag == "XMAS" or xmas_diag == "SAMX":
                    print("diagonal | {},{} -> {},{}".format(x1,y,x1+3,y-3))
                    count +=1

for k in range(1,len(word_search)-1):
    for x in range(len(word_search)):
        if k < len(word_search) - 3:
            y1 = (len(word_search)-1) - x - k
            if y1 >= 0:
                if y1 >= 3:
                    # print("k:{} | {},{} -> {},{}".format(k,x,y1,x+3,y1-3))
                    xmas_diag = word_search[x][y1] + word_search[x+1][y1-1] + word_search[x+2][y1-2] + word_search[x+3][y1-3]
                    if xmas_diag == "XMAS" or xmas_diag == "SAMX":
                        print("diagonal | {},{} -> {},{}".format(k,x,y1,x+3,y1-3))
                        count +=1

print("Total: {}".format(count))


# PART 2
count = 0
for x in range(len(word_search)):
    for y in range(len(word_search[0])):
        if y <= len(word_search) - 3 and x <= len(word_search) - 3:
            x_mas = "".join(word_search[x][y:y+3]) + "".join(word_search[x+1][y:y+3]) + "".join(word_search[x+2][y:y+3])
            if re.match("^M.M.A.S.S$",x_mas):
                print("hit! | {},{} - {})".format(x,y,x_mas))
                count += 1
            if re.match("^S.S.A.M.M$",x_mas):
                print("hit! | {},{} - {})".format(x,y,x_mas))
                count += 1
            if re.match("^M.S.A.M.S$",x_mas):
                print("hit! | {},{} - {})".format(x,y,x_mas))
                count += 1
            if re.match("^S.M.A.S.M$",x_mas):
                print("hit! | {},{} - {})".format(x,y,x_mas))
                count += 1

print("Total: ", count)