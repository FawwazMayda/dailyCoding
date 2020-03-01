def prodSelf(arr):
  t1 = [1]
  t2 = [1]
  #T1 from right  
  for i in range(1,len(arr)):
    t1.append(t1[i-1]*arr[i-1])
  #T2 from left
  for i in range(len(arr)-2,-1,-1):
    #print(i)
    v = t2[0]*arr[i+1]
    t2.insert(0,v)
  res = []
  for i in range(len(arr)):
    res.append(t1[i] * t2[i])
  return res

assert prodSelf([1,2,3,4])==[24,12,8,6]