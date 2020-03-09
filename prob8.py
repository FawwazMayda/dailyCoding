class Node:
  def __init__(self,d):
    self.left = None
    self.right = None
    self.data = d
  def __repr__(self):
    return str(self.data)

def countUnival(root):
  if(root==None):
    return 0
  if (root.left==None and root.right==None):
    return 1
  if(root.left==None and root.data==root.right.data):
    return countUnival(root.right) + 1
  if(root.right==None and root.data==root.left.data):
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
print(countUnival(a))