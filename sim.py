try:
    numero = int(input("Digite um numero: "))
    print("O numero digitado foi ",numero, ".")
except ValueError:
    print("Erro: por favor, digite um numero valido.")

while True:
    entrada = input("Digite 'sim' ou 'nao': ")
    if entrada.lower() in ('sim','nao'):
        break
    print("Entrada inválida. Tente novamente.")

print("Você digitou '", entrada,"'.")