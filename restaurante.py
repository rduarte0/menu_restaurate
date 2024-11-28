"""Exibir um menu com 7 pratos, apresentando o código do prato e o nome .
O usuário poderá inserir o código do prato desejado. Caso o código seja inválido, o sistema deve alertar o usuário e pedir novamente um código válido.
O sistema deverá perguntar ao usuário se ele deseja fazer outro pedido e, se sim, permitir a adição de mais pratos ao pedido.
Acumule os valores de cada prato escolhido.
Se o usuário digitar o código "0", o programa encerrará o pedido e calculará o valor total.
O sistema deve solicitar uma forma de pagamento:
À vista (desconto de 10% sobre o valor total).
Cartão de crédito (acréscimo de 10% sobre o valor total).
Exibir os resultados ao final:
A lista com os códigos e nomes dos pratos escolhidos .
O subtotal (valor total sem acréscimo ou desconto).
A forma de pagamento escolhida.
O valor do desconto ou acréscimo aplicado.
O valor final a ser pago ."""

import os
os.system("cls||clear")

menu = {
    "1": ("Pizza", 25.00),
    "2": ("Hambúrguer", 20.00),
    "3": ("macarrão com carne", 30.00),
    "4": ("dogão duplo", 15.00),
    "5": ("macarrão com frango", 28.00),
    "6": ("espetinho", 22.00),
    "7": ("Lasanha", 24.00)
}


pedidos = []
total = 0

print("Bem-vindo ao nosso restaurante!")
print("Menu:")
for codigo, (nome, preco) in menu.items():
    print(f"{codigo}: {nome} - R${preco:.2f}")


while True:
    codigo_pedido = input("Insira o código do prato desejado (ou '0' para finalizar): ")
   
    if codigo_pedido == "0":
        break
    elif codigo_pedido in menu:
        nome, preco = menu[codigo_pedido]
        pedidos.append((nome, preco))
        total += preco
    else:
        print("Código inválido! Por favor, insira um código válido.")

    continuar = input("Deseja adicionar outro prato? (s/n): ").strip().lower()
    if continuar != 's':
        break


forma_pagamento = input("Escolha a forma de pagamento (1 - À vista, 2 - Cartão de crédito): ")

if forma_pagamento == "1":
    desconto = total * 0.10
    valor_final = total - desconto
    ajuste = -desconto
    forma_pagamento_nome = "À vista"
elif forma_pagamento == "2":
    acrescimo = total * 0.10
    valor_final = total + acrescimo
    ajuste = acrescimo
    forma_pagamento_nome = "Cartão de crédito"
else:
    print("Forma de pagamento inválida!")
    valor_final = total
    forma_pagamento_nome = "Indefinida"
    ajuste = 0

print("\n--- Resumo do Pedido ---")
print("Pratos escolhidos:")
for nome, preco in pedidos:
    print(f"- {nome}: R${preco:.2f}")
print(f"Subtotal: R${total:.2f}")
print(f"Forma de pagamento: {forma_pagamento_nome}")
if ajuste != 0:
    print(f"Ajuste: R${ajuste:.2f}")
print(f"Valor final a ser pago: R${valor_final:.2f}")