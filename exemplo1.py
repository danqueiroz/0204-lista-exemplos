def somar(valor1, valor2):
    resultado = valor1 + valor2
    return resultado

valor_1 = round(float(input("Digite o primeiro número: ")), 2)
valor_2 = round(float(input("Digite o segundo número: ")), 2)

resultado_soma = somar(valor1=valor_1, valor2=valor_2)

if resultado_soma > 40:
    print("A soma dos valores é", resultado_soma)
else:
    print("Ops, só retorno valores acima de 40")