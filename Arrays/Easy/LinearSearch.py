def Linearsearch(arr,num):
  n=len(arr)
  for i in range(n):
    if arr[i]==num:
      print(i)
      break

def input_format():
  arr=list(map(int,input().strip("[]").split(",")))
  num=int(input())
  Linearsearch(arr,num)
input_format()  