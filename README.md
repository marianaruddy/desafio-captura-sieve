Escreva um crawler que visite o site epocacosmeticos.com.br e salve um arquivo .csv com o nome do produto, o título e a url de cada página de produto[1] encontrada; esse arquivo não deve conter entradas duplicadas.

Não é permitido usar o sitemap para pegar todas as urls do site; o site deve de fato ser visitado e parseado para se obter as informações.

Exceto pelo Scrapy, você pode usar os frameworks e bibliotecas que quiser, desde que a linguagem principal usada seja Python (2.7 ou 3.x, tanto faz).

Desenvolva se código nesse repositório e adicione um arquivo INSTALL.txt explicando como instalar e rodar o programa.

Bonus:
    - Testes unitários;
    - Arquitetura paralela ou distribuida.


[1] Uma página de produto é a que contém as informações (nome, preço, disponibilidade, descrição etc.) de apenas um produto. Home page, páginas de busca ou categoria não são consideradas páginas de produto. 

Exemplo:
 
É página de produto:
http://www.epocacosmeticos.com.br/hypnose-eau-de-toilette-lancome-perfume-feminino/p
NÃO é página de produto: http://www.epocacosmeticos.com.br/cabelos

