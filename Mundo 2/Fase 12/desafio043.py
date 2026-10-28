# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:

# - Abaixo de 18.5:  Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
imc = peso / altura ** 2

if imc < 18.5:
    print(f'Seu IMC está em {imc:.2f}  você está abaixo do peso ideal.')
elif imc < 25:
    print(f'Seu IMC está em {imc:.2f} você está com peso ideal.')
elif imc < 30:
    print(f'Seu IMC está em {imc:.2f} você está com Sobrepeso.')
elif imc <= 40:
    print(f'Seu IMC está em {imc:.2f} você está com OBESO.')
else:
    print(f'Seu IMC está em {imc:.2f}, CUIDADO OBESIDADE MÒRBIDA.')