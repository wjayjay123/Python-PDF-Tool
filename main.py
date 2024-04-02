from pdfTool import pdfTool
from tkinter import filedialog
import os
import tkinter as tk


def menu():
    print("---Menu---")
    print("1.Split PDF File")
    print("2.Merge PDF File")
    print("3.Exit")

def splitMenu():
    print("---Split Menu---")
    print("1.All pages")
    print("2.Split at a specific page")
    print("3.Select pages")
    print("4.Back")

pdfToolObj = pdfTool()
while True:
    menu()
    option = input("->").lower()

    if option == "1" or option == "split":
        splitMenu()
        splitOption = input("->").lower()

        if splitOption == "1" or splitOption == "all":
            win = tk.Tk()
            inputFilePath = filedialog.askopenfilename()
            win.destroy()
            pdfToolObj.splitPdf(inputFilePath)

        elif splitOption == "2" or splitOption == "split":
            win = tk.Tk()
            inputFilePath = filedialog.askopenfilename()
            win.destroy()
            splitPage = input("Enter page number:")
            try:
                pdfToolObj.splitPdf(inputFilePath, splitAt=splitPage)
            except:
                print("Invalid file or page number.\n")

        elif splitOption == "3" or splitOption == "select":
            win = tk.Tk()
            inputFilePath = filedialog.askopenfilename()
            win.destroy()
            selectPage = input("Enter pages (e.g. 1,3,5 or 1-5):")
            if "," in selectPage:
                pages = selectPage.split(",")
            elif "-" in selectPage:
                pageRange = selectPage.split("-")
                pages = []
                for i in range (int(pageRange[0]), int(pageRange[1])+1):
                    pages.append(i)
            elif "," not in selectPage and "-" not in selectPage:
                try:
                    pages = [int(selectPage)]
                except:
                    print("Invalid page numbers.\n")
            try:
                pdfToolObj.splitPdf(inputFilePath, selectPage=pages)
            except:
                print("Invalid file or page number.\n")
        
        elif splitOption == "4" or splitOption == "back":
            pass

        else:
            print("Invalid option.\n")

    elif option == "2" or option == "merge":
        inputFilePath = None
        multiFilePaths = []
        while inputFilePath != "":
            win = tk.Tk()
            inputFilePath = filedialog.askopenfilename()
            win.destroy()
            if inputFilePath != "":
                multiFilePaths.append(inputFilePath)
        try:
            pdfToolObj.mergePDF(multiFilePaths)
        except:
            print("Invalid files.\n")
        


    elif option == "3" or option == "exit":
        print("Exiting program.\n")
        break
    else:
        print("Invalid option.\n")