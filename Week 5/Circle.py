class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("New circle with diameter " + str(diameter))

    def area(self, radius):
        return self.pi * radius ** 2


circle = Circle(40) 

pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle. area(11460/2)

circle = Circle(70)
