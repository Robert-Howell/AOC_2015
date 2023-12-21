with open("day3.txt", "r") as data:
    move_string = data.read()

move_dict = {"^": [-1, 0], "v": [1, 0], "<": [0, -1], ">": [0, 1]}


# Part 1: Santa following the drunk elf's directions
def santa_directions(directions):
    current = [0, 0]
    house_set = {(0, 0)}
    for char in directions:
        move = move_dict[char]
        for i in range(2):
            current[i] += move[i]
        current_tup = tuple(current)
        if current_tup not in house_set:
            house_set.add(current_tup)
    return len(house_set)


# Part 2: Santa has a robot helper
def santa_robot_directions(directions):
    santa_current = [0, 0]
    robot_current = [0, 0]
    house_set = {(0, 0)}
    count = 0
    for char in directions:
        move = move_dict[char]
        if count % 2 == 0:
            for i in range(2):
                santa_current[i] += move[i]
            current_tup = tuple(santa_current)
        else:
            for i in range(2):
                robot_current[i] += move[i]
            current_tup = tuple(robot_current)

        if current_tup not in house_set:
            house_set.add(current_tup)

        count += 1

    return len(house_set)


house_count = santa_directions(move_string)
second_house_count = santa_robot_directions(move_string)
