import csv
import re
import pandas as pd

def replace_text(html):
    # Replace Nexer with Nordic Solutions
    html = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'umar.farooq@nordicsolutions.com', html, flags=re.IGNORECASE)
    html = re.sub('Nexer', 'Nordic Solutions', html, flags=re.IGNORECASE)
    html = re.sub('Nexer Group', 'Nordic Solutions', html, flags=re.IGNORECASE)

    # Remov any links
    html = re.sub(r'<a.*?</a>', '', html)
    html = re.sub(r"(please contact).*", r"\1 Umar Farooq Khan at umar.farooq@nordicsolutions.com" , html)
    print(html)
    return html


df = pd.read_csv('all_countries_nexer.csv')

df['desc'] = df['op_desc'].apply(replace_text)

df.to_csv('output_file_all_countries.csv', index=False)

