from fpdf import FPDF
# 12pt = 16 pixels
pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

# Add text
pdf.set_font(family="Times", size=24, style="B")
pdf.cell(w=250, h=80, txt="Flatmates Bill", border=1, align='C', ln=2)
pdf.cell(w=100, h=40, txt="Period", border=1)
pdf.cell(w=150, h=40, txt="March 2021", border=1)
pdf.output("bill.pdf")
