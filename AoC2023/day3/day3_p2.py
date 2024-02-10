def adjacent_number_value(r, c):
    #first row
    numlst = []
    if r == 0:
        if matrix[r][c-1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r) +" "+ str(c-1)]["index"]]["value"])
        if matrix[r][c+1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r) +" "+ str(c+1)]["index"]]["value"])
        if matrix[r+1][c+1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r+1) +" "+ str(c+1)]["index"]]["value"])
        if matrix[r+1][c].isnumeric() == True:
            numlst.append(value_dic[dic[str(r+1) +" "+ str(c)]["index"]]["value"])
        if matrix[r+1][c-1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r+1) +" "+ str(c-1)]["index"]]["value"])
        return numlst
    #last row
    if r == len(matrix)-1:
        if matrix[r-1][c-1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r-1) +" "+ str(c-1)]["index"]]["value"])
        if matrix[r][c-1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r) +" "+ str(c-1)]["index"]]["value"])
        if matrix[r-1][c].isnumeric() == True:
            numlst.append(value_dic[dic[str(r-1) +" "+ str(c)]["index"]]["value"])
        if matrix[r-1][c+1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r-1) +" "+ str(c+1)]["index"]]["value"])
        if matrix[r][c+1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r) +" "+ str(c+1)]["index"]]["value"])
        return numlst
    #first column
    if c == 0:
        if matrix[r-1][c].isnumeric() == True:
            numlst.append(value_dic[dic[str(r-1) +" "+ str(c)]["index"]]["value"])
        if matrix[r-1][c+1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r-1) +" "+ str(c+1)]["index"]]["value"])
        if matrix[r][c+1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r) +" "+ str(c+1)]["index"]]["value"])
        if matrix[r+1][c+1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r+1) +" "+ str(c+1)]["index"]]["value"])
        if matrix[r+1][c].isnumeric() == True:
            numlst.append(value_dic[dic[str(r+1) +" "+ str(c)]["index"]]["value"])
        return numlst
    #last column
    if c == len(matrix[0])-1:
        if matrix[r-1][c-1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r-1) +" "+ str(c-1)]["index"]]["value"])
        if matrix[r][c-1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r) +" "+ str(c-1)]["index"]]["value"])
        if matrix[r-1][c].isnumeric() == True:
            numlst.append(value_dic[dic[str(r-1) +" "+ str(c)]["index"]]["value"])
        if matrix[r+1][c].isnumeric() == True:
            numlst.append(value_dic[dic[str(r+1) +" "+ str(c)]["index"]]["value"])
        if matrix[r+1][c-1].isnumeric() == True:
            numlst.append(value_dic[dic[str(r+1) +" "+ str(c-1)]["index"]]["value"])
        return numlst
    #other normal object
    if matrix[r-1][c-1].isnumeric() == True:
        numlst.append(value_dic[dic[str(r-1) +" "+ str(c-1)]["index"]]["value"])
    if matrix[r][c-1].isnumeric() == True:
        numlst.append(value_dic[dic[str(r) +" "+ str(c-1)]["index"]]["value"])
    if matrix[r-1][c].isnumeric() == True:
        numlst.append(value_dic[dic[str(r-1) +" "+ str(c)]["index"]]["value"])
    if matrix[r-1][c+1].isnumeric() == True:
        numlst.append(value_dic[dic[str(r-1) +" "+ str(c+1)]["index"]]["value"])
    if matrix[r][c+1].isnumeric() == True:
        numlst.append(value_dic[dic[str(r) +" "+ str(c+1)]["index"]]["value"])
    if matrix[r+1][c+1].isnumeric() == True:
        numlst.append(value_dic[dic[str(r+1) +" "+ str(c+1)]["index"]]["value"])
    if matrix[r+1][c].isnumeric() == True:
        numlst.append(value_dic[dic[str(r+1) +" "+ str(c)]["index"]]["value"])
    if matrix[r+1][c-1].isnumeric() == True:
        numlst.append(value_dic[dic[str(r+1) +" "+ str(c-1)]["index"]]["value"])
    return numlst

