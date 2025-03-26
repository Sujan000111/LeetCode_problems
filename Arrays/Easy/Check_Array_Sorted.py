def Check(a):

  for i in range(1,len(a)):
    if a[i]>=a[i-1]:
      pass
    else:
      return False
    return True


def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  if (Check(a)):
    print("sorted")
  else:
    print("not sorted")  
input_format()
