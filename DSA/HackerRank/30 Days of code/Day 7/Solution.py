#!/bin/python3

import math
import os
import random
import re
import sys


def print_arr_numbers(arr):
    line = ""
    for i in range(len(arr)-1, -1, -1):
        line += f"{arr[i]} "

    print(line.rstrip())


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    print_arr_numbers(arr)
