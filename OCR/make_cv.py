import docx
from docx2pdf import convert
import os

# Open the document
doc = docx.Document(r"cv_template.docx")

# Find the text you want to replace
old_text = "Job desc"
for paragraph in doc.paragraphs:
    if old_text in paragraph.text:
        # Replace the text while maintaining the same style and formatting
        for run in paragraph.runs:
            if old_text in run.text:
                new_text = run.text.replace(old_text, '''Madrid, Spain (working remotely)
• Designed and implemented the ETL pipeline for a predictive model of traffic on the main roads in
• Automated scripts in R to extract, transform, clean (incl. anomaly detection), and load into MySQL
• Designed an experiment for Google Spain (conducted in October 2014) to measure the impact of
• A matched-pair, cluster-randomized design, which involved selecting the test and control groups
from a sample of 50+ cities in Spain (where geo-targeted ads were possible) based on their sales-
wise similarity over time, using wavelets (and R).
Head of Sales, Spain & Portugal — Test &Measurement dept.
• Applied analysis of sales and market trends to decide the direction of the department.''')
                run.text = new_text
                break  # break out of the loop once the text is replaced in one run object

# Save the document
doc.save("modified.docx")

convert(r'modified.docx', r"modified.pdf")

os.remove('modified.docx')
