def RightRotate(a,r):
  n=len(a)
  for i in range(r):
   temp=a[n-1]
   for i in range(n-1,0,-1):
     a[i]=a[i-1]
   a[0]=temp  
  print(a)
def input_format():
  a=list(map(int,input().strip("[]").split(',')))
  r=int(input("number of rotations"))
  RightRotate(a,r)
input_format()



