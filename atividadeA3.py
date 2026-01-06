numero_secreto = 7
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    palpite = int(input("Adivinhe o número: "))
    tentativas += 1

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número 🎉")
        break
    else:
        print("Número incorreto. Tente novamente.")

else:
    print("Não foi dessa vez 😢 Suas tentativas acabaram.")