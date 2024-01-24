from PIL import Image
from rembg import remove
from pathlib import Path
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
        Process the uploaded image and converted to .PNG and save
        Remove the background from the .PNG image

        Open the uploaded file as 'rb' -> read as bytes (input_file)
        Open the output file as 'wb' -> write as bytes (output_file)

        Open the input_file
        Convert it into .PNG and saved into the converted folder
        Read the converted file as bytes
        Remove the background from it
        Write the output file in the downloaded folder

        Return void
        """
        with (self.__original_file.open('rb') as input_file,
              self.__download_file.open('wb') as output_file):
            im = Image.open(input_file)
            im.save(self.__converted_file, format='png',
                    optimize=True, quality=90)

            input_file = self.__converted_file.read_bytes()
            # rm_bg = remove(input_file, alpha_matting=True,
            #                alpha_matting_foreground_threshold=200)
            rm_bg = remove(input_file)
            output_file.write(rm_bg)

        # Unlink the uploaded file and converted file
        self.__original_file.unlink()
        self.__converted_file.unlink()


test = PicTube('pic.jpg')
test.process_image()
