# Advent of Code - Day 20
# Part 2

from copy import deepcopy

def parseInput(file):
    image = []
    for i, line in enumerate(open(file)):
        if i == 0:
            algorithm = line.strip()
        elif i > 1:
            image_line = []
            for elem in line.strip():
                image_line.append(elem)
            image.append(image_line)

    return algorithm, image


class ImageEnhancer:
    def __init__(self, algorithm, image):
        self.algorithm = algorithm
        self.flash = False
        self.image_range_x = len(image)-1
        self.image_range_y = len(image[0])-1
        self.image_padding(image)

    def image_padding(self, image):
        padded_image = []
        if self.flash:
            border = "#"
        else:
            border = "."
        for row in range(0, self.image_range_x + 3):
            padded_image_row = []
            for col in range(0, self.image_range_y + 3):
                if row < 1 or row > self.image_range_y + 1:
                    padded_image_row.append(border)
                elif col < 1 or col > self.image_range_y + 1:
                    padded_image_row.append(border)
                else:
                    padded_image_row.append(image[row-1][col-1])
            padded_image.append(padded_image_row)
        self.image_range_x = len(padded_image)-1
        self.image_range_y = len(padded_image[0])-1
        self.image = padded_image

    def in_image_range(self, x, y):
        if x < 0 or x > self.image_range_x:
            return False
        if y < 0 or y > self.image_range_y:
            return False
        return True

    def get_pixel_value(self, x, y):
        x_vals = [x-1, x, x+1]
        y_vals = [y-1, y, y+1]
        binary_row = []
        for xx in x_vals:
            for yy in y_vals:
                if self.in_image_range(xx, yy):
                    binary_row.append(self.image[xx][yy])
                else:
                    if self.flash:
                        binary_row.append("#")
                    else:
                        binary_row.append(".")
        binary_number = []
        for pixel in binary_row:
            if pixel == "#":
                binary_number.append(1)
            else:
                binary_number.append(0)
        pixel_value = int("".join(str(i) for i in binary_number), 2)
        return pixel_value

    def enhance_pixel(self, x, y):
        pixel = self.get_pixel_value(x, y)
        algorithm_value = self.algorithm[pixel]
        self.new_image[x][y] = algorithm_value

    def enhance_image(self):
        self.new_image = deepcopy(self.image)
        for x, row in enumerate(self.image):
            for y, _ in enumerate(row):
                self.enhance_pixel(x, y)
        self.image = deepcopy(self.new_image)
        self.flash = not self.flash
        return self.image

# ----- Part 2 ----- #

algorithm, image = parseInput("input.txt")
ie = ImageEnhancer(algorithm, image)
image = ie.enhance_image()

for n in range(0, 49):
    ie.image_padding(image)
    image = ie.enhance_image()

lit_pixels = 0
for row in image:
    for ele in row:
        if ele == "#":
            lit_pixels += 1
print(lit_pixels)
