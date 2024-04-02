import PyPDF2
import os

class pdfTool:

    def splitPdf(self, inputFilePath, splitAt = None, selectPage = None):
        if (os.path.exists(inputFilePath) and os.path.basename(inputFilePath).endswith(".pdf")):
            fileName = os.path.basename(inputFilePath).replace(".pdf", "")
            outputFolderPath = os.path.dirname(inputFilePath) + "\\" + fileName + "_Output"

            #Create output folder if not created
            if not (os.path.exists(outputFolderPath)):
                os.makedirs(outputFolderPath)
            
            with open(inputFilePath, 'rb') as file:
                pdfReader = PyPDF2.PdfReader(file)
                numPages = len(pdfReader.pages)

                # Split all pages
                if(all(fields is None for fields in (splitAt,selectPage))):
                    for idx in range(0, numPages):
                        pdfWriter = PyPDF2.PdfWriter()
                        pdfWriter.add_page(pdfReader.pages[idx])
                        with open(f"{outputFolderPath}\{fileName}_{idx+1}.pdf", 'wb') as output:
                            pdfWriter.write(output)

                # Split from specified page till the end
                elif(splitAt is not None):
                        pdfWriter = PyPDF2.PdfWriter()
                        # First page to specified page
                        for idx in range(0, int(splitAt)):
                            pdfWriter.add_page(pdfReader.pages[idx])
                        with open(f"{outputFolderPath}\{fileName}_1-{splitAt}.pdf", 'wb') as output:
                            pdfWriter.write(output)

                        pdfWriter = PyPDF2.PdfWriter()
                        # Specified page till last page
                        for idx in range(int(splitAt), numPages):
                            pdfWriter.add_page(pdfReader.pages[idx])
                        with open(f"{outputFolderPath}\{fileName}_{int(splitAt)+1}-{numPages}.pdf", 'wb') as output:
                            pdfWriter.write(output)
                elif(selectPage is not None):
                    if len(selectPage) != 0:
                        pdfWriter = PyPDF2.PdfWriter()
                        # First page to specified page
                        for pages in selectPage:
                            pdfWriter.add_page(pdfReader.pages[int(pages)-1])
                        with open(f"{outputFolderPath}\{fileName}_SelectedPages.pdf", 'wb') as output:
                            pdfWriter.write(output)
                else:
                    print("Error")

        else:
            print("Error, invalid file.")