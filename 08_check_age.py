birthday = int(input("Quel est ton année de naissance ? "))
age = 2026 - birthday
print(f"A la fin de l'année 2026, tu auras {age} ans!")
if age < 12 :
    print("Tu es un enfant")
elif age <= 12 and age >= 17:
    print("Tu es un adolescent")
else:
    print("Tu es un adulte")