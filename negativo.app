AtivA = int(input("Informe os dias para a atividade A: "))
AtivB = int(input("Informe os dias para a atividade B: "))
AtivC = int(input("Informe os dias para a atividade C: "))

if AtivA < 0 or AtivB < 0 or AtivC < 0:
    print("ERRO: Os dias não podem ser negativos.")
else:
    resultado = AtivA + AtivB + AtivC
    print(f"O total de dias é {resultado}")