def adjacent_number(r, c): #row, column
    adjacent = 0
    #first row
    if r == 0:
        if matrix[r][c-1].isnumeric() == True:
            if dic[str(r) +" "+ str(c-1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r) +" "+ str(c-1)]["index"])
        if matrix[r][c+1].isnumeric() == True:
            if dic[str(r) +" "+ str(c+1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r) +" "+ str(c+1)]["index"])
        if matrix[r+1][c+1].isnumeric() == True:
            if dic[str(r+1) +" "+ str(c+1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r+1) +" "+ str(c+1)]["index"])
        if matrix[r+1][c].isnumeric() == True:
            if dic[str(r+1) +" "+ str(c)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r+1) +" "+ str(c)]["index"])
        if matrix[r+1][c-1].isnumeric() == True:
            if dic[str(r+1) +" "+ str(c-1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r+1) +" "+ str(c-1)]["index"])
        return adjacent
    #last row
    if r == len(matrix)-1:
        if matrix[r-1][c-1].isnumeric() == True:
            if dic[str(r-1) +" "+ str(c-1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r-1) +" "+ str(c-1)]["index"])
        if matrix[r][c-1].isnumeric() == True:
            if dic[str(r) +" "+ str(c-1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r) +" "+ str(c-1)]["index"])
        if matrix[r-1][c].isnumeric() == True:
            if dic[str(r-1) +" "+ str(c)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r-1) +" "+ str(c)]["index"])
        if matrix[r-1][c+1].isnumeric() == True:
            if dic[str(r-1) +" "+ str(c+1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r-1) +" "+ str(c+1)]["index"])
        if matrix[r][c+1].isnumeric() == True:
            if dic[str(r) +" "+ str(c+1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r) +" "+ str(c+1)]["index"])
        return adjacent
    #first column
    if c == 0:
        if matrix[r-1][c].isnumeric() == True:
            if dic[str(r-1) +" "+ str(c)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r-1) +" "+ str(c)]["index"])
        if matrix[r-1][c+1].isnumeric() == True:
            if dic[str(r-1) +" "+ str(c+1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r-1) +" "+ str(c+1)]["index"])
        if matrix[r][c+1].isnumeric() == True:
            if dic[str(r) +" "+ str(c+1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r) +" "+ str(c+1)]["index"])
        if matrix[r+1][c+1].isnumeric() == True:
            if dic[str(r+1) +" "+ str(c+1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r+1) +" "+ str(c+1)]["index"])
        if matrix[r+1][c].isnumeric() == True:
            if dic[str(r+1) +" "+ str(c)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r+1) +" "+ str(c)]["index"])
        return adjacent
    #last column
    if c == len(matrix[0])-1:
        if matrix[r-1][c-1].isnumeric() == True:
            if dic[str(r-1) +" "+ str(c-1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r-1) +" "+ str(c-1)]["index"])
        if matrix[r][c-1].isnumeric() == True:
            if dic[str(r) +" "+ str(c-1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r) +" "+ str(c-1)]["index"])
        if matrix[r-1][c].isnumeric() == True:
            if dic[str(r-1) +" "+ str(c)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r-1) +" "+ str(c)]["index"])
        if matrix[r+1][c].isnumeric() == True:
            if dic[str(r+1) +" "+ str(c)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r+1) +" "+ str(c)]["index"])
        if matrix[r+1][c-1].isnumeric() == True:
            if dic[str(r+1) +" "+ str(c-1)]["index"] in index_set:
                adjacent += 1
                index_set.remove(dic[str(r+1) +" "+ str(c-1)]["index"])
        return adjacent
    #other normal object
    if matrix[r-1][c-1].isnumeric() == True:
        if dic[str(r-1) +" "+ str(c-1)]["index"] in index_set:
            adjacent += 1
            index_set.remove(dic[str(r-1) +" "+ str(c-1)]["index"])
    if matrix[r][c-1].isnumeric() == True:
        if dic[str(r) +" "+ str(c-1)]["index"] in index_set:
            adjacent += 1
            index_set.remove(dic[str(r) +" "+ str(c-1)]["index"])
    if matrix[r-1][c].isnumeric() == True:
        if dic[str(r-1) +" "+ str(c)]["index"] in index_set:
            adjacent += 1
            index_set.remove(dic[str(r-1) +" "+ str(c)]["index"])
    if matrix[r-1][c+1].isnumeric() == True:
        if dic[str(r-1) +" "+ str(c+1)]["index"] in index_set:
            adjacent += 1
            index_set.remove(dic[str(r-1) +" "+ str(c+1)]["index"])
    if matrix[r][c+1].isnumeric() == True:
        if dic[str(r) +" "+ str(c+1)]["index"] in index_set:
            adjacent += 1
            index_set.remove(dic[str(r) +" "+ str(c+1)]["index"])  
    if matrix[r+1][c+1].isnumeric() == True:
        if dic[str(r+1) +" "+ str(c+1)]["index"] in index_set:
            adjacent += 1
            index_set.remove(dic[str(r+1) +" "+ str(c+1)]["index"])
    if matrix[r+1][c].isnumeric() == True:
        if dic[str(r+1) +" "+ str(c)]["index"] in index_set:
            adjacent += 1
            index_set.remove(dic[str(r+1) +" "+ str(c)]["index"])
    if matrix[r+1][c-1].isnumeric() == True:
        if dic[str(r+1) +" "+ str(c-1)]["index"] in index_set:
            adjacent += 1
            index_set.remove(dic[str(r+1) +" "+ str(c-1)]["index"])
    return adjacent

def take_number(row, column, long):
    number = "0"
    for num in range(long):
        number+=matrix[row][column+num]
    return int(number[1:])

filename = open(r"day3_input.txt", "r")
matrix = filename.read().split()
for i in range(len(matrix)):
    matrix[i] = list(matrix[i])

#create dictionary
dic = {}
value_dic = {}
index_set = set()
for i in range(len(matrix)):
    j = 0
    while j < len(matrix[0]):
        if matrix[i][j].isnumeric() == True:
            cur_index = j
            jump = 0
            while cur_index < len(matrix[0]):
                if matrix[i][cur_index].isnumeric() == True:
                    dic[str(i)+" "+str(j+jump)] = {"index":str(i)+" "+str(j)}
                    value_dic[str(i)+" "+str(j)] = {"value": take_number(i,j,jump+1)}
                    index_set.add(str(i)+" "+str(j))
                    cur_index += 1
                    jump+=1
                else: 
                    jump+=1
                    break
            j+=jump
        else:
            j+=1

ans = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "*":
            adjac = adjacent_number(i,j)
            if adjac == 2:
                print(i, j, "is gear")
                lst = list(set(adjacent_number_value(i,j)))
                print(lst)
                component_ans=lst[0]*lst[-1]
                ans+=component_ans
print(ans)