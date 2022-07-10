from fpdf import FPDF

name = input("what is your name? ")

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=40)
pdf.cell(0,60,"CS50 Shirtificate",align = 'C')
pdf.image("shirtificate.png",15,60,180,200)
pdf.set_font("helvetica", size=20)
pdf.set_text_color(255,255,255)
#pdf.cell(0,0,f"{name} took CS50")
pdf.text(x=80, y=140, txt=f"{name} took CS50")
pdf.output('shirtificate.pdf')
