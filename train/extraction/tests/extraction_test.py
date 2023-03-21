import unittest
from pathlib import Path
from PIL import Image
import filecmp
import fitz
import sys

class TestExtractPdfToPng(unittest.TestCase):

    def test_extract_pdfs_to_png(self):
        from io import BytesIO
        from fitz import Pixmap

        # setting path
        from extraction import extract_pdf_to_png

        extract_pdf_to_png("tests/tester")

        # check if PNG files were created
        png_directory_path = ".extracted_images"
        png_files = [p for p in Path(png_directory_path).iterdir() if p.is_file()]
        self.assertGreater(len(png_files), 0)


if __name__ == '__main__':
    unittest.main()
