from utils.image_download import simple_image_download as simp
from utils.image_treatment import images_treatment as treatment
import matplotlib
from matplotlib import pyplot
from matplotlib.image import imread
import cv2
import os

folder = "images_dataset/"


def donwload_images(query_element, amount_images):
    response = simp.simple_image_download
    response().download(query_element, amount_images)
    print(response().urls(query_element, amount_images))


def get_images():
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


def show_images(query):
    matplotlib.use('TkAgg')
    for i in range(9):
        # define subplot
        pyplot.subplot(330 + 1 + i)
        # define filename
        filename = folder + query + '/' + query + '_' + str(i + 1) + '.jpeg'
        # load image pixels
        image = imread(filename)
        # plot raw pixel data
        pyplot.imshow(image)
    pyplot.show()


def resize_images(query):
    food_folder = folder + '/' + query
    tr = treatment.images_tratment
    tr.resize_images(food_folder)


def convert_png_images(query):
    food_folder = folder + '/' + query
    tr = treatment.images_tratment
    tr.convert_png_images(food_folder)


def list_images(query):
    food_folder = folder + query
    tr = treatment.images_tratment
    tr.list_images(food_folder)
