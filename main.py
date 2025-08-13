import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

df = pd.read_csv("livros_com_autores_editoras.csv")
df.columns = ["Título", "Autor", "Editora"]

#----------------------------------------- google sheets ----------------------------------------
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credenciais = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', scope)
cliente = gspread.authorize(credenciais)

spreadsheet = cliente.open('Livros Bienal - 2025').sheet1
df = df.fillna("")
spreadsheet.update([df.columns.values.tolist()] + df.values.tolist())

print("Dados atualizados com sucesso!")