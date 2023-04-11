import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('invoices/*')
print(filepaths)
for filepath in filepaths:
    data = pd.read_excel(filepath, sheet_name='Sheet 1')
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr = filename.split('-')[0]
    date = filename.split('-')[1]

    #added invoice
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Invoice nr: {invoice_nr}", ln=1)

    #added date
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Date: {date}", ln=1)



    columns = (data.columns)
    columns = [item.replace('_', ' ').capitalize() for item in columns]
    pdf.set_font(family='Times', size=10, style='B')
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=40, h=8, txt=columns[1], border=1)
    pdf.cell(w=35, h=8, txt=columns[2], border=1)
    pdf.cell(w=25, h=8, txt=columns[3], border=1)
    pdf.cell(w=20, h=8, txt=columns[4], border=1, ln=1)
    #add tables
    for index, row in data.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=40, h=8, txt=str(row['product_name']), border=1)
        pdf.cell(w=35, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=25, h=8, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=20, h=8, txt=str(row['total_price']), border=1, ln=1)



    pdf.output(f"{filename}.pdf")






