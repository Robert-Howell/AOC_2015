with open("day1.txt", "r") as data:
    directions = data.read()

# A hash holding the values for each character.
move_dict = {"(": 1, ")": -1}


# Part 1, we iterate through the string and find the final floor
def floor_calculator(direction_string):
    current_floor = 0
    for index, char in enumerate(direction_string):
        current_floor += move_dict[char]
    return current_floor


# Part 2, iterate and return the index + 1 when we get to floor -1
def negative_calculator(direction_string):
    current_floor = 0
    for index, char in enumerate(direction_string):
        current_floor += move_dict[char]
        if current_floor == -1:
            return index + 1


# Do the calculations and print the answers
print(floor_calculator(directions), negative_calculator(directions))
