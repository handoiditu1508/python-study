class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
point1.draw()
print(point1.x)

point1.z = 30
print(point1.z)
