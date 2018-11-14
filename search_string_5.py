import os, sys
path= 'sample1/nvram2/logs'
sys.path.append(path)

all_files=os.listdir(path) 
for my_file1 in all_files:
    print(my_file1)
    with open(my_file1, 'r') as my_file2:
        print(my_file2)
        for line in my_file2:
            if 'BUILD' in line:
                print(my_file2)