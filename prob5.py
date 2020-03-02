def cons(a,b):
  def pair(f):
    return f(a,b)
  return pair


#return first elem
def car(p):
  def first(a,b):
    return a
  return p(first)

#return second elem
def cdr(p):
  def second(a,b):
    return b
  return p(second)


"""
car(cons(3,4))==3
cdr(cons(3,4))==4
"""
assert car(cons(3,4))==3
assert cdr(cons(3,4))==4
assert car(cons(4,5))!=5
assert cdr(cons(4,5))!=4