from controller import image_controller as image_controller
from controller import model_controler as model_controler
import tensorflow as tf

image_controller = image_controller
model_controler = model_controler

folder = "images_dataset/"


def call_images_from_goole(query, amount_images):
    image_controller.donwload_images(query, amount_images)


def show_images(query):
    image_controller.show_images(query)


def resize_images(query):
    image_controller.resize_images(query)


def convert_to_jpeg(query):
    image_controller.convert_png_images(query)


def list_images(query):
    image_controller.list_images(query)


def create_dataset():
    model_controler.create_dataset()


def count_images():
    model_controler.class_count()


def get_labels(folder):
    model_controler.get_class_name(folder)


def testTensorflow():
    tf.test.is_gpu_available(
        cuda_only=False, min_cuda_compute_capability=None
    )
