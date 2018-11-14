import os,tarfile, glob

string_to_search=input("Enter the string you want to search : ")

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
		#--------------Following code is to find  the string from all the files in a directory--------
		path=output_file_path + '/nvram2/logs'	
		files=os.listdir(path)
		for file1 in files:
			if '.txt' in file1:
				with open(file1) as f2:
					for line in f2:
						if string_to_search in line:
							#print file name which contains the string
							print(file1)
							#print the line which contains the string
							print(str(line))