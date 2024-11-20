import PyPDF2
import sys

WaterMark=sys.argv[1]
PdfList=sys.argv[2:]
writer=PyPDF2.PdfWriter()


for pdf in PdfList:
    reader = PyPDF2.PdfReader(pdf)
    for i in range(len(reader.pages)):
        content_page=reader.pages[i]
        mediabox=content_page.mediabox
        reader1 = PyPDF2.PdfReader(WaterMark)
        image_page = reader1.pages[0]
        image_page.merge_page(content_page)
        image_page.mediabox=mediabox
        writer.add_page(image_page)

with open('pdf_result.pdf', "wb") as fp:
    writer.write(fp)