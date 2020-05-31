from integral_image import calc_integral_image

class Region:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def calc_feature(self, cumul_sum):
        yy = self.y + self.height
        xx = self.x + self.width

        return cumul_sum[yy][xx] - cumul_sum[yy][x] - cumul_sum[y][xx] + cumul_sum[y][x]
