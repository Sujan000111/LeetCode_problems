def AppearingOnce(a):
  for i in a:
    if a.count(i)==1:
      print(i)

def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  AppearingOnce(a)
input_format()  