from pathlib import Path

string_to_search=input("Enter the string you want to search : ")
file_to_search=Path("nvram2/logs/version.txt")
with open(file_to_search, "r", encoding='UTF8') as f2:
	for line in f2:
		if string_to_search in line:
			print(file_to_search) #print file name which contains the string
			print(str(line))    #print the line which contains the string 