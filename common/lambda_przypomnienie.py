# może być funkcją anonimową
liczby = [4,5,3,9]

def potegowanie(x):
    return x**2

zmapowane = map(potegowanie, liczby)
zmapowane2 = map(lambda x: x**2 if x > 5 else x, liczby)

fn1 = lambda a: f"witaj {a}"
fn1("Oliwia")
print(list(zmapowane))
print(list(zmapowane2))