import PyPDF2

# open the PDF file
with open(r"C:\Users\umaRf\OneDrive\Desktop\Transfer\Blue Light Blue Color Blocks Flight Attendant CV.pdf", "rb") as file:
    pdf_reader = PyPDF2.PdfReader(file)

    # get the number of pages in the PDF file
    num_pages = len(pdf_reader.pages)

    # iterate over all the pages
    for page_num in range(num_pages):
        page = pdf_reader.pages[(page_num)]
        print(page.extract_text())