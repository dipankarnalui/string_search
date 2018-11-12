from pathlib import Path

string_to_search=input("Enter the string you want to search : ")
file_to_search=Path("dir/nvram2/logs/version.txt") 
with open(file_to_search, "r", encoding='UTF8') as f2:
	for line in f2:
		if string_to_search in line:
			print(str(line))		