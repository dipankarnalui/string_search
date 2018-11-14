import os,glob
path1= 'sample1/nvram2/logs' 
all_files=glob.glob(os.path.join(path1,"*"))
for my_file1 in glob.glob(os.path.join(path1,"*")):
	if os.path.isfile(my_file1): # to discard folders
		if '.txt' in my_file1:
			with open(my_file1) as my_file2:
				for line in my_file2:
					if 'BUILD' in line:
						print(my_file1)