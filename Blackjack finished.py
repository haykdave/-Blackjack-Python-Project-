import random
values = ["8","K", "A",]
options = {"h":"Hit", "s":"Stand", "d":"Doubledown"}
options2 = {"h":"Hit", "s":"Stand"}
#suites = ["hearts", "diamonds", "clubs", "spades"]

def total_value(hand): #gör 2st
    k=0
    for card in hand:
        if card in ["K", "D", "J"]:
            k=k+10
        elif card == "A":
            k=k+11
        else:
            k= k + int(card)
    if ("A") in hand and k>21:
            k=k-10
    return k

def random_card():
    value= random.choice(values)
    #suit= random.choice(suites)
    return(value)

def add_card(hand):
    hand.append (random_card())
    

dealer=[random_card(),random_card()]
player=[random_card(), random_card()]

print()
print ("Dealer's hand: "f"{dealer[0]}  *")
print()
print ("Your hand:     "f"{player[0]}  {player[1]}")
print()

  
def menu(title, prompt, options):
    print(title)
    print()
    for key in options:
        print (f"{key}) {options[key]}")
    print()
    while True: 
        val = input(prompt)
        if val in options:
            print()
            if val==("h"):
                add_card(player)
                print(player)
                if total_value(player) > 21:
                    print("Bust, Dealer wins")
                    break
                else:
                    menu("Do you want to stand or take another card?", "Your choice: ", options2)
                    break
            elif val == "s":
                print("You chose to stand.")
                while total_value(dealer) < 17:
                    add_card(dealer)
                    print()
                    print("Dealers hand:")
                    print(dealer)
                if total_value(dealer) > 21 and total_value(player) < 21:
                    print("You win")
                    break
                elif total_value(dealer) <= 21 and total_value(dealer) > total_value(player):
                    print("Dealer wins")
                    break
                elif total_value(dealer) == total_value(player):
                    print("Push")
                    break
                else:
                    print("You win")
                    break
            else:
                val=="d"
                add_card(player)
                print("Players hand")
                print(player)
                while total_value(dealer) < 17:
                    add_card(dealer)
                    print()
                    print("Dealers hand:")
                    print(dealer)
                if total_value(dealer) > 21 and total_value(player) < 21:
                    print("You win")
                    break
                elif total_value(dealer) <= 21 and total_value(dealer) > total_value(player):
                    print("Dealer wins")
                    break
                elif total_value(dealer) == total_value(player):
                    print("Push")
                    break
                else:
                    print("You win")
                    break
        

                    
        
if total_value(player)==21:
    print("Blackjack")
    
if total_value(player)<21:
    menu("Choose an option","Your choice:", options)

