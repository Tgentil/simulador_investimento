"""Script para calcular o rendimento de um investimento."""
import sys
import locale
import pandas as pd
from prettytable import PrettyTable

# pylint: disable=line-too-long

# Definindo o locale para português brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# Definindo o encoding para UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Ajustando a largura máxima das colunas para 15
pd.set_option('display.max_colwidth', 15)

# Definindo as variáveis
APORTE = 1000
CDI = 0.1365
MESES = 120
TAXAS = [0.225, 0.20, 0.175, 0.15]
LIMITES = [12, 24, 36, 120]

"""
Taxas de imposto de renda:
Até 180 dias: 22,5%
De 181 a 360 dias: 20%
De 361 a 720 dias: 17,5%
Acima de 720 dias: 15%
"""

# Inicializando as listas
aportes = []
total_investido = []
rendimento_mes = []
montante_total = []

# Calculando os valores para cada mês
for i in range(1, MESES+1):
    aportes.append(APORTE)
    total_investido.append(sum(aportes))

    # Determinando a taxa de imposto de renda
    if i <= LIMITES[0]:
        TAXA = TAXAS[0]
    elif i <= LIMITES[1]:
        TAXA = TAXAS[1]
    elif i <= LIMITES[2]:
        TAXA = TAXAS[2]
    else:
        TAXA = TAXAS[3]

    # Calculando o rendimento do mês
    if i == 1:
        RENDIMENTO = APORTE * CDI * (1 - TAXA) / 12
        MONTANTE = APORTE + RENDIMENTO
    else:
        RENDIMENTO = MONTANTE * CDI * (1 - TAXA) / 12
        MONTANTE += APORTE + RENDIMENTO

    rendimento_mes.append(RENDIMENTO)
    montante_total.append(MONTANTE)

# Criando o DataFrame
df = pd.DataFrame({
    'Mês': range(1, MESES+1),
    'APORTE': aportes,
    'Total Investido': total_investido,
    'Rendimento do Mês': rendimento_mes,
    'Montante Total': montante_total
})

# Formatando as colunas numéricas para usar a vírgula como separador decimal
df['APORTE'] = df['APORTE'].map(
    lambda x: locale.format_string('%.2f', x, True))
df['Total Investido'] = df['Total Investido'].map(
    lambda x: locale.format_string('%.2f', x, True))
df['Rendimento do Mês'] = df['Rendimento do Mês'].map(
    lambda x: locale.format_string('%.2f', x, True))
df['Montante Total'] = df['Montante Total'].map(
    lambda x: locale.format_string('%.2f', x, True))

# Convertendo o DataFrame para um dicionário de listas
DATA = df.to_dict('records')


def print_table(finance_data):
    """
    Função para imprimir uma tabela de dados financeiros.

    Parâmetros:
    finance_data (list): Uma lista de dicionários onde cada dicionário representa um mês de dados financeiros.
                Cada dicionário deve conter as seguintes chaves: 'APORTE', 'Total Investido', 'Rendimento do Mês', 'Montante Total'.

    Retorna:
    None: A função imprime a tabela e não retorna nada.
    """
    table = PrettyTable(['Mês', 'Aporte', 'Total Investido',
                        'Rendimento do Mês', 'Montante Total'])
    for month_number, row in enumerate(finance_data, start=1):
        table.add_row([month_number, row['APORTE'], row['Total Investido'],
                        row['Rendimento do Mês'], row['Montante Total']])
    print(table)


# Imprimindo a tabela
print_table(DATA)
