# Read file
filename = open(r"day1/day1_input.txt", "r")
ans = 0
for line in filename:
    n = len(line)

# part 2
    for i in range(n):
        if line[i].isnumeric() == True:
            first = line[i]
            break
        if n-i>=5:
            if line[i]+line[i+1]+line[i+2]+line[i+3]+line[i+4] == "three":
                first = "3"
                break
            elif line[i]+line[i+1]+line[i+2]+line[i+3]+line[i+4] == "seven":
                first = "7"
                break
            elif line[i]+line[i+1]+line[i+2]+line[i+3]+line[i+4] == "eight":
                first = "8"
                break
        if n-i>=4:
            if line[i]+line[i+1]+line[i+2]+line[i+3] == "four":
                first = "4"
                break
            elif line[i]+line[i+1]+line[i+2]+line[i+3] == "five":
                first = "5"
                break
            elif line[i]+line[i+1]+line[i+2]+line[i+3] == "nine":
                first = "9"
                break
        if n-i>=3:
            if line[i]+line[i+1]+line[i+2] == "one":
                first = "1"
                break
            elif line[i]+line[i+1]+line[i+2] == "two":
                first = "2"
                break
            elif line[i]+line[i+1]+line[i+2] == "six":
                first = "6"
                break
    for i in range(n-1,-1,-1):
        if line[i].isnumeric() == True:
            last = line[i]
            break
        if i>=4:
            if line[i]+line[i-1]+line[i-2]+line[i-3]+line[i-4] == "eerht":
                last = "3"
                break
            elif line[i]+line[i-1]+line[i-2]+line[i-3]+line[i-4] == "neves":
                last = "7"
                break
            elif line[i]+line[i-1]+line[i-2]+line[i-3]+line[i-4] == "thgie":
                last = "8"
                break
        if i>=3:
            if line[i]+line[i-1]+line[i-2]+line[i-3] == "ruof":
                last = "4"
                break
            elif line[i]+line[i-1]+line[i-2]+line[i-3] == "evif":
                last = "5"
                break
            elif line[i]+line[i-1]+line[i-2]+line[i-3] == "enin":
                last = "9"
                break
        if i>=2:
            if line[i]+line[i-1]+line[i-2] == "eno":
                last = "1"
                break
            elif line[i]+line[i-1]+line[i-2] == "owt":
                last = "2"
                break
            elif line[i]+line[i-1]+line[i-2] == "xis":
                last = "6"
                break
    ans += int(first+last)
print(ans)

        
