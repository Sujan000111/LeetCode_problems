from collections import Counter,defaultdict
def SortCharacter(s):
  count=Counter(s)
  buckets=defaultdict(list)
  for char,cnt in count.items():
    buckets[cnt].append(char)
  res=""
  for i in range(len(s),0,-1):
    for c in buckets[i]:
      res=res+c*i
  return res
s=input()
print(SortCharacter(s))      

