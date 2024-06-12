from urllib.request import urlopen 

#nome = "\\interludio 1"
url = "https://parahumans.wordpress.com/2011/06/11/1-1/"
nome = "\\Guilherme" #nome vai vir da URL
formato =".txt"
path = "C:\\Users\\João Fernando Rangel\\Desktop\\Worm_WebScrapping\\TXTS_HTMLS"
#Criar arquivo csv com todas as urls
#Usar script para gerar o nome do arquivo de texto final
#Separar no HTML a parte que contém a 
#
arquivo = open(path+nome+formato, "w+", encoding="utf-8")
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
arquivo.write(html)
arquivo.close()
