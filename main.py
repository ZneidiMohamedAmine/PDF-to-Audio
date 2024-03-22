import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import *

pdfname = askopenfilename()
reader = PdfReader(pdfname)
Pages = reader.numPages

for num in range(0,Pages):
    page = reader.getPage(num)
    text = page.extractText()
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()

