from pessoa2024 import Pessoa2024
from pessoa2023 import Pessoa2023

print("Olá, somos a equipe dos Power Rangers! Nós somos buxos e vamos descobrir sua data de nascimento.\n")

while True:
    calculator2 = input("Você fez aniversário esse ano?\nDigite [Sim] ou [Não]: ")
    if calculator2 in ["Sim", "Não", "sim", "não", "nao", "Nao"]:
        break
    else:
        print("Opção inválida, digite apenas Sim ou Não")

if calculator2 == "Sim" or calculator2 == "sim":
    Pessoa2024.ano1()
elif calculator2 == "Não" or calculator2 == "não" or calculator2 == "Nao" or calculator2 == "nao":
    Pessoa2023.ano2()