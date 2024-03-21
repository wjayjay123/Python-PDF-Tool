from pdfTool import pdfTool 
import os

pdfToolObj = pdfTool()
inputFilePath = input("Enter file path:").strip('"')
pdfTool.splitPdf(inputFilePath)

