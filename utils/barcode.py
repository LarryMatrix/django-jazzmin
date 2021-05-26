import os
import barcode
from barcode.writer import ImageWriter
from django.core.files.base import File


class BarCodeGenerator:
    """
     This class used to generate and render barcode.
    """

    def __init__(self, reg_number):
        self.reg_number = reg_number
        self.global_path = None

    def write(self, *args, **kwargs):
        barcode_class = barcode.get_barcode_class('code128')
        code = barcode_class(f"{self.reg_number}", writer=ImageWriter())
        reg_number_barcode = code.save(code)
        self.global_path = reg_number_barcode
        return self.render(filename=reg_number_barcode)

    @staticmethod
    def render(filename=None):
        if filename:
            f = open(filename, 'rb')
            i = File(f)
            os.remove(filename)
            return i

        return NotImplementedError
