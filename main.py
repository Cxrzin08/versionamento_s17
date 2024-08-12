from pessoa2024 import Pessoa2024
from pessoa2023 import Pessoa2023

print("Olá, somos a equipe dos Power Rangers! Nós somos buxos e vamos descobrir sua data de nascimento.\n")

while True:
    resposta = input("Você fez aniversário esse ano?\nDigite [Sim] ou [Não]: ").capitalize()
    if resposta in ["Sim", "não", "nao", "Não", "não", "Nao", "NAo", "NAO", ]:
        break
    else:
        print("Opção inválida, digite apenas Sim ou Não")

if resposta == "Sim":
    Pessoa2024.ano1()
else:
    Pessoa2023.ano2()
