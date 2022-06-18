# Contrato - Linkedin (SOBRE)
contrato = input("Nome: Matheus\n"
 "Religião: Cristão\n"
 "Idade: 20 anos\n"
 "Localidade: Diadema- São Paulo\n"
 "Profissão: Estudante\n"
 "----------------------------------------------------------------------------------------------------------\n"
 "| Estudante de Ciência da computação, estou em busca de estágio e mais experiência no mercado de trabalho,|\n"
 "| gosto de aprender coisas novas e aprimorar minhas habilidades.                                          |\n"
 "| gosto de: TI, computação, programação e jogos. Atualmente estudando mais Back-End: Python               |\n"
 "----------------------------------------------------------------------------------------------------------\n"
 "Contratar? [Sim|Não]").upper()

if contrato == "SIM":
 print("Meus Parabéns pelo novo funcionário incrível!!!")

else:
 print("Usuários...\n"
 "Esbarrou o dedo no botão errado? tente de novo...")
 contrato = input("Contratar? [Sim|Não]").upper()
 if contrato == "SIM":
  print("Que bom que acertou desta vez!\n"
        "Meus Parabéns pelo novo funcionário incrível!!!")
 else:
  print("Ok.\n"
  "Deus Abençoe!")
