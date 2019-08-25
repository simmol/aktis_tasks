import bisect
from decimal import Decimal


def calculate_median_from_file(file_name):
    with open(file_name) as input_file:
        number_of_records = int(input_file.readline())

        input_list = []
        for x in range(0, number_of_records):
            next_line = input_file.readline()

            # insert the new element so the list is kept sorted
            # Convert the number to Decimal - Better precision and avoided float rounding errors
            bisect.insort(input_list, Decimal(next_line))

            median = calculate_median(input_list)
            # Output the median to STDOUT.
            print(median.quantize(Decimal('.1')))


def calculate_median(sorted_list):
    """Function that can calculate the median of a list
    Assumes the given list to be sorted
    """
    whole_part, remainder = divmod(len(sorted_list), 2)
    if remainder:
        return sorted_list[whole_part]
    return sum(sorted_list[whole_part - 1:whole_part + 1]) / Decimal(2)
