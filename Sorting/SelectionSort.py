def SelectionSort(a):
  n=len(a)
  for i in range(n-1):
    min=i
    for j in range(i,n):
      if a[j]<a[min]:
        min=j
    a[min],a[i]=a[i],a[min]
  print(a)      

def input_format():
  a=list(map(int,input().strip("[]").split(",")))
  SelectionSort(a)
input_format()  