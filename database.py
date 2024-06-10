import sqlite3

#Conexão ao banco(como o mesmo ainda não existe ira ser criado um arquivo .db)
conn = sqlite3.connect('companies.db')
cursor = conn.cursor()

#Criação do Banco de dados com as tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj_cia TEXT NOT NULL,
        denom_social TEXT NOT NULL,
        sit TEXT NOT NULL,
        data_registro DATE,
        data_cancelamento DATE
    );''')

#Criação do índice para otimização das consultas por CNPJ e data
cursor.execute('''
CREATE INDEX IF NOT EXISTS idx_cnpj_cia_data_registro ON companies (cnpj_cia, data_registro);
''')

#Salva e feche a conexão
conn.commit()
conn.close()

print("Banco de dados configurado com sucesso.")