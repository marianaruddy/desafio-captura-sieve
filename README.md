Escreva um crawler que visite o site [epocacosmeticos.com.br](http://www.epocacosmeticos.com.br/) e salve um arquivo .csv com o nome do produto, o título e a url de cada página de produto[1] encontrada. Regras:

  * Esse arquivo não deve conter entradas duplicadas;
  * Não é permitido usar o sitemap para pegar todas as urls do site; o site deve de fato ser visitado e parseado para se obter as informações.
  * Exceto pelo Scrapy, você pode usar os frameworks e bibliotecas que quiser, desde que a linguagem principal usada seja Python (2.7, 3.x, PyPy... tanto faz).

Desenvolva seu código em um local público adicione um arquivo README ou INSTALL explicando como instalar e rodar o programa.

Obrigatório:

  * Testes automatizados. Se não tiver, nem precisa entregar o desafio.
  * Respeite a PEP8, mas não precisa ser xiita.
  * Código organizado. Responsabilidade única, nomes (funções, variáveis, arquivos) que fazem sentido etc.
  
Bônus:
  * Arquitetura distribuída.

[1] Uma página de produto é a que contém as informações (nome, preço, disponibilidade, descrição etc.) de apenas um produto. Home page, páginas de busca ou categoria não são consideradas páginas de produto. 

Exemplo:
 
É página de produto: http://www.epocacosmeticos.com.br/hypnose-eau-de-toilette-lancome-perfume-feminino/p  
**NÃO** é página de produto: http://www.epocacosmeticos.com.br/cabelos

