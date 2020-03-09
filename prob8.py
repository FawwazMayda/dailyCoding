class Node:
  def __init__(self,d):
    this.left = null
    this.right = null
    this.data = d

def countUnival(root):
  if(root==null):
    return 0
  if (root.left==null and root.right==null):
    return 1
  if(root.left==null and root.data==root.right.data):
    return countUnival(root.right) + 1
  if(root.right==null and root.data==root.left.data):
    return countUnival(root.left) + 1
  count = countUnival(root.left) + countUnival(root.right)
  if(root.left.data==root.data and root.right.data==root.data):
    count+=1
  return count

  a = Node(0)
  b = Node(1)
  c = Node(0)
  d = Node(1)
  e = Node(0)
  f = Node(1)
  g = Node(1)

  d.left = f
  d.right = g

  c.left = d 
  c.right = e 

  a.left = b 
  a.right = c 

  print(countUnival(g))