# Contrato - Linkedin (SOBRE)
contrato = input("Nome: Matheus\n"
      "Religião: Cristão\n"
      "Idade: 19 anos\n"
      "Localidade: Diadema- São Paulo\n"
      "Profissão: Estudante\n"
      "----------------------------------------------------------------------------------------------------------\n"
      "| Estudante de Ciência da computação, estou em busca do meu primeiro emprego, gosto de aprender coisas   |\n"
      "|novas e aprimorar minhas habilidades, acredito que pela faculdade isso seja auto explicativo... (rsrs) |\n"
      "|gosto de: TI, computação, programação e jogos.                                                          |\n"
      "----------------------------------------------------------------------------------------------------------\n"
      "Contratar? [Sim|Não]")

if contrato == "Sim":
    print("Meus Parabéns pelo novo funcionário incrível :3")
elif contrato == "Não":
    print("Esbarrou o dedo no botão errado? tente de novo...")
    contrato = input("Contratar? [Sim|Não]")
    print("Ok.\n"
          "Deus Abençoe!")
else:
    print("Usuários...")
    print("Esbarrou o dedo no botão errado? tente de novo...")
    contrato = input("Contratar? [Sim|Não]")
    print("Ok.\n"
          "Deus Abençoe!")
