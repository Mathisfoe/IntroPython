totalsec = int(input("Insère un nombre de seconde : "))
heures = totalsec // 3600
restsec = totalsec % 3600
minutes = restsec // 60
sec = restsec % 60
print(f"{heures} heure, {minutes} minutes et {sec} seconde.")