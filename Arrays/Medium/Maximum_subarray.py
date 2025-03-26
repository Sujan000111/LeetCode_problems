def MaximumSubarray(a):
  n=len(a)
  max=a[0]
  for i in range(n):
    for j in range(i,n):
      subarray=a[i:j+1]
      if sum(subarray)>max:
        max=sum(subarray)
  print(max)            

def input_format():
  a=list(map(int,input().strip("[]").split(',')))
  MaximumSubarray(a)
input_format()  
