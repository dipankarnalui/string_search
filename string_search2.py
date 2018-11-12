import os,tarfile, glob
from pathlib import Path

string1=input("Enter the string you want to search : ")
all_files = [f for f in os.listdir('.') if os.path.isfile(f)] #all_files holds all the files in current directory
for current_file in all_files: 
	print("Reading " + current_file)
	if (current_file.endswith(".tgz")) or (current_file.endswith("tar.gz")):
		tar = tarfile.open(current_file, "r:gz")
		file_name=os.path.splitext(current_file)[0] #file_name contains only name by removing the extension
		os.makedirs(file_name) #make directory with the file name
		output_file_path=file_name  #Path to store the files after extraction
		tar.extractall(output_file_path) #extract the current file
		tar.close()
		log_file_path=Path(output_file_path + "/nvram2/logs/")
		file_to_open=log_file_path/"version.txt"
		f1 = open(file_to_open, "r", encoding='UTF8')
		content=f1.read()
		print("----------------------")
		print(content)
		print("----------------------")