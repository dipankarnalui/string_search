import os,tarfile, glob

string_to_search=input("Enter the string you want to search : ")

all_files = [f for f in os.listdir('.') if os.path.isfile(f)] #all_files holds all the files in current directory
for current_file in all_files: 
	if (current_file.endswith(".tgz")) or (current_file.endswith("tar.gz")):
		tar = tarfile.open(current_file, "r:gz")
		file_name=os.path.splitext(current_file)[0] #file_name contains only name by removing the extension
		os.makedirs(file_name) #make directory with the file name
		output_file_path=file_name  #Path to store the files after extraction
		tar.extractall(output_file_path) #extract the current file
		tar.close()
		
		#--------------Following code is to find  the string from all the files in a directory--------
		path1=output_file_path + r'\nvram2\logs'
		all_files=glob.glob(os.path.join(path1,"*"))
		for my_file1 in glob.glob(os.path.join(path1,"*")):
			if os.path.isfile(my_file1): # to discard folders
				with open(my_file1, errors='ignore') as my_file2:
					for line_no, line in enumerate(my_file2):
						if string_to_search in line:
							print(string_to_search + " is found in " + my_file1 + "; Line Number = " + str(line_no))