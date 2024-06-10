Este é um projeto simples desenvolvido em Python que permite persistir informações sobre companhias abertas em um banco de dados SQL e consultar essas informações posteriormente. As informações são obtidas a partir de um conjunto de dados público disponível no [dados.gov.br](https://dados.gov.br/dados/conjuntos-dados/cias-abertas-informao-cadastral).

Como Executar Localmente
Para executar este projeto localmente, siga as instruções abaixo:

1. Configuração do Banco de Dados
O script database.py é responsável por configurar o banco de dados e criar a tabela necessária para armazenar as informações das companhias. Execute-o para criar o banco de dados SQLite e a tabela:

 -- python database.py

2. Inserção de Dados
O script insercao_dados.py realiza a inserção dos dados do arquivo CSV no banco de dados SQLite. Ja está nos arquivos o cad_cia_aberta.csv, ja com a edição das informações:


 -- python insercao_dados.py

3. Consulta de Dados
O script consultar_dados.py permite consultar informações das companhias com base no CNPJ e na data fornecida. Execute-o para realizar consultas ao banco de dados:


 -- python consultar_dados.py



Explicação das Decisões Tomadas

Banco de Dados: Utilizei o SQLite devido à sua simplicidade de configuração e portabilidade, sendo adequado para este projeto de escopo reduzido.
Persistência de Dados: Os dados das companhias são persistidos no banco de dados SQLite para permitir consultas futuras.
Consulta de Dados: Foi desenvolvida uma função que permite consultar informações das companhias com base no CNPJ e na data, retornando os dados relevantes.
Considerações Finais
Este projeto atende aos requisitos propostos, fornecendo uma solução simples e funcional para persistir e consultar informações sobre companhias abertas.

Melhorias:
Colocar a consulta dentro de um laço para que não seja necessario a execução constante