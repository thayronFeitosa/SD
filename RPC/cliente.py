import Pyro4

# Cria um proxy para se conectar ao servidor Pyro
def main():
    calculadora = Pyro4.Proxy("PYRO:obj_c003de8b09c84ee4873f656bbc586723@localhost:31999")  # Substitua 'obj_123456' pelo URI do servidor
    resultado = calculadora.somar(85, 3)
    print("A soma é:", resultado)
    
    resultado = calculadora.subtrair(85, 3)
    print("A subtração é:", resultado)
    
    resultado = calculadora.multiplicar(85, 3)
    print("A multiplicação é:", resultado)


if __name__ == "__main__":
    main()
