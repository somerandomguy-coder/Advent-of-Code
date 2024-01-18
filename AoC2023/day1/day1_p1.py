# Read file
inputfile = open(r"C:\Users\Nam Le\Documents\Coding\AoC2023\day1_input.txt", "r")
ans = 0
for line in inputfile:
    n = len(line)

# part 1
    num = []
    for i in range(n):
        if line[i].isnumeric() == True:
            first = line[i]
            break
    for i in range(n-1, -1, -1):
        if line[i].isnumeric() == True:
            last = line[i]
            break
    plus = int(first + last)
    ans += plus
print(ans)


