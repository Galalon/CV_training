

class ShapeParser:

    def __init__(self):
        self.shapes = []

    def parse(self, filename):
        with open(filename) as file:
            for line in file:
                self.parse_line(line)
        return self.shapes

    def parse_line(self, line):
        parts = line.split()
        if len(parts) == 0:
            return
        if parts[0] == 'circle':
            self.parse_circle(parts)
        elif parts[0] == 'rectangle':
            self.parse_rectangle(parts)
        elif parts[0] == 'square':
            self.parse_square(parts)
        elif parts[0] == 'triangle':
            self.parse_triangle(parts)

    def parse_circle(self, parts):
        if len(parts) != 4:
            raise ValueError('Invalid circle')
        self.shapes.append(('circle', float(parts[1]), float(parts[2]), float(parts[3])))

    def parse_rectangle(self, parts):
        if len(parts) != 5:
            raise ValueError('Invalid rectangle')
        self.shapes.append(('rectangle', float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])))

    def parse_square(self, parts):
        if len(parts) != 4:
            raise ValueError('Invalid square')
        self.shapes.append(('square', float(parts[1]), float(parts[2]), float(parts[3])))

    def parse_triangle(self, parts):
        if len(parts) != 7:
            raise ValueError('Invalid triangle')
        self.shapes.append(('triangle', float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5]), float(parts[6])))


# Example for using the ShapeParser
# parser = ShapeParser()
# shapes = parser.parse('shapes.txt')
# print(shapes)


# shapes.txt:
# circle 10 10 5
# rectangle 10 10 20 30
# square 10 10 40
# triangle 10 10 20 30 40 50
