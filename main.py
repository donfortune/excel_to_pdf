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

    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Invoice nr: {invoice_nr}", ln=1)


    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=f"Date: {date}")
    pdf.output(f"{filename}.pdf")





