# Python Longest Palindromic Substring

## Overview

This program finds the longest substring of a given string
that is a palindrome.

A palindrome is a string that reads the same forwards and
backwards.

## Example

Input:

malayalam

Output:

malayalam

## How It Works

The program:

1. Generates different substrings using nested loops.
2. Reverses each substring using the `rev01()` function.
3. Checks whether the substring is a palindrome.
4. Compares the lengths of palindromic substrings.
5. Stores the longest palindrome found.

## Concepts Covered

- Strings
- String slicing and indexing
- Functions
- Nested loops
- String reversal
- Palindrome checking
- Substrings

## Complexity

### Time Complexity

O(n³)

### Space Complexity

O(n)

## Repository Structure

```text
Python-Longest-Palindromic-Substring/
│
├── LongestPalindromicSubstring.py
└── README.md
