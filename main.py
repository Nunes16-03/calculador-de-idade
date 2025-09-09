ano = 2025 
nascimento = int(input("Digite o ano do seu nascimento: "))
idade = 0

while ano > nascimento:
    idade += 1
    nascimento += 1

print(f"Sua idade em {ano} é {idade} anos.")