from PIL import Image
from rembg import remove
import config
import os


class PicTube:
    """
    This class represent the manipulation of images with the following attributes:
    - original_file: The original format of the image file
    - converted_file: The converted format of the image file
    """

    def __init__(self, original_file):
        """
        Initialize a new Pictube object with the given original_file

        Args:
        :param original_file: The original file name
        Make an upload folder to handle file uploads
        Make a convert folder to handle file conversion
        Make a download folder to handle file downloads

        Return void
        """
        os.makedirs(config.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(config.CONVERT_FOLDER, exist_ok=True)
        os.makedirs(config.DOWNLOAD_FOLDER, exist_ok=True)

        # :var __original_file: private str '/static/assets/upload/<filename>'
        self.__original_file = config.UPLOAD_FOLDER + original_file

        # :var __PNG: private str '<filename.png>'
        self.__PNG = original_file.split('.')[0] + '.png'

        # :var __converted_file: private str '/static/assets/convert/<filename>.png'
        self.__converted_file = config.CONVERT_FOLDER + self.__PNG

        # :var __download_file: private str '/static/assets/download/<filename>.png'
        self.__download_file = config.DOWNLOAD_FOLDER + self.__PNG

    def _convert_to_png(self):
        """
        Protected function
        Convert the original file format
        Save the converted file

        Return void
        """

        # :var im: object Open the uploaded file
        im = Image.open(self.__original_file)
        im.save(self.__converted_file, format='png')

    def _remove_background(self):
        """
        Protected function
        Remove background from an image
        Save the output file in the download folder

        Return void
        """
        with open(self.__download_file, 'wb') as file:
            input_file = open(self.__converted_file, 'rb').read()
            rm_bg = remove(input_file, alpha_matting=True, alpha_matting_foreground_threshold=50)
            file.write(rm_bg)
            file.close()
        os.remove(self.__original_file)
        os.remove(self.__converted_file)


class PicRunner(PicTube):
    """
    This class is a subclass of PicTube
    """
    def call_pictube(self):
        """
        Static function
        Purpose of this function is to run all the protected functions inside the PicTube class one-by-one

        Return void
        """
        self._convert_to_png()
        self._remove_background()


# test = PicRunner('pi1.jpg')
# test.call_pictube()
