#1. Wczytywanie danych prostych
plik = open('Dane.txt')

dane = plik.readlines()
print(dane)

for i in range(len(dane)):
    dane[i] = int(dane[i].strip())

print(dane)

#Wczytywanie danych prostych - wersja jednolinijkowa
dane2 = [int(x) for x in open('dane.txt').readlines()]
print(dane2)

#3. Wczytywanie danych prostych - wersja jednolinijkowa (z map)
dane3 = list(map(int, open('dane.txt').readlines()))
print(dane3)

#4. Wczytywanie danych zaawansowanych
plik = open('dane2.txt')
dane4 = plik.readlines()
print(dane4)

for i in range(len(dane4)):
    dane4[i] = dane4[i].split()

print(dane4)

for i in range(len(dane4)):
    dane4[i] = dane4[i].split()
    for j in range(2, 6):
        dane4[i][j] = int(dane[i][j])
print(dane4)