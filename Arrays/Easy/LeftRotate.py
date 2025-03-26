def LeftRotate(a,r):
  n=len(a)
  for i in range(r):
   temp=a[0]
   for i in range(1,n):
     a[i-1]=a[i]
   a[n-1]=temp  
  print(a)
def input_format():
  a=list(map(int,input().strip("[]").split(',')))
  r=int(input("number of rotations"))
  LeftRotate(a,r)
input_format()

def LeftRotate(a):
  temp=a[0]
  n=len(a)
  for i in range(1,n):
    a[i-1]=a[i]
  a[n-1]=temp  
  print(a)
def input_format():
  a=list(map(int,input().strip("[]").split(',')))
  LeftRotate(a)
input_format()
