def TwoSum(a,target):
  n=len(a)
  for i in range(n):
    for j in range(i+1,n):
      if a[i]+a[j]==target:
        print([a[i],a[j]])
        break
def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  target=int(input())
  TwoSum(a,target)
input_format()  