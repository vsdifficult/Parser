from bs4 import BeautifulSoup 
from core.headers import headers




import tkinter, requests

def get_link(url, element):  
     
    
     response = requests.get(url=url, headers=headers)  

     if response.status_code == 200: 
          bsf = BeautifulSoup(response.text, "html.parser")
          result = bsf.find_all(element) 
          print(result) 


if __name__ == "__main__": 
     get_link(url = ?, element=?)
    