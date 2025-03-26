def Missing_number(arr):
  n=len(arr)
  for i in range(1,n+1):
    if i not in arr:
      print(i)
      break

def input_format():
  arr=list(map(int,input().strip('[]').split(",")))
  Missing_number(arr)
input_format()


#or
def Missing_number(arr,n):
  sum1=(n*(n+1))//2
  sum2=sum(i for i in arr)
  print(sum1)
  print(sum2)
  print(sum1-sum2)
  

def input_format():
  arr=list(map(int,input().strip('[]').split(",")))
  n=int(input())
  Missing_number(arr,n)
input_format()

#Optimalsolution
#Uisng Xor
def Missing_number(arr,n):
  xor1=0
  for i in range(1,n+1):
    xor1=xor1^i
  xor2=0
  for i in arr:
    xor2=xor2^i 
  print(xor1^xor2)   


def input_format():
  arr=list(map(int,input().strip('[]').split(",")))
  n=int(input())
  Missing_number(arr,n)
input_format()




