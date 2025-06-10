import matplotlib.pyplot as plt
from fpdf import FPDF
import Gemini_ask
import os

# file_path = r'/Users/shripad/Documents/Developer/Projects/Project-1-Email Report Generator/test.xlsx'
# obj = data_utils.get_excelData(file_path)

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Monthly Financial Report - May 2025', ln=True, align='C')
        self.ln(10)

    def add_summary(self, text):
        self.set_font('Arial', '', 12)
        self.cell(0, 10, text, ln=True)
        self.ln(10)

    def add_category_table(self, category_data):
        self.set_font('Arial', 'B', 12)
        self.cell(60, 10, 'Category', 1)
        self.cell(60, 10, 'Total Amount', 1)
        self.ln()
        self.set_font('Arial', '', 12)
        for category, amount in category_data.items():
            self.cell(60, 10, category, 1)
            self.cell(60, 10, f"Rs. {amount}", 1)
            self.ln()
        self.ln(10)

    def add_chart(self, chart_path):
        self.image(chart_path, x=30, w=150)

def generate_pdf(obj):
    pdf = PDFReport()
    pdf.add_page()
    prompt = f'''
    Generate a concise summary based on this data, total income: {obj.totalIncome}, total expenses: {obj.totalExpenses}, net balance: {obj.netBalance}, category and respective amounts are mapped as follows: {obj.cat_amt}, these are category types: {obj.categoryType}.
    '''
    text = Gemini_ask.ask_gemini(prompt)
    pdf.add_summary(text)
    pdf.add_category_table(obj.cat_amt)
    pdf.add_chart(r'monthly_report.png')
    os.remove(r'monthly_report.png')
    pdf.output('monthly_report.pdf')