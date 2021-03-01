import glob
from PIL import Image


class images_tratment:

    def resize_images(root_dir):
        for filename in glob.iglob(root_dir + '**/*.jpeg', recursive=True):
            print(filename)
            im = Image.open(filename)
            imResize = im.resize((300, 300), Image.NONE)
            imResize.save(filename, 'JPEG', quality=100)

    def convert_png_images(root_dir):
        for filename in glob.iglob(root_dir + '**/*.png', recursive=True):
            print(filename)
            im = Image.open(filename)
            imResize = im.resize((300, 300), Image.NONE)
            imResize = im.convert('RGB')
            imResize.save(filename, 'JPEG', quality=100)


