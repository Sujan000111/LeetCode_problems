def SellBuy(a):
  mini=a[0]
  n=len(a)
  profit=0
  for i in range(1,n):
    cost=a[i]-mini
    if cost>profit:
      profit=cost
    mini=min(mini,a[i])
  print(profit)    

def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  SellBuy(a)
input_format()  