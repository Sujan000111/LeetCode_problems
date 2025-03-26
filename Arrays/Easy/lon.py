def largestSubarray(a,k):
 
  n=len(a)
  max_len=0
  
  for i in range(n):
    for j in range(i,n):
      sub_array=a[i:j+1]
      if sum(sub_array)==k:
        if len(sub_array)>max_len:
          max_len=len(sub_array)
          longest_subarray=sub_array[:]
  print(longest_subarray)        
                
  print(max_len)
def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  k=int(input())
  largestSubarray(a,k) 
input_format()  
