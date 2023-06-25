import utils
from utils import *
import numpy as np


def warpPerspective(img, transform_matrix, output_width, output_height):
    """
    TODO : find warp perspective of image_matrix and return it
    :return a (width x height) warped image
    """
    res = np.zeros(shape=(output_width, output_height, 3))
    for i in range(len(img)):
        for j in range(len(img[i])):

            pix = np.dot(transform_matrix, np.array([i, j, 1]))
            pix[0] /= pix[2]
            pix[1] /= pix[2]
            if 0 <= int(pix[0]) < output_width and 0 <= int(pix[1]) < output_height:
                res[int(pix[0]), int(pix[1])] = img[i, j]

    return res
    pass


def grayScaledFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    filter_matrix = np.array([[.3, .6, .11]])
    return utils.Filter(img, filter_matrix)
    pass


def crazyFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    filter_matrix = np.array([[0, 0, 1],
                             [0, .5, 0],
                             [.5, .5, 0]])
    inv = np.linalg.inv(filter_matrix)
    res = utils.Filter(img, filter_matrix)
    return res, utils.Filter(res, inv)
    pass


def scaleImg(img, scale_width, scale_height):
    """
    TODO : Complete this part based on the description in the manual!
    """
    res = np.zeros(shape=(width * scale_width, height * scale_height, 3))
    for i in range(width * scale_width):
        for j in range(height * scale_height):
            old_x = i / scale_width
            old_y = j / scale_height
            res[i, j] = img[int(old_x), int(old_y)]

    return res
    pass


def permuteFilter(img):
    """
    TODO : Complete this part based on the description in the manual!
    """
    filter_matrix = np.array([[0, 0, 1],
                             [0, 1, 0],
                             [1, 0, 0]])
    return utils.Filter(img, filter_matrix)
    pass


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')

    # You can change width and height if you want
    width, height = 300, 400

    showImage(image_matrix, title="Input Image")

    # TODO : Find coordinates of four corners of your inner Image ( X,Y format)
    #  Order of coordinates: Upper Left, Upper Right, Down Left, Down Right
    pts1 = np.float32([[241, 25], [586, 184], [251, 986], [610, 912]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = getPerspectiveTransform(pts1, pts2)

    warpedImage = warpPerspective(image_matrix, m, width, height)
    showWarpPerspective(warpedImage)

    grayScalePic = grayScaledFilter(warpedImage)
    showImage(grayScalePic, title="Gray Scaled")

    crazyImage, invertedCrazyImage = crazyFilter(warpedImage)
    showImage(crazyImage, title="Crazy Filter")
    showImage(invertedCrazyImage, title="Inverted Crazy Filter")

    scaledImage = scaleImg(warpedImage, 3, 4)
    showImage(scaledImage, title="Scaled Image")

    permuteImage = permuteFilter(warpedImage)
    showImage(permuteImage, title="Permuted Image")
