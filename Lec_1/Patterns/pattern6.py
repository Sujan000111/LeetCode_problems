"""
1 2 3 4 
1 2 3
1 2
1
"""
n=4
for i in range(0,n+1):
  for j in range(1,n-i+1):
    print(j,end=" ")
  print("")  