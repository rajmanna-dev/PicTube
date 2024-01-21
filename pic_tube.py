from PIL import Image
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
        Make a download folder to handle file downloads

        Return void
        """
        os.makedirs(config.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(config.DOWNLOAD_FOLDER, exist_ok=True)

        # :var original_file: str '/static/assets/upload/<filename>'
        self.original_file = config.UPLOAD_FOLDER + original_file

        # :var converted_file: str '/static/assets/download/<filename>.png'
        self.converted_file = config.DOWNLOAD_FOLDER + original_file.split('.')[0] + '.png'

    def convert_to_png(self):
        """
        Convert the original file format
        Save the converted file
        Return void
        """

        # :var im: object Open the uploaded file
        im = Image.open(self.original_file)
        im.save(self.converted_file, format='png')
