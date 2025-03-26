def second_largest(arr):
  arr=set(arr)
  arr=list(arr)
  s=max(arr[:])
  max1=0
  arr.remove(s)
  for i in arr:
    if i>max1:
      max1=i
  print(max1)    
def input_format():
  arr=list(map(int,input().strip("[]").split(",")))
  second_largest(arr)
input_format()  

#or
def second_largest(arr):
  arr=set(arr)
  arr=list(arr)
  s=max(arr[:])
  max1=0
  arr.remove(s)
  print(max(arr[:]))   
def input_format():
  arr=list(map(int,input().strip("[]").split(",")))
  second_largest(arr)
input_format()  

#or
#Bruteforce
def second_largest(arr):
  arr.sort()
  n=len(arr)
  largest=arr[n-1] 
  for i in reversed(range(n-1)):
    if arr[i]!=largest:
      second_largest=arr[i]
      break
  print(second_largest)  
def input_format():
  arr=list(map(int,input().strip("[]").split(",")))
  second_largest(arr)
input_format()  

#Time Complexity:O(N)


#Better solution
def second_largest(arr):
  max=0
  s_largest=-1
  for i in arr:
    if i>max:
      max=i
  for i in range(0,len(arr)-1):
    if(arr[i]>s_largest) and arr[i]!=max:
      s_largest=arr[i]
  print(s_largest)     
def input_format():
  arr=list(map(int,input().strip("[]").split(",")))
  second_largest(arr)
input_format()  
#O(N+N)=O(2n)

#Optimal Solution
def second_largest(a):
  n=len(a)
  largest=a[0]
  slargest=-1
  for i in range(1,n-1):
    if(a[i]>largest):
      slargest=largest
      largest=a[i]
    elif  a[i]<largest and a[i]>slargest:
      slargest=a[i]  
  print(slargest)    

def input_format():
  arr=list(map(int,input().strip("[]").split(",")))
  second_largest(arr)
input_format()  


