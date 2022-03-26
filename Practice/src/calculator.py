class Calculator:
# ejer 1
    def add(self, val1, val2):
        return val1 + val2
# ejer 2
    def valid_age(self, val):
        return 0 < val < 100
# ejer 3
    def max(self, val1, val2, val3):
        if val1 > val2 and val1 > val3:
            return val1
        elif val2 > val3:
            return val2
        else:
            return val3
# ejer 4
    def isVocal(self, val):
        if val == 'a' or val == 'e' or val == 'i' or val == 'o' or val == 'u':
            return 'vocal'
        elif val == 1 or val == 2 or val == 3 or val == 4 or val == 5 or val == 6 or val == 7 or val == 8 or val == 9 or val == 0:
            return 'numero'
        else:
            return 'consonante'
# ejer 5
    def inverse(self, val):
        return val[::-1]
# ejer 6
    def palindromo(self, val):
        if str(val) == str(val)[::-1]:
            return True
        else:
            return False
# ejer 7
    def mayorMenorPromedio(self, val):
        aux = []
        aux.insert(0, max(val))
        aux.insert(1, min(val))
        aux.insert(2, sum(val)/len(val))
        print(aux)
        return aux

# ejer 8
    def paises(self, val):
        auxM = 0
        for valor in val:
            if (len(valor) > auxM):
                auxM = len(valor)
                aux = valor
        return aux

# ejer 9
    def binario(self, val):
        numero_binario = 0
        multiplicador = 1
        while val != 0:
            numero_binario = numero_binario + val % 2 * multiplicador
            val //= 2
            multiplicador *= 10

        return numero_binario
# ejer 10
    def cantidad_caracteres(self, val):
        return len(val)




