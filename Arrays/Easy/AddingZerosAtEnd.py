def AddingZeroEnd(arr):
  temp=[]
  n=len(arr)
  for i in range(n):
    if arr[i]!=0:
      temp.append(arr[i])
  for i in range(len(temp)):
    arr[i]=temp[i]
  for i in range(len(temp),n):
    arr[i]=0      
  print(arr)

def input_format():
  arr=list(map(int,input().strip("[]").split(',')))
  AddingZeroEnd(arr)
input_format()  

def AddingZeroEnd(arr):
  for i in arr:
    if i==0:
      arr.remove(0)
      arr.append(0)  
  print(arr)

def input_format():
  arr=list(map(int,input().strip("[]").split(',')))
  AddingZeroEnd(arr)
input_format()  

#Optimal solution
def AddingZeroEnd(arr):
 j=-1
 n=len(arr)
 for i in range(n):
   if arr[i]==0:
     j=i
     break
 for i in range(j+1,n):
   if arr[i]!=0:
     arr[i],arr[j]=arr[j],arr[i]
     j=j+1
 print(arr)   

def input_format():
  arr=list(map(int,input().strip("[]").split(',')))
  AddingZeroEnd(arr)
input_format()  