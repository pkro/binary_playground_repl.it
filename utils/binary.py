import re

def byteconvert(num):
  if(type(num) == list):
    num = ''.join([str(s) for s in num])

  if(type(num) == str):
    return int(num,2)

  start = 128
  bits = []
  while start >= 1:
    if num - start >= 0:
      bits.append('1')
      num = num - start  
      
    else:
      bits.append('0')
    start = start // 2
    
  return ''.join(bits)


def binary_op(opStr: str):
  bc = byteconvert
  # for learning's sake arithmetic counterparts to the bitwise logical operators
  ops = {
    "&": lambda a, b: bc([int(bit1) * int(bit2) for bit1, bit2 in zip(a, b)]),
    "|": lambda a, b: bc([int(bit1) + int(bit2) - (int(bit1) * int(bit2)) for bit1, bit2 in zip(a, b)]),
    "^": lambda a, b: a ^ b,
    "<<": lambda a, b: a << b,
    ">>": lambda a, b: a >> b
  }
  op1, operator, op2 = re.findall(r"(\d+)\s+(\D+?)\s+(\d+)", opStr)[0]
  res = bc(ops[operator](op1, op2))
  # i want both print and single returned res, have to get rid of print side effect
  return (res, op1, op2, operator)