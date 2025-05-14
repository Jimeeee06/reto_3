class Point:
    definition: str = "Entidad geometrica abstracta que representa una ubicación en un espacio."
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

class Line:
    def __init__(self, length: float = 0, slope: float = 0, start: Point = None, end: Point = None):
        self.length = length
        self.slope = slope
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()
    def compute_slope(self):
        delta_x = self.end.x - self.start.x
        delta_y = self.end.y - self.start.y
        return delta_y / delta_x if delta_x != 0 else print('undefined slope') 
    def compute_length(self):
        delta_x = self.end.x - self.start.x
        delta_y = self.end.y - self.start.y
        return (delta_x ** 2 + delta_y ** 2) ** 0.5
    def compute_horizontal_cross(self):
        if self.slope == 0 or (self.start.y >=0 and self.end.y >= 0) or (self.start.y <= 0 and self.end.y <= 0):
            return "No horizontal cross"
        x = self.start.x
        y = self.start.y + self.slope * (x - self.start.x)
        return f"The horizontal cross is at {Point(x, y)}"
    def compute_vertical_cross(self):
        if self.slope == 0 or (self.start.x >=0 and self.end.x >= 0) or (self.start.x <= 0 and self.end.x <= 0):
            return "No vertical cross"
        y = self.start.y
        x = self.start.x + (y - self.start.y) / self.slope
        return f"The vertical cross is at {Point(x, y)}"
    def intersection(self, line:"Line"):
        if self.slope == line.slope:
            return "No intersection"
        x = (line.start.y - self.start.y + self.start.x * self.slope - line.start.x * line.slope) / (self.slope - line.slope)
        y = self.slope * (x - self.start.x) + self.start.y
        return f"The intersection with {line} is {Point(x, y)}"
    def __str__(self):
        return f"Line from {self.start} to {self.end} with length {self.length} and slope {self.slope}"

class Rectangle:
    #initializes the rectangle with the width and height of the rectangle in 0,
    # and the center of the rectangle in (0,0). 
    def __init__(self, method: int, width: float = 0, height: float = 0, center: Point = None, 
                 corner_point: Point = None, point1: Point = None, point2: Point = None, 
                 line1: Line = None, line2: Line = None, line3: Line = None, line4: Line = None):
        #if the method is 1, we ask for the width and height of the rectangle,
        #and for the bottom left corner of the rectangle.
        if method == 1:
            self.width = width
            self.height = height
            self.corner_point = corner_point
            self.center = Point(self.corner_point.x + self.width / 2, self.corner_point.y + self.height / 2)
        #if the method is 2, we ask for the width and height of the rectangle,
        #and for the center of the rectangle.
        elif method == 2:
            self.width = width
            self.height = height
            self.center = center
        #if the method is 3, we ask for the coordinates of the two vertices of the rectangle.
        elif method == 3:
            point1: Point = point1
            point2: Point = point1
            self.width = abs(point1.x - point2.x)
            self.height = abs(point1.y - point2.y) 
            self.center = Point((point1.x + point2.x) / 2, (point1.y + point2.y) / 2)
        #if the method is 4, we ask for the four lines of the rectangle.
        elif method == 4:
            self.line1 = line1
            self.line2 = line2
            self.line3 = line3
            self.line4 = line4
            self.height = max(line1.length, line2.length, line3.length, line4.length)
            self.width = min(line1.length, line2.length, line3.length, line4.length)
            self.center = Point((line1.start.x + line3.start.x) / 2, (line1.start.y + line3.start.y) / 2)
        else:
            pass
    def compute_area(self) -> float:
        return self.width * self.height
    def compute_perimeter(self) -> float:
        return 2 * (self.width + self.height)
    def compute_interference_point(self, point: Point) -> bool:
        # Check if the point is inside the rectangle
        if (self.center.x - self.width / 2 <= point.x <= self.center.x + self.width / 2 and
            self.center.y - self.height / 2 <= point.y <= self.center.y + self.height / 2):
            return True
        else:
            return False
    def compute_interference_line(self, ) -> bool:
        pass
    

class Square(Rectangle):
    def __init__(self, method, width = 0, height = 0, center = None):
        super().__init__(method, width, height, center)
