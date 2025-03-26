def LargestElement(arr):
  max=0
  for i in arr:
    if i>max:
      max=i
  print(max)    

def input_format():
  arr=list(map(int,input().strip("[]").split(",")))
  LargestElement(arr)
input_format()
#optimal solution
#tc->O(N)

#or
def LargestElement2(arr):
  print(max(arr[:]))
def input_format1():
  arr=list(map(int,input().strip("[]").split(",")))
  LargestElement2(arr)
input_format1()

#or
def LargestElement3(arr):
  arr.sort()
  print(arr[len(arr)-1])
def input_format3():
  arr=list(map(int,input().strip("[]").split(",")))
  LargestElement3(arr)
input_format3()
#brute force method
#O(nlogn)
