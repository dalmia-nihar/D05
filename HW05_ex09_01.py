#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

import re 

# Body
def read_file():
	file_name = input("Please enter the file name with extention: ")
	data = open(file_name, "r")
	for line in data:
		if len(line.strip()) > 20:
			print (line, end = "")



##############################################################################
def main():
    read_file()  # Call your functions here.

if __name__ == '__main__':
    main()
