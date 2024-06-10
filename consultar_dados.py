import sqlite3
from datetime import datetime

#Função para consultar informações das companhias
def informacoes_companhia(cnpj_cia):
    conn = sqlite3.connect('companies.db')
    cursor = conn.cursor()

#Sintax que realiza as consultas
    cursor.execute("""
        SELECT cnpj_cia, denom_social, 
        CASE
            WHEN data_cancelamento < ? THEN 'ATIVA'
            ELSE sit
        END AS sit, 
        data_registro, data_cancelamento FROM companies
        WHERE cnpj_cia = ?
        ORDER BY data_registro DESC
        LIMIT 1
    """, (data, cnpj_cia))

    result = cursor.fetchone()
    conn.close()

    if result:
        cnpj_cia, denom_social, sit, data_registro, data_cancelamento = result

# Verifica se data_registro é uma string ou um objeto datetime
        if isinstance(data_registro, str):
            data_registro_str = data_registro
        else:
            data_registro_str = data_registro.strftime('%d/%m/%Y')

#Verifica se data_cancelamento é uma string ou um objeto datetime
        if data_cancelamento:
            if isinstance(data_cancelamento, str):
                data_cancelamento_str = data_cancelamento
            else:
                data_cancelamento_str = data_cancelamento.strftime('%d/%m/%Y')
        else:
            data_cancelamento_str = None

        return {
            "cnpj_cia": cnpj_cia,
            "denom_social": denom_social,
            "sit": sit,
            "data_registro": data_registro_str,
            "data_cancelamento": data_cancelamento_str
        }
    else:
        return None
#Solicitação dos dados ao usuario
if __name__ == "__main__":
    cnpj = input("Digite o CNPJ da companhia: ")
    print("Digite a data desejada no formato DD/MM/YYYY")
    data = input("Caso vazio o mesmo trará a data de hoje: ")

    if not data:
        data = datetime.now().strftime('%d/%m/%Y')

#Retorno das informações solicitadas 
    info = informacoes_companhia(cnpj)
    if info:
        print(f"Informações da companhia em {data}:")
        print(f"CNPJ: {info['cnpj_cia']}")
        print(f"Denominação Social: {info['denom_social']}")
        print(f"Situação: {info['sit']}")
        print(f"Data de Registro: {info['data_registro']}")
        if info['data_cancelamento']:
            print(f"Data de Cancelamento: {info['data_cancelamento']}")
    else:
        print("Nenhuma informação encontrada para o CNPJ fornecido.")
