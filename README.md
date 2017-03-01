Escreva um crawler que visite o site [epocacosmeticos.com.br](http://www.epocacosmeticos.com.br/) e salve um arquivo .csv com o nome do produto, o título e a url de cada página de produto[1] encontrada. Regras:

  * Esse arquivo não deve conter entradas duplicadas;
  * Não é permitido usar o sitemap para pegar todas as urls do site; o site deve de fato ser visitado e parseado para se obter as informações.
  * Exceto pelo Scrapy, você pode usar os frameworks e bibliotecas que quiser, desde que a linguagem principal usada seja Python (2.7, 3.x, PyPy... tanto faz).

Desenvolva seu código em um local público adicione um arquivo README ou INSTALL explicando como instalar e rodar o programa.

Obrigatório:

  * Testes unitários automatizados. Escrever testes faz parte de nossa cultura.
  * Respeite a PEP8, mas não precisa ser xiita.
  * Código organizado. Responsabilidade única, nomes (funções, variáveis, arquivos) que fazem sentido etc.

Bônus:

  * Arquitetura distribuída.

Responda às seguintes questões de forma discursiva:

  * Agora você tem de capturar dados de outros 100 sites. Quais seriam suas estratégias para escalar a aplicação?
  * Alguns sites carregam o preço através de JavaScript. Como faria para capturar esse valor.
  * Alguns sites podem bloquear a captura por interpretar seus acessos como um ataque DDOS. Como lidaria com essa situação?
  * Um cliente liga reclamando que está fazendo muitos acessos ao seu site e aumentando seus custos com infra. Como resolveria esse problema?

[1] Uma página de produto é a que contém as informações (nome, preço, disponibilidade, descrição etc.) de apenas um produto. Home page, páginas de busca ou categoria não são consideradas páginas de produto.

Exemplo:

É página de produto: http://www.epocacosmeticos.com.br/hypnose-eau-de-toilette-lancome-perfume-feminino/p  
**NÃO** é página de produto: http://www.epocacosmeticos.com.br/cabelos

## IPC
Levamos **MUITO** a sério código limpo e organizado. Nossa dica é: Olhe um código que tenha escrito a menos de um mês e reflita. Sinto-me orgulhoso por ter escrito essas linhas de código? Se a resposta for _não_, considere a possibilidade de se atualizar antes de entregar o desafio. Os livros a seguir podem ajudar nessa jornada:

* [Código Limpo. Habilidades Práticas Do Agile Software](https://www.amazon.com.br/C%C3%B3digo-Limpo-Habilidades-Pr%C3%A1ticas-Software/dp/8576082675)
* [Refactoring: Improving the Design of Existing Code](https://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672)
* [TDD. Desenvolvimento Guiado por Testes](https://www.amazon.com.br/TDD-Desenvolvimento-Guiado-por-Testes/dp/857780724X)
* [O Programador Pragmático: De Aprendiz a Mestre](https://www.amazon.com/Programador-Pragm%C3%A1tico-Aprendiz-Mestre-Portuguese-ebook/dp/B019HM0H90)
* [O Codificador Limpo](https://www.amazon.com.br/O-Codificador-Limpo-Bob-Martin/dp/8576086476)
* [Practices of an Agile Developer: Working in the Real World](https://www.amazon.com/Practices-Agile-Developer-Pragmatic-Bookshelf/dp/097451408X)

Bad smells muito comuns que vemos em nossos desafios:

* Código duplicado.
* Código sem testes automatizados.
* Funções/métodos longos (mais de 10 linhas).
* Classes muito longas (mais de 20 métodos).
* Muitos if/else.
* Uso de estruturas de dados inadequadas. `for barcode in {12345}:` por exemplo.
* Funções/métodos com muitos parâmetros (mais de 3).
* `print`, `import ipdb`... Use esse [_hook pre-commit_](https://gist.github.com/eduardo-matos/8555eb3d6511dff5eed9). Sério!
* Retornar estado de erro em vez de levantar exceção.
* Não prover instruções de instalação (readme, makefile...). Quem faz com Docker ganha uma barra de chocolate!