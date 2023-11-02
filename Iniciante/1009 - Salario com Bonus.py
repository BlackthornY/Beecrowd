# BEE 1009 - Calculando salário com bônus

nome = str(input())
salario_fixo = float(input())
total_vendas_efetuadas = float(input())

comissao = total_vendas_efetuadas*0.15

salario_total = salario_fixo + comissao

print(f'TOTAL = R$ {salario_total:.2f}')