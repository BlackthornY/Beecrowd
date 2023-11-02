# BEE 1010 - Calculo simples de 2 itens

codigo1, qtd_peca1, valor_peca1 = input().split(" ")
codigo2, qtd_peca2, valor_peca2 = input().split(" ")


codigo1 =  int(codigo1)
qtd_peca1 = int(qtd_peca1)
valor_peca1 = float(valor_peca1)

codigo2 =  int(codigo2)
qtd_peca2 = int(qtd_peca2)
valor_peca2 = float(valor_peca2)

TOTAL = qtd_peca1*valor_peca1 + qtd_peca2*valor_peca2
print(f'VALOR A PAGAR: R$ {TOTAL:.2f}')