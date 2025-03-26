n=5
for i in range(n+1):
  for j in range(i):
    print("*",end=" ")
  print("")  
for i in range(2,n+1):
  for j in range(n-i+1):
    print("*",end=" ")
  print("")   

#or
for i in range(2*n+1):
  if i==(round(n/2)):
   for j in range(n-i+1):
      print("*",end=" ")
  else:
    for j in range(2*n-1):
      print("*",end=" ")
  print("")         