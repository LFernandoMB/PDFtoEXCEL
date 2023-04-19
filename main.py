"""
import PyPDF2
import pandas as pd

# Abre o arquivo PDF
with open('arquivo.pdf', 'rb') as pdf_file:
    # Cria um objeto PDF Reader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Obtém o número de páginas do PDF
    num_pages = len(pdf_reader.pages)

    # Cria um objeto Excel Writer
    writer = pd.ExcelWriter('arquivo.xlsx', engine='xlsxwriter')

    # Itera sobre cada página do PDF
    for page_num in range(num_pages):
        # Extrai o texto da página
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Separa o texto em linhas
        lines = text.split('\n')

        # Adiciona as linhas à lista de dados
        data = []
        for line in lines:
            data.append(line.split())

        # Cria um DataFrame do pandas com os dados da página
        df = pd.DataFrame(data)

        # Salva o DataFrame em uma aba do Excel
        df.to_excel(writer, sheet_name=f'Página {page_num+1}', index=False)

    # Salva e Fecha o arquivo Excel
    writer.close()
"""

import PyPDF2
import pandas as pd

# Abre o arquivo PDF
with open('arquivo.pdf', 'rb') as pdf_file:
    # Cria um objeto PDF Reader
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Obtém o número de páginas do PDF
    num_pages = len(pdf_reader.pages)

    # Cria uma lista para armazenar os dados
    data = []

    # Itera sobre cada página do PDF
    for page_num in range(num_pages):
        # Extrai o texto da página
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        # Separa o texto em linhas
        lines = text.split('\n')

        # Adiciona as linhas à lista de dados
        for line in lines:
            data.append(line.split())

# Cria um DataFrame do pandas com os dados
df = pd.DataFrame(data)

# Salva o DataFrame em um arquivo Excel
df.to_excel('arquivo.xlsx', index=False)
