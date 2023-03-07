import re
import nltk
from nltk.tokenize import sent_tokenize
import PyPDF2
import spacy

# Load the PDF document and extract text
pdf_file = open(r"C:\Users\umaRf\OneDrive\Desktop\samplecvs\Green Grey Color Blocks Copy Editor CV.pdf", 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
text = ""
for page in pdf_reader.pages:
    text += page.extract_text()

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")
# Process the text with spaCy
doc = nlp(text)

# Sample CV text
cv_text = text

work_exp_start = re.split(r'Work Experience', cv_text)

print(work_exp_start[1])
for ent in doc.ents:
    print(ent.text, ent.label_)

# Print the extracted sentences

