def SumOfPrime(num):
  if num==0:
    return False
  for i in range(2,int(num**0.5)+1):
    if num%i==0:
      return False
  return True  

def input_format():
  start=int(input())
  end=int(input())
  sum=0
  for i in range(start,end+1):
    if(SumOfPrime(i)==True):
      sum=sum+i
  print(sum)    
input_format()  