def Anagram(s,t):
  return sorted(s)==sorted(t)
s=input()
t=input()
print(Anagram(s,t))
