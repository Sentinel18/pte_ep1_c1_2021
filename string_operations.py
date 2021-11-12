str1 = "Az almafán almák teremnek."
print("A szöveg hossza:", len(str1))
print(type(len(str1)))
str2 = "terem"
print(str1.find(str2)) #visszaadja a pozicióját ahol elkezdődik a keresett string   figyeli hogy nagybetű vagy kisbetű
lower_str1 = str1.lower()
print(str1)
print(lower_str1)
print(str1.upper())
print("------")
print(lower_str1.islower()) #visszaadja hogy milyen betű kisbetű
print(lower_str1.isupper())
print(str1.isupper())
print(str2.isalpha())
print(str2.isalpha())
print(str2.isalnum())
str3 = "user12"
print(str3.isalpha())
print(str3.isalnum())