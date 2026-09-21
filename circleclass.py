class Coordinate(object):
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval
    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    
class Circle(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    def is_inside(self, point):
        return point.distance(self.center) < self.radius

center = Coordinate(2, 2)
my_circle = Circle(center, 2)
p = Coordinate(1, 1)

print(my_circle.is_inside(p))