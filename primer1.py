pocetna_pozicija= 0
cilj = 80
# .
trenutna_pozicija= 0
brzina = 20

for x in range(10):
    if trenutna_pozicija == cilj:
        print("stigao do cilja.")
        break
    elif trenutna_pozicija > cilj:
        print("prosli ste")
    trenutna_pozicija += brzina