def Divisor(n):
  res=[]
  for i in range(1,n+1):
    if n % i==0:
      res.append(i)
  print(*res)    
    
def input_format():
  n=int(input())
  Divisor(n)
input_format()  
