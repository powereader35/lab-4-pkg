from geometry import shapes, utils

#A short explanation for creating shapes and printing their areas!

# to create a new square:

a = shapes.Square(3) # the input is the side length

print(a.area()) # to print the area

# for a circle 
b = shapes.Circle(3) # the input is the side length

print(b.area()) # to print the area

# comparing different shapes
a = shapes.Square(3)
b = shapes.Circle(6)
c = shapes.Square(2)

stats = utils.area_stats((a,b,c))

print(stats)