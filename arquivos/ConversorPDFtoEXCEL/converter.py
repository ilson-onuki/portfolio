import tabula
import pandas as pd

def pdf_to_excel(pdf_path, excel_path):
    # Extrair dados do PDF para um DataFrame
    df = tabula.read_pdf(pdf_path, pages='all')

    # Concatenar todos os DataFrames
    combined_df = pd.concat(df)

    # Salvar o DataFrame em um arquivo Excel
    combined_df.to_excel(excel_path, index=False)

# Caminho do arquivo PDF de entrada
pdf_path = "files/teste_clientes.pdf"

# Caminho do arquivo Excel de saída
excel_path = "files/teste_clientes.xlsx"

# Chamar a função para converter PDF para Excel
pdf_to_excel(pdf_path, excel_path)

print("Conversão concluída. O arquivo Excel foi salvo em:", excel_path)
