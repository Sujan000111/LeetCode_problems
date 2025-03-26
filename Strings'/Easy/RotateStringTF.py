def rotateString(s,goal):
  return len(s)==len(goal) and goal in (s+s)
s=input()
goal=input()
print(rotateString(s,goal))