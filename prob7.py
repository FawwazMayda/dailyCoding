def decode(s):
  if len(s)<=1:
    return 1
  elif len(s)==2:
    if s[0]=='0':
      return 1
    val = int(s)
    if val <= 25:
      return 2
    else:
      return 1
  elif len(s)>2:
    if s[0]=='0':
      return decode(s[1:])
    val = int(s[0:2])
    if val<=25:
      #print(s[1:])
      #print(s[2:])
      return decode(s[1:]) + decode(s[2:])
    else:
      return decode(s[2:])

#print(decode('111'))
def decode2(s):
  if len(s)<=1:
    return 1
  elif len(s)==2:
    val = int(s)
    if val <=26:
      return 2 
    else:
      return 1
  else:
    val = int(s[0:2])
    if val <= 26 :
      return decode2(s[1:]) + decode2(s[2:])
    else:
      return decode2(s[1:])

assert decode2('81') == 1
assert decode2('11') == 2
assert decode2('111') == 3
assert decode2('1111') == 5
assert decode2('1311') == 4
