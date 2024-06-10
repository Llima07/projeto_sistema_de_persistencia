import sqlite3
import csv

#Arquivo local
arquivo_csv = 'cad_cia_aberta.csv'

#Criação da função que ira processar os dados
def processamento_dados(file_path):

    #Conexão com o banco.
    conn = sqlite3.connect('companies.db')
    cursor = conn.cursor()

    #Abertura do arquivo
    with open(file_path, mode='r', encoding='latin1') as file:
        leitor = csv.DictReader(file)

    #Loop para adição dos dados no banco
        for linha in leitor:
            cnpj_cia = linha['CNPJ_CIA']
            demon_social = linha['DENOM_SOCIAL']
            sit = linha['SIT']
            data_registro = linha['DT_REG']
            data_cancelamento = linha['DT_CANCEL']

            cursor.execute("INSERT INTO companies(cnpj_cia, denom_social, sit, data_registro, data_cancelamento) VALUES (?, ?, ?, ?, ?)", 
                (cnpj_cia, demon_social, sit, data_registro, data_cancelamento))

    #Comit dos dados 
    conn.commit()
    conn.close()

#chamada da função
processamento_dados(arquivo_csv)

print('Dados inseridos com sucesso!')