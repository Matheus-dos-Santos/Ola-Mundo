# Contrato - Linkedin (SOBRE)
contrato = input("""Nome: Matheus dos Santos Ferreira
Religião: Cristão
Idade: 20 anos 
Localidade: Diadema- São Paulo 
Profissão: Estudante
Linguagem preferida: Python
------------------------------------------------- ---------------------------------------------------------
| Estudante da computação, estou em busca de estágio e mais experiência no mercado de trabalho,           |
| gosto de aprender coisas novas e aprimorar minhas habilidades.                                          |
| gosto de: TI, programação, programação e jogos. Atualmente estudando mais Back-End: Python              |
------------------------------------------------- ---------------------------------------------------------
Contratar? [Sim|Não]""").upper()

if contrato == "SIM":
    print("Meus Parabéns pelo novo funcionário incrível!!!")

else:
    print("Usuários... \n"
        "Esbarrou o dedo no botão errado? tente de novo...")
    contrato  =  input ( "Contratar? [Sim|Não]" ).upper()
    if  contrato  ==  "SIM":
        print ( "Que bom que acertou desta vez! \n "
            "Meus Parabéns pelo novo funcionário incrível!!!" )
    else:
        print ( "Ok. \n "
            "Deus Abençoe!")
