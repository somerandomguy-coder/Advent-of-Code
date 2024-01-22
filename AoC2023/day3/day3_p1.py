# symbol = set()
symbol = ['+', '=', '*', '#', '-', '&', '@', '%', '/', '$']
filename = open(r"day3_input.txt", "r")
# for line in filename:
    # for char in line:
    #     if char.isnumeric() == False and char != ".":
    #         symbol.add(char)

matrix = filename.read().split()
for i in range(len(matrix)):
    matrix[i] = list(matrix[i])

def is_surrounded(r, c): #row, column
    #first row
    if r == 0:
        if matrix[r][c-1] in symbol:
            return True
        if matrix[r][c+1] in symbol:
            return True
        if matrix[r+1][c+1] in symbol:
            return True
        if matrix[r+1][c] in symbol:
            return True
        if matrix[r+1][c-1] in symbol:
            return True
        else: 
            return False
    #last row
    if r == len(matrix)-1:
        if matrix[r-1][c-1] in symbol:
            return True
        if matrix[r][c-1] in symbol:
            return True
        if matrix[r-1][c] in symbol:
            return True
        if matrix[r-1][c+1] in symbol:
            return True
        if matrix[r][c+1] in symbol:
            return True
        else:
            return False
    #first column
    if c == 0:
        if matrix[r-1][c] in symbol:
            return True
        if matrix[r-1][c+1] in symbol:
            return True
        if matrix[r][c+1] in symbol:
            return True
        if matrix[r+1][c+1] in symbol:
            return True
        if matrix[r+1][c] in symbol:
            return True
        else: 
            return False
    #last column
    if c == len(matrix[0])-1:
        if matrix[r-1][c-1] in symbol:
            return True
        if matrix[r][c-1] in symbol:
            return True
        if matrix[r-1][c] in symbol:
            return True
        if matrix[r+1][c] in symbol:
            return True
        if matrix[r+1][c-1] in symbol:
            return True
        else: 
            return False
    #other normal object
    if matrix[r-1][c-1] in symbol:
        return True
    if matrix[r][c-1] in symbol:
        return True
    if matrix[r-1][c] in symbol:
        return True
    if matrix[r-1][c+1] in symbol:
        return True
    if matrix[r][c+1] in symbol:
        return True    
    if matrix[r+1][c+1] in symbol:
        return True
    if matrix[r+1][c] in symbol:
        return True
    if matrix[r+1][c-1] in symbol:
        return True
    else:
        return False

def take_number(row, column, long):
    number = "0"
    for num in range(long):
        number+=matrix[row][column+num]
    return int(number[1:])

dic = {}
for i in range(len(matrix)):
    j = 0
    while j < len(matrix[0]):
        if matrix[i][j].isnumeric() == True:
            cur_index = j
            jump = 0
            while cur_index < len(matrix[0]):
                if matrix[i][cur_index].isnumeric() == True:
                    dic[str(i)+" "+str(j)] = {"long":jump+1}
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
        if str(i) + " "+str(j) in dic:
            for k in range(dic[str(i)+" "+str(j)]["long"]):
                if is_surrounded(i, j+k) == True:
                    ans += take_number(i,j,dic[str(i)+" "+str(j)]["long"])
                    del dic[str(i)+" "+str(j)]
                    break
print(ans)