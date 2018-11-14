import os, glob

string_to_search=input("Enter the string you want to search : ")
path='nvram2\logs\*.txt'
files=glob.glob(path)
for current_file in files: 
	with open(current_file) as f2:
		for line in f2:
			if string_to_search in line:
				print(current_file) #print file name which contains the string
				print(str(line))    #print the line which contains the string		