# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# - Á vista dinheiro/pix/debíto: 10% de desconto
# - Á vista no crédito: 5% de desconto
# - 2 x no crédito sem juros
# - 3 x ou mais no crédito: 20% de juro

valor = float(input('Qual valor do produto? '))
for_pag = int(input('**Formas de pagamento**\n1 - Dinheiro/Pix/Debíto\n2 - Credito - Á Vista\n3 - Credito - até 2X\n4 - Credito - Acima de 3X\nEscolha a forma de pagamento: '))

if for_pag == 1:
    desc = valor * 0.10
    print(f'Valor a pagar: R$ {valor - desc:.2f}')
elif for_pag == 2:
    desc = valor * 0.05
    print(f'Valor a pagar: R$ {valor - desc:.2f}')
elif for_pag == 3:
    print(f'Valor a pagar: R$ {valor:.2f}')
    print(f'Valor da parcela: {valor / 2:.2f}')
elif for_pag == 4:
    juros = valor *0.20
    valor = valor + juros
    print(f'Valor a pagar: {valor:.2f}')
    parcela = int(input('Quantas parcelas?:'))
    if parcela >= 3:
        print(f'Valor das parcelas: {valor / parcela:.2f}')
    else:
        print('Quantidade de parcelas invalida!')
else:
    print('OPÇÃO INVALIDA')