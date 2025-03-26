def Majority_element(a):
  n=len(a)
  res=[]
  for i in a:
    if a.count(i)>n//2:
      return i
      break
def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  print(Majority_element(a))
input_format()  