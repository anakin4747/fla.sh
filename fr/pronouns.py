#!/usr/bin/python3

import sys

count = 0
consecutive_lines = ""

subject_pronouns = {
    1: "je/j'",
    2: "tu/t'",
    3: "il/elle/on",
    4: "nous",
    5: "vous",
    6: "ils/elles",
}

imperatif_pronouns = {
    1: "tu/t'",
    2: "nous",
    3: "vous",
}

pronouns = {}

while input := sys.stdin.readline():
    if not input.strip():
        # print("Empty")

        if count == 3:
            pronouns = imperatif_pronouns

        if count == 6:
            pronouns = subject_pronouns

        for idx, line in enumerate(consecutive_lines.splitlines()):
            print(pronouns[idx + 1], line)

        count = 0
        consecutive_lines = ""
        print("")
    else:
        count += 1
        consecutive_lines += input
