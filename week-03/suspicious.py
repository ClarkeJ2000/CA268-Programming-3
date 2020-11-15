import sys
file_1 = open(sys.argv[1],'r')
file_2 = open(sys.argv[2],'r')
set1 = set()
set2 = set()
   
for line in file_1:
   set1.add(line.strip())
for line in file_2:
   set2.add(line.strip())
  
baddies = set1.intersection(set2)
baddies = sorted(list(baddies))
i = 0
  
while i < len(baddies):
   print('{}. {}'.format((i+1),baddies[i]))
   i += 1
