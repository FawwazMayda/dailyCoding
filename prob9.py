def find_sum_max(arr):
  # Max sum including current element
  include = 0
  # Max sum excluding current element
  exclude = 0
  for v in arr:
    new_exclude = max(include,exclude)
    include = exclude + v
    exclude = new_exclude
  
  return max(include,exclude)

print(find_sum_max([2,4,6,2,5]))
print(find_sum_max([5,1,1,5]))