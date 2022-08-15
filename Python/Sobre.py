# Linkedin (SOBRE)
contrato = input("""Nome: Matheus dos Santos Ferreira
Religião: Cristão
Idade: 20 anos 
Localidade: Diadema - São Paulo 
Profissão: Estudante
Linguagem preferida: Python
------------------------------------------------- ---------------------------------------------------------
| Estudante na aréa de TI com experiência em suporte técnico, programador Python,                         |
| aonde faço automação de tarefas e análise de dados. Analítico e organizado,                             |
| buscando aprender cada vez mais.                                                                        |
-----------------------------------------------------------------------------------------------------------
Contratar? [Sim|Não]:\n""").upper()

while contrato == "Sim" or "Não".upper():
    if contrato == "Sim".upper():
        print("Meus Parabéns pelo novo funcionário incrível!")
        break
    else:
        print("Usuários...\nEsbarrou o dedo no botão errado? tente de novo...")
        contrato = input("Contratar? [Sim|Não]:\n").upper()
        if contrato == "sim".upper():
            print("Que bom que acertou desta vez!")
        else:
            print("Ok. \nDeus Abençoe!")
            break
