from utils.display import color_text_with
from utils.binary import byteconvert, binary_op

green = color_text_with("\033[1;32;40m")

def op(opStr):
  res, op1, op2, operator = binary_op(opStr)
  print(f'{op1} {green(operator)}\n{op2} = \n{green(res)}')
  return res


#op('10011100 | 00110100')
#op('10011100 & 00110100')
op(f"{op('10011100 | 00110100')}&{op('10011100 & 00110100')}")
