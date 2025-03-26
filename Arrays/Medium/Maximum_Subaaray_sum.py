
def Maximum_Subarray_sum(a):
  n=len(a)
  max=0
  for i in range(n):
    for j in range(i,n):
      subarray=a[i:j+1]
      if sum(subarray)>max:
        max=sum(subarray)
        max_subarray=subarray      
  print(max)  
  print(max_subarray)    

def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  Maximum_Subarray_sum(a)
input_format()
