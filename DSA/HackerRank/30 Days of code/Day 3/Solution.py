#!/bin/python3

import math
import os
import random
import re
import sys


def check_number_weird(num):
    if num % 2 == 0 and (num > 20 or num < 6):
        return "Not Weird"
    else:
        return "Weird"


if __name__ == '__main__':
    N = int(input().strip())
    result = check_number_weird(N)
    print(result)
