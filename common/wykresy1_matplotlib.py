import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,15,13,17,20]

# Wykres liniowy

plt.plot(x,y, color = "pink", linewidth = 2, marker = "o", markersize = 10, linestyle = "--")
plt.title("Wykres liniowy")
plt.xlabel("Numer dnia")
plt.ylabel("Wartość sprzedaży")
plt.grid(True)
plt.show()

# wykres słupkowy

# produkty = ["A","B","C","D"]
# wyniki = [12,19,7,15]
#
# plt.bar(produkty, wyniki)
# plt.barh(produkty, wyniki)
# plt.xlabel("Produkt")
# plt.ylabel("Wyniki")
#plt.show()

oceny = [2,2,5,5,4,3,2,5,4,3]
plt.hist(oceny, bins = 4)
plt.title("Histogram ocen")
plt.xlabel("ocena")
plt.ylabel("Liczba wystąpień")
plt.ylim([0,100])

plt.show()

# Wykres kołowy

etykiety = ["Python", "Java", "C++", "JS"]
wartosci = [40,25,15,20]
plt.pie(x = wartosci, labels = etykiety, autopct = lambda p: p)
# autopct ="%1.2f%%"
plt.show()

#Wykres punktowy
a = [1,2,3,4,5]
b =[3,7,4,9,6]

plt.scatter(x=a,y=b)
plt.show()

#Dwie linie na jednym wykresie
dni = [1,2,3,4,5]
sprzedaz =[10,12,15,14,18]
koszty=[6,7,8,7,9]

plt.plot(dni, sprzedaz, label="Sprzedaż")
plt.plot(dni, koszty, label="Koszty")
plt.title("Sprzedaż i koszty")
plt.xlabel("Numer dnia")
plt.ylabel("Kwoty")
plt.legend()
plt.show()

# zadanie 1
dni = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Nd"]
sprzedaz = [120, 150, 180, 160, 170, 210, 190]
plt.plot(dni, sprzedaz, marker = "o")
plt.title("Wykres liniowy")
plt.xlabel("Dni")
plt.ylabel("sprzeadaż")
plt.show()

# zadanie 2
produkty = ["Laptop", "Tablet", "Telefon", "Monitor"]
sprzedaz = [25, 18, 40, 12]
plt.bar(produkty, sprzedaz)
plt.title("Wykres słupkowy")
plt.xlabel("Produkty")
plt.ylabel("Sprzedaz")
plt.show()

# zadanie 3
wyniki = [45, 50, 52, 48, 60, 70, 65, 55, 58, 62, 75, 80, 78, 85, 90]
plt.hist(wyniki, edgecolor='black')
plt.xlabel('Wyniki testu')
plt.ylabel('Liczba studentów')
plt.title('Rozkład wyników testu studentów')
plt.show()