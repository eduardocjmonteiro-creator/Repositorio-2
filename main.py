import random, time

n_v = int(input("Digite o númro de repetições: "))

print("Iniciando em 3 segundos...")
time.sleep(3)

def rept():
    n = 0
    c = 0

    while True:
        print(random.randint(0,9) + n)
        n += 1 * random.randint(0,9)
        time.sleep(0.01)
        c += 1
        if n > 100:
            break

    print("Limite de 100 ultrapassado")
    print(f"Número de repetições: {c}.")
    print("\n\n")

for i in range(n_v):
    rept()

print("\n\n________________________")
print("Finalizado")