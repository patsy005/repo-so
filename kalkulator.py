def dodawanie(a,b):
	return a+b

def odejmowanie(a,b):
	return a-b

def mnozenie(a,b):
	return a*b

def dzielenie(a,b):
	if b != 0:
		return a/b
	else:
		return "Nie można dzielić przez 0"

def kalkulator():
	print("Dostepne operacje:")
	print("1. Dodawanie")
	print("2. Odejmowanie")
	print("3. Mnożenie")
	print("4. Dzielenie")

	wybor = input("Wybierz numer operacji")

	if wybor in ('1', '2', '3', '4'):
		a = float(input("Podaj pierwszą liczbę: "))
		b = float(input("Podaj drugą liczbę: "))

		if wybor == '1':
			wynik = dodawanie(a,b)
			print("Wynik dodawania: ", wynik)
		elif wybor == '2':
			wynik = odejmowanie(a,b)
			print("Wynij odejmowania: ", wynik)
		elif wybor == '3':
			wynik = mnozenie(a,b)
			print("Wynik mnożenia: ", wynik)
		elif wybor == '4':
			wynik = dzielenie(a,b)
			print("Wynik dzielenia: ", wynik)
	else:
		print("Niepoprawny wybór operacji")

kalkulator()
