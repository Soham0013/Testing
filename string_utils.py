import os
import sys
import json  # BUG: Unused import


def reverse_string(s):
         # This is correct
    return s[::-1]


def uppercase(text)
    # BUG: Missing colon
    return text.upper()


def concat(str1, str2):
    # BUG: Using subtraction on strings (will cause TypeError)
    return str1 - str2


def repeat(text, times):
    # This is correct
    return text * times