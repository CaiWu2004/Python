"""2"""

uncommon = 5
rare = 15
reverse_holos = 10
holos = 15
full_holo = 20
starters = 5
legendaries = 30

start_price = 5

rarity = input("Welcome to the pokemon card price calculator! Is your card a special rarity?(Y/N)" )
if rarity == "Y":
    uc = input("Is your card an uncommon card?(Y/N)")
    if uc == "Y":
        start_price = start_price + uncommon
    else:
        rr = input("Is your card a rare card?(Y/N)" )
        if rr == "Y":
            start_price = start_price + rare
else:
    print("Your card is not a special rarity." )

holographic = input("Is your card a holographic card?(Y/N)")
if holographic == "Y":
    rev_holo = input("Is your card a reverse holographic card?(Y/N)" )
    if rev_holo == "Y":
        start_price = start_price + reverse_holos
    elif rev_holo == "N":
        holograph = input("Is your card a holo card?(Y/N)" )
        if holograph == "Y":
            start_price = start_price + holos
        elif holograph == "N":
            full_holographic = input("Is your card a full holo card?(Y/N)" )
            if full_holographic == "Y":
                start_price = start_price + full_holo
else:
    print("Your card is not a valid pokemon card.")

pokemon_race = input("Is your card of a special pokemon?(Y/N)" )
if pokemon_race == "Y":
    starter = input("Is your card a starter card?(Y/N)" )
    if starter == "Y":
        start_price = start_price + starters
    elif starter == "N":
        lega = input("Is your card a legendary card?(Y/N)" )
        if lega == "Y":
            start_price = start_price + legendaries
else:
    print("Your card is not a special pokemon card.")

print("Your card has a final resale price of:","$",start_price)

