def color_text_with(color, text=""):
  c_normal = "\033[0;0m"
  def color_text(text):
    # for inmmutable variables () from the outer scope that we
    # want to modify (like a counter variable), we would have 
    # to define them as nonlocal here in the inner function scope
    return f'{color}{text}{c_normal}'
  if text:
    return color_text(text)
  return color_text