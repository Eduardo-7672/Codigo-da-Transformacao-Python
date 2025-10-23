'''
nomeclatura
PASCALCase
CamelCase
-> Snake_Case <-
Kebab-Case

Comentários, pode ser usados como apostrofos
ou cerquilhas
instruções, expressõesx exibições em tela.
'''

print ('Hello, World!')

nome_pessoa = str (input ("Qual o seu nome? "))
print(f"Olá, {nome_pessoa}. Que nome bonito o seu!! ")

import datetime

# Obtém a data e hora atuais
agora = datetime.datetime.now()

# Formata a data e hora para exibição
# %d - dia do mês
# %m - mês
# %Y - ano com 4 dígitos
# %H - hora (formato 24h)
# %M - minuto
# %S - segundo
data_hora_formatada = agora.strftime("%d/%m/%Y %H:%M:%S")

# Imprime o resultado
print(f"Seja bem vindo! Data e Hora Exatas: {data_hora_formatada}")
	
