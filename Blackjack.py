from random import randint

def card_deck():
    card_value=['Ace','2','3','4','5','6','7','8','9','J','Q','K']
    card_type=['Hearts','Spades','Clubs','Diamonds']
    deck=[]
    for i in card_type:
        for j in card_value:
            deck.append(j + ' of ' + i)
    return deck

def card_value(card):
    if card[:1] in ('J','Q','K','1'):
        return int(10)
    elif card[:1] in ('2','3','4','5','6','7','8','9'):
        return int(card[:1])
    elif card[:1] == 'A':
        print ("\n"+ str(card))
        num=raw_input("Do you want this to be 1 or 11?\n")
        while num!='1' or num!='11':
            if num=='1':
                return int(1)
            elif num=='11':
                return int(11)
            else:
                num=raw_input("Do you want this to be 1 or 11?\n")

def new_card(deck):
    return deck[randint(0,len(deck)-1)]

def remove_card(deck,card):
    return deck.remove(card)

play_again=' '
while play_again!='exit':
    print("\n\n**********WELCOME**********")

    new_deck=card_deck()
    card1=new_card(new_deck)
    remove_card(new_deck,card1)
    card2=new_card(new_deck)
    remove_card(new_deck,card2)
    val1=card_value(card1)
    val2=card_value(card2)
    total=val1+val2
    print("\n"+card1+" and "+card2+" with a total of "+str(total))

    dealer_card1 = new_card(new_deck)
    remove_card(new_deck,dealer_card1)
    dealer_card2 = new_card(new_deck)
    remove_card(new_deck,dealer_card2)
    dealer_value1 = card_value(dealer_card1)
    dealer_value2 = card_value(dealer_card2)
    dealer_total = dealer_value1 + dealer_value2
    print ('\nThe Dealer smiles as he looks at you and\ndeals one card up and one card face down.\n')
    print ("First a " + dealer_card1 + " and face down card.\n")

    if total==21:
        print("BLACK JACK! YOU WON!")
    else:
        while total<21:
            ans= raw_input("Would you like to hit or stand?\n>")
            if ans.lower()=='hit':
                more_card = new_card(new_deck)
                remove_card(new_deck,more_card)
                more_value = card_value(more_card)
                total += int(more_value)
                print ("\n"+more_card + " for a new total of " + str(total)+"\n")
                if total>21:
                    print("YOU LOSE!!!")
                    play_again= raw_input("Would you like to continue? Type EXIT to leave.\n")
                elif total == 21:
                    print("YOU WIN!!!")
                    play_again = raw_input("Would you like to continue? EXIT to leave\n")
                else:
                    continue
            elif ans.lower()=='stand':
                print("\nThe dealer nods and reveals his other card to be ")
                print("a " + dealer_card2 + " for a total of " + str(dealer_total)+"\n")
                if dealer_total < 17:
                    print("The Dealer hits again.\n")
                    dealer_more = new_card(new_deck)
                    more_dealer_value = card_value(dealer_more)
                    print("The card is a " + str(dealer_more)+"\n")
                    dealer_total += int(more_dealer_value)
                    if dealer_total > 21 and total <=21:
                        print("Dealer Bust! You win!\n")
                    elif dealer_total < 21 and dealer_total > total:
                        print("Dealer has " + str(dealer_total) + " you lose!\n")
                    else:
                        continue
                elif dealer_total == total:
                    print("Equal Deals, no winner")
                elif dealer_total < total:
                    print("YOU WIN!!!")
                else:
                    print("YOU LOSE!!!")
                play_again = raw_input("\nWould you like to continue? EXIT to leave!\n")
                break
print("\nTHANK YOU FOR PLAYING!!")
            
