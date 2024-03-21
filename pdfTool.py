import PyPDF2
import os

class pdfTool():

    def splitPdf(inputFilePath, startPage = None, endPage = None, selectPage = None):
        fileName = os.path.basename(inputFilePath)
        outputFolderPath = inputFilePath + "_Output"

        #Create output folder if not created
        if not (os.path.exists(outputFolderPath)):
            os.makedirs(outputFolderPath)
        
        with open(inputFilePath, 'rb') as file:
            pdfReader = PyPDF2.PdfReader(file)
            numPages = len(pdfReader.pages)

            # Split all pages
            for idx, page in enumerate(pdfReader.pages):
                pdfWriter = PyPDF2.PdfWriter()
                pdfWriter.add_page(page)
                with open(f"{outputFolderPath}\{fileName}_{idx+1}.pdf", 'wb') as output:
                    pdfWriter.write(output)