# Linkedin (SOBRE)
contrato = input("""Nome: Matheus dos Santos Ferreira
Religião: Cristão
Idade: 20 anos 
Localidade: Diadema- São Paulo 
Profissão: Estudante
Linguagem preferida: Python
------------------------------------------------- ---------------------------------------------------------
| Estudante da computação, estou em busca de estágio e mais experiência no mercado de trabalho,           |
| gosto de aprender coisas novas e aprimorar minhas habilidades                                           |
| gosto de: TI, programação e jogos. Atualmente estudando mais Back-End: Python                           |
-----------------------------------------------------------------------------------------------------------
Contratar? [Sim|Não]:\n""").upper()

while contrato == "Sim" or "Não".upper():
    if contrato == "Sim":
        print("Meus Parabéns pelo novo funcionário incrível!!!")
        break
    else:
        print("Usuários...\nEsbarrou o dedo no botão errado? tente de novo...")
        contrato = input("Contratar? [Sim|Não]").upper()
        if contrato == "Sim":
            print("Que bom que acertou desta vez! \nMeus Parabéns pelo novo funcionário incrível!")
        else:
            print("Ok. \nDeus Abençoe!")
            break
