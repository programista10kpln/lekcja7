liczby = [2, 10, 12, 114, 16, 7778, 98, 5]

wynik = map(lambda x: x * 2, liczby)  # modyfikuje listę zgodnie z działaniem 1 arg czyli funkcji
print(list(wynik))

liczby_razy_dwa = [i * 2 for i in liczby]
print(liczby_razy_dwa)

wynik_filtr = filter(lambda x: x % 2 == 0, liczby)  # obcina to co nie spełnia warunku
print(list(wynik_filtr))

liczby_podzielne_przez_dwa = [i for i in liczby if i % 2 == 0]
print(liczby_podzielne_przez_dwa)

# generatory - yield
print('\n')


def generator():
    i = 0
    while i < 9:
        yield i
        i += 1


print(list(generator()))
print('\n')


def generator_parzystych(n):  # sposob z yield
    i = 0
    while i < n:
        if i % 2 == 0:
            yield i
        i += 1


print(list(generator_parzystych(15)))

def generator_parzystych2(n): #sposob z list expression
    output = []
    for i in range(0, n):
        if i % 2 == 0:
            output.append(i)
    return output

print(generator_parzystych2(15))