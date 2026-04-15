import pandas as pd
# import openpyxl

# Series

numbers = [10, 20, 30, 40]
ids = ["a", "b", "c", "d"]
# s = pd.Series(numbers)
s = pd.Series(numbers, index=ids)
print(s)
print(s["a"])

# DataFrame
data = [
    {
        "miasto":"Warszawa",
        "temperatura": 20,
    },
    {
        "miasto":"Kraków",
        "temperatura": 18
    }
]

# data = {
#     "miasto": ["Warszawa", "Kraków", "Gdańsk"],
#     "temperatura": [10, 20, 30]
# }

df = pd.DataFrame(data)
print(df)



# loc, iloc

a = df.loc[0]
b = df.loc[0, "miasto"]
c = df.loc[ df["temperatura"] >= 18]


# iloc

d = df.iloc[0]
e = df.iloc[0, 1]
f = df.iloc[0:2]
print(f)

g = df.head(1)
print(g)

h = df[["miasto", "temperatura"]]
print(h)

#Tworzenie nowej kolumny
df["temp_f"] = df["temperatura"] * 1.8 + 32
print(df)
# # Usuwanie kolumny
# test = df.drop("temp_f", axis=1)
# print(test)

df.to_csv("test.csv", index=False)
df.to_json("test.json")

df.to_excel("test.xlsx", index=False)

df.to_html("test.html")