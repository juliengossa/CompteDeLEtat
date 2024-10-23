# python code to translate the table spanning from page 171 to 210 of a pdf file into csv file

import PyPDF2
import csv

years = ["2021","2022","2023"]

def extract_text_from_pdf(pdf_path, start_page, end_page):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        for page_num in range(start_page - 1, end_page):
            page = reader.getPage(page_num)
            text += page.extract_text()
    return text

def parse_table_data(text):
    # This function should be customized based on the structure of the table in the PDF
    lines = text.split('\n')
    table_data = []
    operateur = "Inconnu"
    for line in lines:
        if not line.strip():  continue
        if "–" in line and "Opérateur – Statut" not in line:
            values = line.split("–")
            operateur = [ values.strip() for values in values ]
        else:
            values = line.split()
            if values[0] not in years: continue
            year = values[0]
            value = values[1] + values[2] if values[1] in ["1","2","3"] else values[1]
            if not value.isnumeric(): continue
            table_data.append(operateur+[year, value])
    return table_data

def write_to_csv(table_data, csv_path):
    with open(csv_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Opérateur", "Statut", "Année", "Valeur"])
        for row in table_data:
            writer.writerow(row)

pdf_path = 'Jaune2025_operateurs.pdf'
csv_path = 'operateurs.csv'
start_page = 171
end_page = 210

text = extract_text_from_pdf(pdf_path, start_page, end_page)
table_data = parse_table_data(text)
write_to_csv(table_data, csv_path)
