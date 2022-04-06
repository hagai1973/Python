import math
from math import ceil
#to round up use celi

def paint_calc(height, width, coverage):
    return math.ceil((height * width)/coverage)

num = paint_calc(7,13,5)
print (f"Number of cans need to buy: {num}")

