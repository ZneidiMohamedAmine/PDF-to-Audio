import pyttsx3
import PyPDF4 
from tkinter.filedialog import *

pdfname = askopenfilename()
reader = PyPDF4.PdfFileReader(pdfname)
Pages = reader.numPages

for num in range(0,Pages):
    page = reader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()

