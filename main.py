liczby = [2, 10, 12, 114, 16, 7778, 98, 5]

wynik = map(lambda x: x * 2, liczby) #modyfikuje listę zgodnie z działaniem 1 arg czyli funkcji
print(list(wynik))

liczby_razy_dwa = [i * 2 for i in liczby]
print(liczby_razy_dwa)

wynik_filtr = filter(lambda x: x % 2 == 0, liczby) #obcina to co nie spełnia warunku
print(list(wynik_filtr))

liczby_podzielne_przez_dwa = [i for i in liczby if i % 2 == 0]
print(liczby_podzielne_przez_dwa)
