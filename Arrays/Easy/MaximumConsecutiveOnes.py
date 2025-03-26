def MaximumConsectiveOnes(a):
  maxi=0
  count=0
  for i in range(len(a)):
    if a[i]==1:
      count=count+1
      maxi=(max(maxi,count))
    else:
      count=0
  print(maxi)      
    


def input_format():
  a=list(map(int,input().strip("[]").split(',')))
  MaximumConsectiveOnes(a)
input_format()  