from pathlib import Path

# absolute path:
# c:\Program Files\Microsoft
# Relative path:
# /user/local/bin
path = Path("emails")
print(path.exists())
# print(path.mkdir())  # make directory
# print(path.rmdir())
path1 = Path()  # capital P because its a class
for file in path1.glob('*.*'):
    print(file)# search for files in the directory of the curernt path
# from glob we can define a certain search pattern "*" means search through everything all files all directories
# "*.*" get all the files in the directory but not all the direcotries
# "*.py " or "*.xls" any type of file


