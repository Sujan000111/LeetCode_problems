def Prime_number(n):
  count=0
  if n==1:
    print("Neither primr or composite")
  else:
    for i in range(1,n+1):
      if n%i==0:
        count=count+1
    if count==2:
      print("prime number")
    else:
      print("Not a prime number")  



def input_format():
  n=int(input())
  Prime_number(n)

input_format()  


#or
def prime2(n):
  if n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True 
n=int(input()) 
if(prime2(n)):
  print("prime")
else:
  print("not a prime")  