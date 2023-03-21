import unittest
from pathlib import Path
from PIL import Image
import filecmp
import PyPDF2
import fitz

class TestExtractPdfToPng(unittest.TestCase):

    def test_extract_pdfs_to_png(self):
        from io import BytesIO
        from fitz import Pixmap
        import os
        from extraction import extract_pdf_to_png
        # import os, fitz
        # doc = fitz.open()  # PDF with the pictures
        #
        # img = fitz.open("1626442120528.jpeg")  # open pic as document
        # rect = img[0].rect  # pic dimension
        # pdfbytes = img.convert_to_pdf()  # make a PDF stream
        # img.close()  # no longer needed
        # imgPDF = fitz.open("pdf", pdfbytes)  # open stream as PDF
        # page = doc.new_page(width=rect.width,  # new page with ...
        #                     height=rect.height)  # pic dimension
        # page.show_pdf_page(rect, imgPDF, 0)  # image fills the page
        # doc.save("test/all-my-pics.pdf")
        extract_pdf_to_png("tester")

        # check if PNG files were created
        png_directory_path = "extracted_images"
        png_files = [p for p in Path(png_directory_path).iterdir() if p.is_file()]
        self.assertGreater(len(png_files), 0)


if __name__ == '__main__':
    unittest.main()
