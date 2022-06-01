liczby = [2, 10, 12, 114, 16, 7778, 98]

wynik = map(lambda x: x * 2, liczby)
print(list(wynik))

liczby_razy_dwa = [i * 2 for i in liczby]
print(liczby_razy_dwa)


