import pandas as pd

# URL do CSV
url = "https://docs.google.com/spreadsheets/d/1Q2LlKm3mhAGglwnLBc9lfT_23wbgDF9sKy7L0pNCVMs/pub?output=csv"

# Ler o CSV diretamente do Google Sheets
df = pd.read_csv(url)

# Exibir os primeiros registros para verificar
email = df.values[0][1]
nome = df.values[0][2]
ultimo_nome = df.values[0][3]
numero = df.values[0][4]
genero = df.values[0][5]
experiencia = df.values[0][6]
tecnologia_usada = df.values[0][7]
internet = df.values[0][8]
recursos = df.values[0][9]
dados = [
    nome,
    ultimo_nome,
    numero, genero,
    email,
    experiencia,
    tecnologia_usada,
    internet,
    recursos,
    ]


print(dados)
