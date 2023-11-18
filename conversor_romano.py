def decimal_para_romano(numero):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

    resultado = ''
    i = 0

    while numero > 0:
        for _ in range(numero // valores[i]):
            resultado += simbolos[i]
            numero -= valores[i]

        i += 1

    return resultado

print(decimal_para_romano(999))

# abaixo será o codigo de conversão de romano para decimal.

def romano_para_decimal(romano):
    romano_valores = {'I': 1, 'IV' : 4, 'V': 5 ,'IX': 9, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    resultado = 0
    anterior = 0

    for letra in romano:
        valor = romano_valores[letra]
        resultado += valor

        if valor > anterior:
            resultado -= 2 * anterior
        anterior = valor

    return resultado

numero_romano = "MCMXCVIII"
decimal = romano_para_decimal(numero_romano)
print(f"O número romano {numero_romano} em decimal é: {decimal}")
