# symbol = set()
symbol = ['+', '=', '*', '#', '-', '&', '@', '%', '/', '$']
filename = open(r"day3/day3_test_input1.txt", "r")
# for line in filename:
    # for char in line:
    #     if char.isnumeric() == False and char != ".":
    #         symbol.add(char)

matrix = filename.read().split()
for i in range(len(matrix)):
    matrix[i] = list(matrix[i])
print(matrix)


def is_surrounded(r, c): #row, column
    if matrix[r-1][c-1] in symbol:
        return True
    if matrix[r][c-1] in symbol:
        return True
    if matrix[r+1][c-1] in symbol:
        return True
    if matrix[r-1][c] in symbol:
        return True
    if matrix[r+1][c] in symbol:
        return True
    if matrix[r-1][c+1] in symbol:
        return True
    if matrix[r][c+1] in symbol:
        return True
    if matrix[r+1][c+1] in symbol:
        return True
    else:
        return False
#find number
# i = 0
# j = 0
# while i < len(matrix):
#     while j < len(matrix[0]):
#         if matrix[i][j].isnumeric()==True:
#             cur_num = matrix[i][j]
#             while cur_num.isnumeric()==True:
#                 if is_surrounded == 

index = set()
dic = {}
for i in range(len(matrix)):
    j = 0
    while j < len(matrix[0]):
        if matrix[i][j].isnumeric() == True:
            first_index = j
            cur_index = j
            jump = 0
            while cur_index < len(matrix[0]):
                if matrix[i][cur_index].isnumeric() == True:
                    dic[str(i)+str(j)] = {"index": first_index, "long":jump+1}
                    index.add()
                    cur_index += 1
                    jump+=1
                else: 
                    jump+=1
                    break
            j+=jump
        else:
            j+=1

print(dic)
print(index)
