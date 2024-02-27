primeiro = int(input("Primeiro valo:"))
segundo = int(input("Segundo valor:"))
terceiro = int(input("Terceiro valor:"))
# calculando o maior valor
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
# calculando o menor valor
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro

print(f"O menor valor digitado foi {menor}")
print(f"O maior valor digitado foi {maior}")
