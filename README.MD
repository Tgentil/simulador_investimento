# Rendimento de Investimento

[![GitHub](https://img.shields.io/badge/Visite-Meu%20Perfil-0891B2?style=flat-square&logo=github)](https://github.com/Tgentil)

Este é um script Python para fazer uma simulação hipotética e calcular o rendimento de um investimento dado um valor de aporte mensal e um percentual de rendimento (CDI). Ele também leva em consideração a taxa de imposto de renda que varia de acordo com o tempo de investimento.
>Os valores são meramente ilustrativos e hipoteticos e não levam em conta diversos fatores, não leve os valores a sério ou invista baseando-se nesse código 


## Requisitos

Para rodar este script, você precisa ter Python instalado em sua máquina, bem como as seguintes bibliotecas Python:

- pandas
- prettytable
- locale

## Como usar

Para usar este script, você pode simplesmente executá-lo em um terminal. Ele calcula o rendimento de um investimento para cada mês, levando em consideração o aporte mensal, o percentual de CDI, e a taxa de imposto de renda aplicável.

As variáveis `aporte`, `cdi`, `meses`, `taxas`, e `limites` são definidas no início do script. Você pode alterá-las de acordo com as suas necessidades. 

- `aporte`: é o valor que você vai investir a cada mês.
- `cdi`: é o percentual do CDI que o investimento rende.
- `meses`: é o número de meses que você vai investir.
- `taxas`: é uma lista das taxas de imposto de renda para diferentes períodos de tempo.
- `limites`: é uma lista dos limites de tempo (em meses) para cada taxa de imposto de renda.

Ao final da execução, o script imprime uma tabela que mostra o aporte, o total investido, o rendimento do mês, e o montante total para cada mês.

## Funções

O script contém uma função `print_table(finance_data)` que imprime uma tabela dos dados financeiros calculados. 

- `finance_data`: Uma lista de dicionários onde cada dicionário representa um mês de dados financeiros. Cada dicionário deve conter as seguintes chaves: 'APORTE', 'Total Investido', 'Rendimento do Mês', 'Montante Total'.

A função `print_table(finance_data)` imprime a tabela e não retorna nada.

## Autor

* Thiago da Silveira Gentil