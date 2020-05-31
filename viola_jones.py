from integral_image import calc_integral_image
from region import Region
import numpy as np

class ViolaJones:
    # this is a ensemble system
    # only param is number of weak classifier
    def __init__(self, weak_features_count):
        self.W = weak_features_count

    # create Haar-like features
    def create_features(self, shape):
        height, width = shape
        all_possible_features = []

        for cur_width in range(1, width+1):
            for cur_height in range(1, height + 1):
                x = 0
                while x + cur_width < width :
                    y = 0
                    while y + cur_height < height :
                        cur_rect = Region(x, y, cur_width, cur_height)

                        # create two horizontally adjacent rectange feature
                        if x + 2 * cur_width < width:
                            cur_rect_right = Region(x + cur_width, y, cur_width, cur_height)
                            all_possible_features.append(([cur_rect], [cur_rect_right]))

                            # create three horizontally adjacent rectangle feature
                            if x + 3 * cur_width < width :
                                cur_rect_right_right = Region(x + 2 * cur_width, y, cur_width, cur_height)
                                all_possible_features.append(([cur_rect_right], [cur_rect, cur_rect_right_right]))

                            # create four rectange feature
                            if y + 2 * cur_height < height:
                                cur_rect_bottom = Region(x , y + cur_height, cur_width, cur_height)
                                cur_rect_bottom_right = Region(x + cur_width, y + cur_height, cur_width, cur_height)
                                all_possible_features.append(([cur_rect, cur_rect_bottom_right], [cur_rect_right, cur_rect_bottom]))
                                

                        # create two vertically adjacent rectange feature
                        if y + 2 * cur_height < height:
                            cur_rect_bottom = Region(x , y + cur_height, cur_width, cur_height)
                            all_possible_features.append(([cur_rect], [cur_rect_bottom]))
                            # create three vertically adjacent rectangle feature
                            if y + 3 * cur_height < height :
                                cur_rect_bottom_bottom = Region(x, y + 2 * cur_height, cur_width, cur_height)
                                all_possible_features.append(([cur_rect_bottom], [cur_rect, cur_rect_bottom_bottom]))
                        
                        
                        
                        
                        y += 1
                    x += 1
        return all_possible_features


    # image_dataset -> array of tuples (image, image_label)
    def train(self, image_dataset):
        training_image_data = []
        weights = np.zeros(len(image_dataset))
        positive_class_count = 0
        negative_class_count = 0

        for i in range(len(image_dataset)):
            training_image_data.append((calc_integral_image(image_dataset[i][0]), image_dataset[i][1]))
            if image_dataset[i][1] == 1:
                positive_class_count += 1
            else:
                negative_class_count += 1
        
        for i in range(len(image_dataset)):
            if image_dataset[i][1] == 1:
                weights[i] = 1.0 / (2 * positive_class_count)
            else:
                weights[i] = 1.0 / (2 * negative_class_count)