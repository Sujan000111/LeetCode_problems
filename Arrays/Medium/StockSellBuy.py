def StockBuySell(a):
  mini=a[0]
  profit=0
  n=len(a)
  for i in range(1,n):
    cost=a[i]-mini
    if cost>profit:
     profit=cost
     buy_price=mini
     sell_price=a[i]
    mini=min(mini,a[i])
  print(f"Buying at {buy_price} and Selling at {sell_price}")  
  print(profit)  


def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  StockBuySell(a)
input_format()  