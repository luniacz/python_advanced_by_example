import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as their names, their due amounts and the period of
    the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # add icon
        pdf.image('files/house.png', w=30, h=30)

        # insert tittle
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='The Flatmates Bill', border=0, align='C', ln=1)

        # insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=25, txt='Period: ', border=0)
        pdf.cell(w=150, h=25, txt=bill.period, border=0, ln=1)

        # insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=0, ln=1)

        # insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=0, ln=1)

        # change directory to generate and open pdf
        os.chdir('reports')
        pdf.output(self.filename)
        webbrowser.open(self.filename)
