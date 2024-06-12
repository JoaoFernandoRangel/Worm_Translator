from urllib.request import urlopen 
import csv
import time

inicio = time.time()

# Caminho para o arquivo CSV
path_to_csv = "C:\\Users\\João Fernando Rangel\\Desktop\\Worm_WebScrapping\\Worm_Translator\\Urls\\URLs.csv"

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

# Caminho para o arquivo de saída
output_path = "C:\\Users\\João Fernando Rangel\\Desktop\\Worm_WebScrapping\\Worm_Translator\\TXTS_HTMLS\\output.txt"

# Abre o arquivo de saída
with open(output_path, "w+", encoding="utf-8") as arquivo:
    for counter in URLS:
        page = urlopen(counter)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        arquivo.write(html)
        arquivo.write("\n\n")  # Adiciona uma quebra de linha entre cada HTML para clareza
        print(counter)

fim = time.time()
print(f"Tempo total: {fim-inicio} segundos")
