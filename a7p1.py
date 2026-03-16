#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2026 Louis Lam
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
# ---------------------------------------------------------------

"""
Assignment 7 Problem 1
"""

from sys import flags


def antiKasiski(key: str, plaintext: str) -> str:
    """
    Thwart Kasiski examination 
    """
    current = plaintext
    start_index = 0

    while True:
        # Encrypt current plaintext with Vigenere
        ciphertext = ""
        for i in range(len(current)):
            p = ord(current[i]) - ord('A')
            k = ord(key[i % len(key)]) - ord('A')
            c = (p + k) % 26
            ciphertext += chr(c + ord('A'))

        # Find earliest repeated trigram whose first occurrence
        # starts at or after start_index
        repeat_index = -1
        for i in range(start_index, len(ciphertext) - 2):
            trigram = ciphertext[i:i + 3]
            if ciphertext.find(trigram, i + 1) != -1:
                repeat_index = i
                break

        # If none found, we are done
        if repeat_index == -1:
            return ciphertext

        # Insert X immediately after first occurrence of that trigram
        insert_pos = repeat_index + 3
        current = current[:insert_pos] + 'X' + current[insert_pos:]

        # do not later insert for repeated subsequences whose first
        # occurrence starts before this index
        start_index = repeat_index


def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking


# Invoke test() if called via `python3 a7p1.py`
# but not if `python3 -i a7p1.py` or `from a7p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
