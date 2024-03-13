numero = int(input("Digite um número inteiro: "))
print("Escolha uma das bases para conversão:")
print("[ 1 ] converter para BINÁRIO")
print("[ 2 ] converter para OCTAL")
print("[ 3 ] converter para HEXADECIMAL")
opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"{numero} convertido em Binário é igual a {bin(numero)[2:]}")
elif opcao == 2:
    print(f"{numero} convertido em Octal é igual a {oct(numero)[2:]}")
elif opcao == 3:
    print(f"{numero} convertido em Hexadecimal é igual a {hex(numero)[2:]}")
else:
    print("Número invalido, digite novamente.")
