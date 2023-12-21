import hashlib


# This function counts the number of 0 in the string made by the has generator
def zero_checker(test, goal):
    count = 0
    for char in test:
        if char == "0":
            count += 1
            if count == goal:
                return True
        else:
            return False


# This function uses the hashlib library to generate a md5 hash from the input
def md5_generator(test_input, goal):
    result = hashlib.md5(test_input.encode("utf-8")).hexdigest()
    if zero_checker(result, goal):
        return True


# The puzzle input.
puzzle_input = "ckczppom"
count = 0


# Part 1 done with a while loop
while True:
    test_input = puzzle_input + str(count)
    if md5_generator(test_input, 5):
        print(count)
        break
    count += 1


# Part 2 with a for loop, just for extra flavor
for i in range(10, 100_000_000):
    new_input = puzzle_input + str(i)
    if md5_generator(new_input, 6):
        print(i)
        break
