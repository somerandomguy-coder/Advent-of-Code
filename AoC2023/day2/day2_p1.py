def is_possible(game):
    ball_sets = game.split("; ")
    for ball_set in ball_sets:
        lst = ball_set.split(", ")
        for i in lst:
            num, color = i.split()
            if color == "red" and int(num) > 12:
                return False
            if color == "green" and int(num) > 13:
                return False
            if color == "blue" and int(num) > 14:
                return False
    return True
    

ans = 0

filename = open(r"day2/day2_input.txt", "r")
for line in filename:
    ids, games = line.split(": ")
    if is_possible(games) == True:
        ans += int(ids[5:])
print(ans)


