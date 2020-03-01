import math
def segregate(arr):
  j=0
  for i in range(len(arr)):
    if arr[i]<=0:
      arr[i],arr[j] = arr[j],arr[i]
      j+=1
  return j

def findMissingPositiveJ(arr,j):
  print(arr)
  n=len(arr)
  for i in range(j,n):
    v=abs(arr[i])
    pointed = n - v
    if pointed < n-1:
      arr[pointed] = -1*arr[pointed]
  
  for i in range(n):
    if arr[i]>=0:
      return arr[i]+1
  return n
def findMissingPositive(arr):
  j = segregate(arr)
  res = findMissingPositiveJ(arr,j)
  print("#=> {}".format(res))
  return res

assert findMissingPositive([2,2,1])==3
assert findMissingPositive([2,3,4,5,-5,-10,-2,0])==1
assert findMissingPositive([3,4,-1,1])==2