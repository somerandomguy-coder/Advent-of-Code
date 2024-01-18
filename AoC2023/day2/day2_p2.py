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
    