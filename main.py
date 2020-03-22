import datetime
import docx
from docx.shared import Pt

doc = docx.Document()
now = datetime.datetime.now()

# EZ Journal
date = now.strftime("%m-%d-%Y at %H:%M\n")
entry = input("Write a Journal Entry: ")

with open('journal.txt', 'r') as g:
    g_contents = g.read()
    full = g_contents + date + entry + "\n\n"

with open('journal.txt', 'w') as j:
    j.write(full)

doc.add_paragraph(full)
doc.save('new.docx')
        
    
        
        
    



