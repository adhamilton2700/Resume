import random

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f'{self.rank["rank"]} of {self.suit}'

class deck:
    def __init__(self):
        self.cards = []
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        ranks = [{"rank": "A", "value": 11},
                {"rank": "K", "value": 10},
                {"rank": "Q", "value": 10},
                {"rank": "J", "value": 10},
                {"rank": "10", "value": 10},
                {"rank": "9", "value": 9},
                {"rank": "8", "value": 8},
                {"rank": "7", "value": 7},
                {"rank": "6", "value": 6},
                {"rank": "5", "value": 5},
                {"rank": "4", "value": 4},
                {"rank": "3", "value": 3},
                {"rank": "2", "value": 2}]
        
        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit, rank))

    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    
    def deal(self, num):
        C_dealt = []
        for x in range(num):
            if len(self.cards) > 0:
                card = self.cards.pop()
                C_dealt.append(card)
        return C_dealt

class hand:
    def __init__(self, dealer =  False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, c_list):
        self.cards.extend(c_list)
    
    def calc_val(self):
        ace_count=0
        self.value = 0
        has_ace = False
        for c in self.cards:
            self.value += int(c.rank["value"])
            if c.rank["rank"] == "A":
                has_ace = True
                ace_count +=1
        if has_ace and self.value > 21:
            self.value -= (10*ace_count)
        
        return self.value
    
    def ret_val(self):
        self.calc_val()
        return self.value
    
    def blackjack(self):
        return (self.value == 21 and len(self.cards) == 2)
          
    def show(self, D_show_all = False):
        print(f'{"Dealer's" if self.dealer else "Your"} Hand:')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not D_show_all and not self.blackjack():
                print("hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value:",self.ret_val())
        print()

class game:
    def play(self):
        game_number = 0
        games_to_play = 0
        
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except:
                print("you must enter an integer number.")
        
        while game_number < games_to_play:
            game_number += 1
            deck1 = deck()
            deck1.shuffle()
            P_hand = hand()
            D_hand = hand(dealer=True)
        
            for i in range (2):
                P_hand.add_card(deck1.deal(1))
                D_hand.add_card(deck1.deal(1))
        
            print()
            print("*" * 30)
            print(f'Currently on Game:{game_number} of {games_to_play}')
            P_hand.show()
            D_hand.show()

            if self.winner(P_hand, D_hand):
                continue

            choice = ""

            while P_hand.ret_val() < 21 and choice not in ["s", "stand"]:
                choice = input("Would you like to 'hit' or 'stand'? enter H or S\n").lower()
                while choice not in ["h", "hit", "s", "stand"]:
                    choice = input("Would you like to 'hit' or 'stand'? enter H or S\n").lower()
                if choice in ["h", "hit"]:
                    P_hand.add_card(deck1.deal(1))
                    P_hand.show()

            if self.winner(P_hand, D_hand):
                continue

            P_hand_val = P_hand.ret_val()
            D_hand_val = D_hand.ret_val()

            while D_hand_val < 17:
                D_hand.add_card(deck1.deal(1))
                D_hand_val = D_hand.ret_val()
            
            D_hand.show(D_show_all=True)

            if self.winner(P_hand, D_hand):
                continue
            
            print("Final Result")
            print("Player hand:", P_hand_val)
            print("Dealer's hand:", D_hand_val)

            self.winner(P_hand, D_hand, game_over=True)

    def winner(self, P_hand, D_hand, game_over=False):
        if not game_over:
            if P_hand.ret_val() > 21:
                print("Busted. Dealer Win!")
                return True
            elif D_hand.ret_val() > 21:
                print("Dealer busted. You win!")
                return True
            elif P_hand.blackjack() and D_hand.blackjack():
                print("Player and Dealer both have blackjack. Push!")
                return True
            elif P_hand.blackjack():
                print("Blackjack. You win!")
                return True
            elif D_hand.blackjack():
                print("Dealer has Blackjack. You lose!")
                return True
        else:
            if P_hand.ret_val() > D_hand.ret_val():
                print("Congratulations! Player Wins!")
            elif D_hand.ret_val() > P_hand.ret_val():
                print("Dealer Wins!")
            elif P_hand.ret_val() == D_hand.ret_val():
                print("Push!")
            return True
        return False

g = game()
g.play()