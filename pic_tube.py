from PIL import Image
from rembg import remove
from pathlib import Path
import config
import os


class PicTube:
    """
    This class represent the manipulation of images with the following attributes:
    - original_file: The original file format of the image file.
    """

    def __init__(self, original_file):
        """
        Initialize a new Pictube object with the given original_file.

        Args:
        :param original_file: The original file name.

        Creates necessary folders to handle file uploads, conversions and downloads.

        Return void.
        """
        os.makedirs(config.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(config.CONVERT_FOLDER, exist_ok=True)
        os.makedirs(config.DOWNLOAD_FOLDER, exist_ok=True)

        # :var __original_file: private '/static/assets/upload/<filename.xyz>'
        self.__original_file = Path(config.UPLOAD_FOLDER) / original_file

        # :var __PNG: private str '<filename.png>'
        self.__PNG = original_file.split('.')[0] + '.png'

        # :var __converted_file: private str '/static/assets/convert/<filename.png>'
        self.__converted_file = Path(config.CONVERT_FOLDER) / self.__PNG

        # :var __download_file: private str '/static/assets/download/<filename.png>'
        self.__download_file = Path(config.DOWNLOAD_FOLDER) / self.__PNG

    def process_image(self):
        """
        Process the uploaded image by convert it to .PNG, removing the background, and saving the result.

        Return void.
        """
        with (self.__original_file.open('rb') as input_file,
              self.__download_file.open('wb') as output_file):
            im = Image.open(input_file)
            im.save(self.__converted_file, format='png',
                    optimize=True, quality=90)

            input_file = self.__converted_file.read_bytes()
            rm_bg = remove(input_file, alpha_matting=True,
                           alpha_matting_foreground_threshold=50, discard_threshold=1e-5, shift=1e-5)

            # rm_bg = remove(input_file)
            output_file.write(rm_bg)

        # Unlink the uploaded file and converted file
        self.__original_file.unlink()
        self.__converted_file.unlink()


# Example usages
test = PicTube('pic.jpg')
test.process_image()
