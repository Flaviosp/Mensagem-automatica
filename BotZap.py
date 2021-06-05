#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
#caminho para aquivo com dados do telefone
contato = pd.read_excel(r'C:\Users\')
display(contato)
                 


# In[65]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib


navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")
texto = urllib.parse.quote('Ola tudo bom? Meu nome é Flavio e somos representante do moinho Canuelas, atuamos na região de Sorocaba e agora estamos expandindo a região....Gostaria de estar fazendo o seu cadastro para que possamos no futuro sermos parceiros')

while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)

for i, Telefone in enumerate(contato['Telefone']):
    numero = contato.loc[i, "Telefone"]
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath ('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)   
    time.sleep(15)
    
    


# In[ ]:




