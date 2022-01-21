cyclic_group = [] # Lista para guardar nuestro grupo ciclico
aux = [] # Lista para intercambiar valores
exponents = [] # Exponentes del grupo ciclico

def check_prime(num):
    flag = False

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    
    return flag

def dlp(p, a): 
    for x in range(p-1):
        aux.append(pow(a,(x+1),p))

    for x in range(p-1):
        cyclic_group.append(f'{a}^{aux.index(x+1)+1}')
        exponents.append(aux.index(x+1)+1)


def main(p, a, op):

    if op == '0':
        flag = check_prime(p)

        if flag:
            print(p, "no es primo")
        else: 
            dlp(p,a)
            print()
            print(aux)
            print(cyclic_group)
    elif op == '1':
        flag = check_prime(p)

        if flag:
            print(p, "no es primo")
        else: 
            dlp(p,a)
            print()
            x = input("buscar exponente>> ")
            if int(x) < int(p):
                print(f'el exponente es: {exponents.index(int(x))+1}')
            else:
                print("exit")
    else:
        print("exit")

p = input("ingrese la cantidad de 'p'>> ")
a = input("ingrese la cantidad de alfa>> ")
op = input("modo por defecto(0) modo buscar(1)>> ")

main(int(p), int(a), op)
