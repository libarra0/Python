def potencia(limit_pow):
    contador = 0
    value_pow = 2**contador
    while value_pow <= limit_pow:
        print(f'2 elevado a la {contador} es igual a {value_pow}')
        contador += 1
        value_pow = 2**contador


def run():
    limit_value = input("Por favor ingrese un numero limite para elevarlo: ")
    limit_value = int(limit_value)
    potencia(limit_value)


if __name__ == '__main__':
    run()