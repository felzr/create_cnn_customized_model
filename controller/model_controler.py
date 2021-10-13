import pathlib

from tflite_model_maker.config import ExportFormat
from tflite_model_maker import ImageClassifierDataLoader
from tflite_model_maker import image_classifier


def create_dataset():
    print('criando dataset')
    data = ImageClassifierDataLoader.from_folder('./images_dataset')
    train_data, rest_data = data.split(0.8)
    validation_data, test_data = rest_data.split(0.5)
    model = image_classifier.create(train_data, validation_data=validation_data, epochs=10)
    model.summary()
    model.export(export_dir='model/', export_format=ExportFormat.LABEL)
    model.export(export_dir='model/')

def image_count():
    print('contando numero de images')
    data_dir = pathlib.Path('./images_dataset')
    image_count = len(list(data_dir.glob('*/*.jpeg')))
    print(image_count)


def class_count():
    print('contando numero de images')
    data_dir = pathlib.Path('./images_dataset')
    image_count = len(list(data_dir.glob('*/*.jpeg')))
    print(image_count)


def get_class_name(path):
    data_dir = pathlib.Path('./images_dataset')
    labels = list(data_dir.glob())
    print(labels)

