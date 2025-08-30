num = input("Digite o número: ")

if len(num) == 8:
    num = "9" + num
elif len(num) == 9 and num[0] != "9":
    num = "9" + num[1:]

print("Número completo:", num[:5] + "-" + num[5:])
