import pyttsx3
from pypdf import PdfReader

reade=PdfReader(r'C:\Users\SUBHRADIP\OneDrive\Desktop\P lnag\My python\Case Study.pdf')
page=reade.pages[1]
text=page.extract_text()

speak=pyttsx3.init()
speak.say(text)
speak.runAndWait()
