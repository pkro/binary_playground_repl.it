import re

def byteconvert(num):
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

def op(opStr: str):
  b = byteconvert
  color = "\033[1;32;40m"
  ops = {
    "&": lambda a, b: a & b,
    "|": lambda a, b: a | b,
    "^": lambda a, b: a ^ b,
    "<<": lambda a, b: a << b,
    ">>": lambda a, b: a >> b
  }
  op1, operator, op2 = re.findall(r"(\d+)\s+(\D+?)\s+(\d+)", opStr)[0]
  res = b(ops[operator](b(op1), b(op2)))
  print(f'{op1} {operator}\n{op2} = \n{color}{res}')
  return res
  
op('10011100 & 00110100')
