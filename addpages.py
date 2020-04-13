#!/bin/python3

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4



pdf = PdfFileReader('path/to/file')
pdf_writer = PdfFileWriter()
#pdf.getNumPages()
for page in range(pdf.getNumPages()):
    packet = io.BytesIO()

    can = canvas.Canvas(packet, pagesize=A4)


    can.drawString(525, 30, "ADDTEXT" + str(page) )
    can.save()
    packet.seek(0)
    watermark = PdfFileReader(packet)
    watermark_page = watermark.getPage(0)



    pdf_page = pdf.getPage(page)
    pdf_page.mergePage(watermark_page)
    pdf_writer.addPage(pdf_page)

with open('out.pdf', 'wb') as fh:
    pdf_writer.write(fh)