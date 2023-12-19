# Open the file and turn it into a list of integers
with open("day2.txt", "r") as data:
    dimensions = [list(map(int, x.strip("\n").split("x"))) for x in data]


# Part 1: Calculating wrapping paper
def paper_calc(l, w, h):
    first, second, third = (l * w),  ( w * h), (h * l)
    subtotal = (first * 2) + (second * 2) + (third * 2)
    return subtotal + min(first, second, third)


# Part 2: Calculation ribbon; sorting works, a better solution should be found
def ribbon_calculator(dim_list):
    dim_list.sort()
    return ((dim_list[0]) * 2) + ((dim_list[1]) * 2) + (dim_list[0] * dim_list[1] * dim_list[2])


# Calculate the values and print them
paper_total = sum([paper_calc(thing[0], thing[1], thing[2]) for thing in dimensions])
ribbon_total = sum([ribbon_calculator(thing) for thing in dimensions])
