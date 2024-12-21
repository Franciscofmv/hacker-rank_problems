"""
Requirements for solution:

1. Shall read NxM matrix by column the following format:
    - From left to righ
    - From top to bottom

2. Reading the sentences from the matrix shall not use if conditionals


Note: This is the solution for the HackerRank Page - not meant to run
locally
"""

#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

rows = int(first_multiple_input[0])

columns = int(first_multiple_input[1])

matrix = []
# Initalize a list of size <columns>
sentences = [""] * columns

for _ in range(rows):
    matrix_item = input()
    
    # left to right, top to bottom:
    for i in range(columns):
        sentences[i] += matrix_item[i]

    #matrix.append(matrix_item)
f = lambda x: re.sub(r'\b[^a-zA-Z0-9]+\b', ' ', x)
result = f("".join(sentences))
print(result)
