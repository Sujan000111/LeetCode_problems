def HCF(n,m):
  gcd=1
  for i in range(1,min(n,m)):
    if n%i==0 and m%i==0:
      gcd=i
  print(gcd)  
          

def input_format():
  n=int(input())
  m=int(input())
  HCF(n,m)
input_format()  