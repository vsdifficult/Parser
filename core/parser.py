from bs4 import BeautifulSoup 
from headers import headers
from tkinter import *

import tkinter, requests

def get_link():  
     url = entry1.get()
     element = entry2.get()
     output.delete(0, END)
    
     response = requests.get(url=url, headers=headers)  

     if response.status_code == 200: 
          bsf = BeautifulSoup(response.text, "html.parser")
          result = bsf.find_all(element) 
          output.insert(END, result)

          with open("data/index.html", 'w', encoding="utf-8") as file_html: 
               file_html.write(str(response.text ))

          with open("data/parsing_result.txt", 'w', encoding="utf-8") as file_from_result: 
               file_from_result.write(str(result))    
window = Tk() 
window.geometry("450x450")  

window.resizable(False, False)
window.title("Parser by Difficult")

label1 = Label(window, text="URL:")
label1.pack()

entry1 = Entry(window)
entry1.pack()

label2 = Label(window, text="Element:")
label2.pack()


entry2 = Entry(window)
entry2.pack()

button = Button(window, text="Connect", command=get_link)
button.pack()

output = Entry(window, width=50)
output.pack()

window.mainloop()
