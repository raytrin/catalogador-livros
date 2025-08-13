# 📚 Catalogador de Livros para Google Sheets

Este projeto lê uma lista de livros a partir de um arquivo CSV e envia os dados diretamente para uma planilha no Google Sheets.  
O objetivo é automatizar a catalogação de títulos, autores e editoras, evitando preenchimento manual.

---

## 🚀 Funcionalidades
- Leitura de dados de um arquivo CSV.
- Preenchimento automático de valores ausentes.
- Envio dos dados para uma planilha no Google Sheets.
- Tratamento para evitar valores incompatíveis com JSON (`NaN`).

---

## 🛠️ Tecnologias Utilizadas
- [Python 3.12+](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [gspread](https://docs.gspread.org/en/latest/)
- [oauth2client](https://pypi.org/project/oauth2client/)

---

## 📂 Estrutura do Projeto
```
.
├── main.py                         # Script principal
├── livros_com_autores_editoras.csv # Base de dados dos livros
├── credenciais.json                # Credenciais da API do Google 
├── requirements.txt                # Dependências do projeto
└── .gitignore
```
---

## ⚙️ Como Usar

### 1️⃣ Criar e ativar um ambiente virtual
```
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 2️⃣ Instalar as dependências
```
pip install -r requirements.txt
```
### 3️⃣ Configurar as credenciais do Google

- Acesse Google Cloud Console.
- Ative a API do Google Sheets e Google Drive.
- Gere uma chave do tipo Service Account e baixe o arquivo credenciais.json.
- Coloque o credenciais.json na raiz do projeto.

### 4️⃣ Criar a planilha no Google Sheets

- Crie uma planilha no Google Sheets e utilize esse mesmo nome no 'client.open("Nome da sua planilha")'.
- Compartilhe a planilha com o e-mail do seu Service Account (presente no credenciais.json).

### 5️⃣ Executar o script
```
python main.py

#Se tudo estiver correto, a saída será:
#Dados atualizados com sucesso!
```
### 📌 Observações

- O arquivo credenciais.json está no .gitignore e não deve ser enviado para repositórios públicos.
- O CSV precisa estar no formato: Título, Autor, Editora.
- A planilha deve existir e estar compartilhada com o e-mail do Service Account.
