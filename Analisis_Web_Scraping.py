#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Web Scraping from a web page.


# In[28]:


from selenium import webdriver


# In[29]:


from bs4 import BeautifulSoup as bs


# In[30]:


import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# In[31]:


from urllib.parse import urljoin


# ## Configuración

# In[32]:


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[33]:


titulosucio = []
preciosucio = []
stocksucio = []


# In[48]:


titulo = []
precio = []
stock = []


# In[35]:


driver.get("http://books.toscrape.com/")


# ## Extracción de Datos

# In[36]:


contenido = driver.page_source


# In[37]:


contenido


# In[38]:


soup = bs(contenido)


# In[39]:


soup


# Arma un for en el que vayas agregando a nuestras listas los datos necesarios con a.find, usa . append para ir agregando los datos a las listas

# In[44]:


soup.find_all("article", attrs={"class":"product_pod"})     


# In[45]:


#Armo el for (renglon de arriba)...
for libro in soup.find_all("article",attrs={"class":"product_pod"}):
    titulo = libro.find("h3")
    titulosucio.append(titulo.text)
    precio = libro.find("p", attrs={"class":"price_color"})
    preciosucio.append(precio.text)
    stock = libro.find("p", attrs={"class":"instock availability"})
    stocksucio.append(stock.text)


# In[46]:


titulosucio


# In[49]:


#for para limpiar titulosucio
for libro in titulosucio:
    titulo.append(libro.replace("\n","").strip())


# In[50]:


titulo


# Arma un for para limpiar precio

# In[52]:


#for para limpiar titulosucio
for libro in preciosucio:
    precio.append(libro.replace("\n","").strip())


# In[53]:


precio


# Arma un for para limpiar ubicación

# In[54]:


#for para limpiar titulosucio
for libro in stocksucio:
    stock.append(libro.replace("\n","").strip())


# In[55]:


stock


# ## Almacenamiento

# In[56]:


df = pd.DataFrame({"Titulo":titulo,"Precio":precio,"Stock":stock})


# In[57]:


df.head(20)


# In[59]:


df.to_csv("Libros.csv", index=False, encoding="utf8")


# In[71]:


#Ejemplo repetido aunque para las 50 paginas totales

from selenium import webdriver
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import pandas as pd

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

url = "http://books.toscrape.com"

titulosucio = []
preciosucio = []
stocksucio = []

titulo = []
precio = []
stock = []

while True:
    driver.get(url)
    contenido = driver.page_source
    soup = bs(contenido)
    for libro in soup.find_all("article", attrs={"class":"product_pod"}):
        titulo = libro.find("h3")
        titulosucio.append(titulo.text)
        precio = libro.find("p",attrs={"class":"price_color"})
        preciosucio.append(precio.text)
        stock = libro.find("p", attrs={"class":"instock availability"})
        stocksucio.append(stock.text)
        #for para limpiar titulosucio
    for libro in titulosucio:
        titulo.append(libro.replace("\n","").strip())
    for libro in preciosucio:
        precio.append(libro.replace("\n","").strip())
    for libro in stocksucio:
        stock.append(libro.replace("\n","").strip())
    #Paginacion
    siguientepag = soup.select_one("li.next>a")
    if siguientepag:
        siguienteurl = siguientepag.get("href")
        url = urljoin(url,siguienteurl)
    else:
        break

