def find_sum_max(arr):

  include = 0
  exclude = 0
  for v in arr:
    new_exclude = max(include,exclude)
    include = exclude + v
    exclude = new_exclude
  
  return max(include,exclude)

print(find_sum_max([2,4,6,2,5]))
print(find_sum_max([5,1,1,5]))