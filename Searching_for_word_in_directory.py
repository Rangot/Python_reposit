import glob
import os

os.chdir('C:\Python prog\lessons')


n1 = input()
            
new_files = []

for files in glob.glob('*.py'):
    f = open( files, 'r' )
    file_contents = f.read()
    if n1 in file_contents:
            new_file = f.name
            print (new_file)
            new_files.append(new_file)
             
    f.close()

n2 = input()    
for files in new_files:
    f = open( files, 'r' )
    file_contents = f.read()
    if n2 in file_contents:
        print (f.name)
    f.close()