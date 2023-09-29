# Adventure Game: Escape the Room

# Funktion för att starta spelet
def start_game():
    print("Välkommen till Escape the Room! Din uppgift är att fly från rummet.")
    choice = input("Vill du börja? (ja/nej) ")

    if choice.lower() == 'ja':
        room_one()
    else:
        print("Okej, kanske en annan gång!")

# Funktion för det första rummet
def room_one():
    print("\nDu är nu i rum ett.")
    items = ['nyckel', 'lampa']
    
    for item in items:
        print(f"Det finns en {item} här.")

    choice = input("\nVilket föremål vill du plocka upp? ")
    
    if choice.lower() in items:
        room_two(choice)
    else:
        print("Det föremålet finns inte. Försök igen.")
        room_one()

# Funktion för det andra rummet
def room_two(item):
    print(f"\nDu har nu {item} och är i rum två.")
    print("Du ser en dörr. Vill du använda din nyckel för att öppna den?")
    
    choice = input("(ja/nej) ")
    
    if choice.lower() == 'ja' and item == 'nyckel':
        print("Grattis, du har flytt rummet och vunnit spelet!")
    else:
        print("Tyvärr, du kan inte fly från rummet utan nyckeln. Du förlorar.")

# Starta spelet
start_game()
