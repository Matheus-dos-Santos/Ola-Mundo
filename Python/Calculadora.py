# Calculadora
num1 = int(input("Digite um número: "))
equac = input("Escolha entre: [ + ou - ou * ou /]: ")
num2 = int(input("Digite um número: "))
# If's
if equac == "+":
    print(num1, "+", num2, "=", num1 + num2)
elif equac == "-":
    print(num1, "-", num2, "=", num1 - num2)
elif equac == "*":
    print(num1, "*", num2, "=", num1 * num2)
elif equac == "/":
    print(num1, "/", num2, "=", num1 / num2)
else:
    print("ERROR!")