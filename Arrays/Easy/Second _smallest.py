def second_smallest(a):
  smallest=a[0]
  s_smallest=-1
  n=len(a) 
  for i in range(1,n-1):
    if a[i]<smallest:
      s_smallest=smallest
      smallest=a[i]
    elif a[i]>smallest and a[i]<s_smallest:
      s_smallest=a[i]  
  print(s_smallest)    


def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  second_smallest(a)
input_format()
