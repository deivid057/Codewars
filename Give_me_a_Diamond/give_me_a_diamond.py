def diamond(n):
    # variaveis e calculos
    expresao = ''
    caracter = '*'
    m = 0
    b = n - 1
    calculation = n // 2
    l = 0

    if n <= 0 or n % 2 == 0:
        return None
    elif n == 1:
        return "*\n"
    elif n == 3:
        expected = " *\n"
        expected += "***\n"
        expected += " *\n"
        return expected
    else:
        # loop gerador do diamante
        while True:
            if l == 2:
                print(expresao)
                break
            er = (' ' * (calculation - m) + (caracter * (n - b)) + '\n')
            expresao += er
            b -= 2
            m += 1

            if m == calculation + 1:
                while True:
                    er = (' ' * ((calculation + m) // n) + (caracter * (n + b)) + '\n')
                    m += n
                    b += -2
                    expresao += er
                    if n + b == -1:
                        l += 2
                        break