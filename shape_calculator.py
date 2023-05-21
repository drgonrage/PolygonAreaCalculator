class Rectangle:
    def __init__(self, width:int,height:int):
        self.width = width
        self.height = height

    def set_width(self, width:int):
        self.width = width
    
    def set_height(self, height:int):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'  
        picture = ''
        for _ in range(self.height):
            picture += '*' * self.width + '\n'
        return picture

    def get_amount_inside(self,shape:object):
        if isinstance(shape, Rectangle):
            fits_width = self.width // shape.width
            fits_height = self.height // shape.height
            return fits_width * fits_height
        elif isinstance(shape, Square):
            fits_width = self.width // shape.side
            fits_height = self.height // shape.side
            return fits_width * fits_height
        else:
            return 0
    
    def __repr__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

    def set_side(self,side:int):
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square(side={self.width})"