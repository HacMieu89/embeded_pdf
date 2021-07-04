import sys
from PyPDF2 import PdfFileReader, PdfFileWriter

def js_into_pdf(path):
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    for page in range(pdf.getNumPages()):
        pdf_writer.addPage(pdf.getPage(page))
    pdf_writer.addJS('app.alert("18520084-18520509-18520532");')
    with open('created.pdf', 'wb') as out:
        pdf_writer.write(out)
    print('Created: {0}'.format('created.pdf'))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
        js_into_pdf(path)
    else:
        print('Give the path of the PDF as a first argument')
