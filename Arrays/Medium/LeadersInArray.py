def LeaderArray(a):
  n=len(a)
  res=[]
  for i in range(n):
    leader=True
    for j in range(i+1,n):
      if a[j]>a[i]:
        leader=False
        break
    if leader==True:
      res.append(a[i])
  return res
def input_format():
  a=list(map(int,input().strip("[]").split(',')))
  print(LeaderArray(a))
input_format()  