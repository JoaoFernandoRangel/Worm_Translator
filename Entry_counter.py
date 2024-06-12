from urllib.request import urlopen 
import csv

# Caminho para o arquivo CSV
path_to_csv = "C:\\Users\\João Fernando Rangel\\Desktop\\Worm_WebScrapping\\Urls\\URLs.csv"
# Lista para armazenar as URLs
URLS = []
# Abre o arquivo CSV
with open(path_to_csv, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Para iterar sobre cada linha do CSV
    for row_number, row in enumerate(csv_reader, start=1):
        # Verifica se a linha não está vazia
        if row:
            # Lê a célula (n, 1) e adiciona à lista URLS
            cell_value = row[0]  # O índice 0 corresponde à primeira célula (n, 1)
            URLS.append(cell_value)

# Imprime a lista URLS para verificar
