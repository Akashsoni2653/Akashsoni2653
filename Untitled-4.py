
def largest(list):
    largest_number = list[0]
    for numbers in list:
        if numbers > largest_number:
            largest_number = numbers
    return largest_number


def smallest(list):
    smallest_number = list[0]
    for numbers in list:
        if numbers < smallest_number:
            smallest_number = numbers
    return smallest_number