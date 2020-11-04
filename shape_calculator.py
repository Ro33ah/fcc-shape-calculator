class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = 2*self.width + 2*self.height
    return perimeter

  def get_diagonal(self):
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return f'Too big for picture.'

    width_line = ""
    for height in range(self.height):
      width_line += "*" * self.width
      if height < self.height:
        width_line += "\n"
    return width_line

  def get_amount_inside(self, shape):
    main_area = self.get_area()
    shape_area = shape.get_area()
    result = main_area//shape_area
    return result

  def __str__(self):
    if type(self) == Rectangle:
      obj_instance = f'Rectangle(width={self.width}, height={self.height})'
    if type(self) == Square:
        obj_instance = f'Square(side={self.width})'

    return obj_instance

class Square(Rectangle):
  def __init__(self, side_length):
    self.width = side_length
    self.height = side_length
  
  def set_side(self, side):
    self.width = side
    self.height = side

  def trach_changes(self):
    print(f'this is just a dummy method {self.width}')

