def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir para cero")
    return a / b

def main():
    print("Aplicación ejercicio:3.0.0")
    print("Calculadora simple")
    print("Suma:", sumar(5, 3))
    print("Resta:", restar(5, 3))
    print("Multiplicación:", multiplicar(5, 3))
    print("División:", dividir(6, 2))

if __name__ == "__main__":
    main()