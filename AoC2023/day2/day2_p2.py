def power_of_fewest_ball(game):
    max_red = 0
    max_blue = 0
    max_green = 0
    ball_sets = game.split("; ")
    for ball_set in ball_sets:
        lst = ball_set.split(", ")
        for i in lst:
            num, color = i.split()
            num = int(num)
            if color == "red" and num > max_red:
                max_red = num
            if color == "green" and num > max_green:
                max_green = num
            if color == "blue" and num > max_blue:
                max_blue = num
    return max_red * max_green * max_blue
    

ans = 0
filename = open(r"day2/day2_input.txt", "r")
for line in filename:
    ids, games = line.split(": ")
    ans += power_of_fewest_ball(games)
print(ans)

