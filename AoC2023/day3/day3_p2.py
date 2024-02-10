def adjacent_number(r, c): #row, column
    adjacent = 0
    #first row
    if r == 0:
        if matrix[r][c-1].isnumeric() == True:
            adjacent += 1
        if matrix[r][c+1].isnumeric() == True:
            adjacent += 1
        if matrix[r+1][c+1].isnumeric() == True:
            adjacent += 1
        if matrix[r+1][c].isnumeric() == True:
            adjacent += 1
        if matrix[r+1][c-1].isnumeric() == True:
            adjacent += 1
        return adjacent
    #last row
    if r == len(matrix)-1:
        if matrix[r-1][c-1].isnumeric() == True:
            adjacent += 1
        if matrix[r][c-1].isnumeric() == True:
            adjacent += 1
        if matrix[r-1][c].isnumeric() == True:
            adjacent += 1
        if matrix[r-1][c+1].isnumeric() == True:
            adjacent += 1
        if matrix[r][c+1].isnumeric() == True:
            adjacent += 1
        return adjacent
        
    #first column
    if c == 0:
        if matrix[r-1][c].isnumeric() == True:
            adjacent += 1
        if matrix[r-1][c+1].isnumeric() == True:
            adjacent += 1
        if matrix[r][c+1].isnumeric() == True:
            adjacent += 1
        if matrix[r+1][c+1].isnumeric() == True:
            adjacent += 1
        if matrix[r+1][c].isnumeric() == True:
            adjacent += 1
        return adjacent
    #last column
    if c == len(matrix[0])-1:
        if matrix[r-1][c-1].isnumeric() == True:
            adjacent += 1
        if matrix[r][c-1].isnumeric() == True:
            adjacent += 1
        if matrix[r-1][c].isnumeric() == True:
            adjacent += 1
        if matrix[r+1][c].isnumeric() == True:
            adjacent += 1
        if matrix[r+1][c-1].isnumeric() == True:
            adjacent += 1
        return adjacent
    #other normal object
    if matrix[r-1][c-1].isnumeric() == True:
        adjacent += 1
    if matrix[r][c-1].isnumeric() == True:
        adjacent += 1
    if matrix[r-1][c].isnumeric() == True:
        adjacent += 1
    if matrix[r-1][c+1].isnumeric() == True:
        adjacent += 1
    if matrix[r][c+1].isnumeric() == True:
        adjacent += 1    
    if matrix[r+1][c+1].isnumeric() == True:
        adjacent += 1
    if matrix[r+1][c].isnumeric() == True:
        adjacent += 1
    if matrix[r+1][c-1].isnumeric() == True:
        adjacent += 1
    return adjacent



def take_number(row, column, long):
    number = "0"
    for num in range(long):
        number+=matrix[row][column+num]
    return int(number[1:])

filename = open(r"day3_test_input2.txt", "r")
matrix = filename.read().split()
for i in range(len(matrix)):
    matrix[i] = list(matrix[i])

#create dictionary
dic = {}
for i in range(len(matrix)):
    j = 0
    while j < len(matrix[0]):
        if matrix[i][j].isnumeric() == True:
            cur_index = j
            jump = 0
            while cur_index < len(matrix[0]):
                if matrix[i][cur_index].isnumeric() == True:
                    dic[str(i)+" "+str(j+jump)] = {"index":str(i)+" "+str(j)}
                    # dic[str(i)+" "+str(j)] = {"long":jump+1}
                    cur_index += 1
                    jump+=1
                else: 
                    jump+=1
                    break
            j+=jump
        else:
            j+=1

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "*":
            print(adjacent_number(i,j))
            if adjacent_number(i,j) == 2:
                print(i, j, "is gear")
print(dic)