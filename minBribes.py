#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    
    for i, v in enumerate(q):
        if v - (i+1) > 2:
            print("Too chaotic")
            return
            
    for i in range(len(q)):
        start = max(0, q[i] - 2)
        for j in range(start,i):
            if q[j] > q[i]:
                bribes +=1
    print(bribes)
    

def minimumBribes2(q):
    swaps = 0
    min_val = len(q)

    for i in range(len(q) - 1, -1, -1):

        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return

        if q[i] > i + 1:
            swaps += q[i] - (i + 1)

        else:
            if min_val > q[i]:
                min_val = q[i]
            elif q[i] != min_val:
                swaps += 1

    print(swaps)

def run_tests():
    tests = [
        ([2, 1, 5, 3, 4], 3),
        ([2, 5, 1, 3, 4], "Too chaotic"),
        ([1, 2, 3, 4, 5], 0),
        ([1, 2, 5, 3, 7, 8, 6, 4], 7),
        ([3, 1, 2], 2),
        ([1, 3, 2], 1),
        ([4, 1, 2, 3], "Too chaotic"),
        ([1, 2, 3, 5, 4], 1),
        ([3, 2, 1], 3),
        ([1, 4, 3, 2], 3)
    ]

    print("\nRunning full test suite:\n")

    for q, expected in tests:
        print(f"Test: {q}")
        print("Expected:", expected)
        print("Output:  ", end="")

        # Capture printed output
        from io import StringIO
        import sys

        backup = sys.stdout
        sys.stdout = StringIO()

        minimumBribes2(q)

        result = sys.stdout.getvalue().strip()
        sys.stdout = backup

        print(result)

        if result == str(expected):
            print("✔ PASS\n")
        else:
            print("❌ FAIL\n")


run_tests()
