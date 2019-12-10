#!/usr/bin/env python3
import sys
from os import path
from BoyerMoore import string_search
from typing import *


def process(filename: str, pattern: str) -> list:
    f = open(filename)
    line = 0

    result = []

    while True:
        code = f.readline().strip('\n').lstrip('>')
        sequence = f.readline().strip('\n')
        line += 2

        if not code or not sequence:
            break

        search_result = string_search(pattern, sequence)
        if len(search_result) > 0:
            result.append([line, code])

    return result


def print_results(results: list):
    if not results:
        return

    for result in results:
        print("Line: " + str(result[0]) + ", Code: " + result[1])


def main():
    if len(sys.argv) < 2:
        print("Usage: ./Search.py <file name> <pattern>")
        return

    filename = sys.argv[1]
    pattern = sys.argv[2]

    if not path.exists(filename):
        print("File does not exist")
        return

    result = process(filename, pattern)
    print_results(result)


if __name__ == "__main__":
    main()
