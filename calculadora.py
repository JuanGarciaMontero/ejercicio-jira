# calculadora.py

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir por 0"
    else:
        return a / b

if __name__ == "__main__":
    print("Suma:", sumar(5, 3))
    print("Resta:", restar(5, 3))
    print("Multiplicación:", multiplicar(5, 3))
    print("División:", dividir(5, 3))
