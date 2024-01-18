# Read file
filename = open(r"day1/day1_input.txt", "r")
ans = 0
for line in filename:
    n = len(line)

# part 1

#     for i in range(n):
#         if line[i].isnumeric() == True:
#             first = line[i]
#             break
#     for i in range(n-1, -1, -1):
#         if line[i].isnumeric() == True:
#             last = line[i]
#             break
#     plus = int(first + last)
#     ans += plus
# print(ans)

# Second way (a bit slower but less code)
    num = []
    for char in line:
        if char.isnumeric() == True:
            num.append(char)
    ans += int(num[0]+num[-1])
print(ans)