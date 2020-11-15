import sys

file1 = open(sys.argv[1], "r")
file2 = open(sys.argv[2], "r")
set1 = set()
set2 = set()
for line in file1:
	set1.append(line.strip())
for line in file2:
	set2.append(line.strip())

