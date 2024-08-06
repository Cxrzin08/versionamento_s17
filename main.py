from pessoa import Pessoa

print("0lá somos a equipe dos power ranger nós somos buxos e vamos descobrir sua data de nacimento.")


calculator2 = input("Voce fez aniversario esse ano?\nDigite sua resposta:").capitalize


if calculator2 == "Sim":
    Pessoa.ano1()
elif calculator2 == "Não":
    Pessoa.ano2()
