para = 1
while para == 1 :
    n1 = float (input("digite o primeiro numero:"))
    n2 = float (input("digite o segundo numero:"))
    print("digite o operador")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0.sair")
    op = int (input())
    if op == 0:
        break
    def calc (n1, n2, op):
        if op == 1 :
            res = n1 + n2
        elif op == 2 :
            res = n1 - n2
        elif op == 3 :
            res = n1 * n2
        elif op == 4 :
            res = n1/n2
        elif op > 4 or op < 0:
            res = "essa função não existe"
        return res
    resultado = calc(n1,n2,op)
    
    print("o resultado é:", resultado)