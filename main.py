import pyttsx3
import PyPDF2
book = open('iot.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(2)
text = page.extraText()
speaker.say(text)
speaker.runAndWait()
