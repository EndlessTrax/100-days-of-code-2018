'''
Write a script partial_PDF.py that extracts a specific range of pages from a PDF file based on file names 
    and a page range supplied by the user. The program should run as follows:
1. Let the user choose a file using a fileopenbox
2. Let the user choose a beginning page to select using an enterbox
3. If the user enters invalid input, use a msgbox to let the user know that there was a problem, 
    then ask for a beginning page again using an enterbox
4. Let the user choose an ending page using another enterbox
5. If the user enters an invalid ending page, use a msgbox to let the user know that there was a problem, 
    then ask for a beginning page again using an enterbox
6. Let the user choose an output file name using a savefilebox
7. If the user chooses the same file as the input file, let the user know the problem using a msgbox, 
    then ask again for a file name using a savefilebox
8. Output the new file as a section of the input file based on the usersupplied page range. 
    The user should be able to supply “1” to mean the first page of the document. There are a number of potential
    issues that your script should be able to handle. These include:
    • If the user cancels out of a box, the program should exit without any errors
    • Check that pages supplied are valid numbers; you can use the string method isdigit() to check whether
        or not a string is a valid positive integer. (The isdigit() method will return False for the string “0” as well.)
    • Check that the page range itself is valid (i.e., the end to the start)
'''

import os
from easygui import *
from PyPDF2 import PdfFileReader, PdfFileWriter


# Choose file to open
def open_file():
    start_file = fileopenbox(title="Select your file to edit...")
    if start_file is None:
        exit()

    file_path = os.path.abspath(start_file)
    return file_path


# Choose first and check if valid input
def start_page():
    input_first_page = enterbox("What page would you like to start at?", "Choose starting point")
    if input_first_page.isdigit() and input_first_page != "0":
        first_page = int(input_first_page)
    else: 
        msgbox("That is not a valid page number!", "Please try again...")

    return first_page


# Choose ending page and check if valid input
def finish_page():
    input_last_page = enterbox("What page would you like to start at?", "Choose starting point")
    if input_last_page.isdigit() and input_last_page != "0":
        last_page = int(input_last_page)
    else: 
        msgbox("That is not a valid page number!", "Please try again...")

    return last_page


# Check page is valid
def check_valid_page_range(user_file, num1, num2):
    page_number = user_file.getNumPages()
    if num1 < page_number and num2 <= page_number and num1 <= num2:
        pass
    else:
        msgbox("That is not a valid page number range. Please check your page numbers exist.", "Please try again...")


# Choose output file and check filename does not already exist
def save_file(sfile):
    end_file = filesavebox(title="Where would you like to save your file?")
    while sfile == end_file:
        msgbox("Cannot overwrite original file!", "Please choose another file...")
        end_file = filesavebox(title="Where would you like to save your file?")
    return end_file


def main():
    # Ask what file to open
    user_file = open_file()

    # Ask which pages the user wants to extract
    beginning_page = start_page()
    ending_page = finish_page()
    
    # Create reader and writer objects 
    input_file = PdfFileReader(open(user_file, 'rb'))
    output_pdf = PdfFileWriter()

    # Check the pages give are valid page numbers within the document
    check_valid_page_range(input_file, beginning_page, ending_page)
    
    # Create the output file
    output_file = open(f"{user_file}-edited.pdf", 'wb')

    # Extract the pages 
    for n in range(beginning_page - 1, ending_page):
        page = input_file.getPage(n)
        output_pdf.addPage(page)

    # Write the pages to the file.
    output_pdf.write(output_file)
    output_file.close()
  

if __name__ == '__main__':
    main()
