def color_text_with(color, text=""):
  c_normal = "\033[0;0m"
  def color_text(text):
    return f'{color}{text}{c_normal}'
  if text:
    return color_text(text)
  return color_text