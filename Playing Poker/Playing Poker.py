import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        
    def draw(self, deck):
        self.hand.append(deck.drawCard())
    
    def showHand(self):
        print (self.hand)
    
    def dealHand(self, other, deck, handSize):
        for i in range(handSize):
            self.draw(deck)
            other.draw(deck)
        self.hand = " ".join(self.hand)
        other.hand = " ".join(other.hand)

class Deck:
    def __init__(self):
        self.deck = []
        self.build()
        
    def build(self):
        face_vals = {2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"T", 11:"J", 12:"Q", 13:"K", 14:"A"}
        for s in ["H", "S", "D", "C"]:
            for i in range(2, 15):
                self.deck.append(face_vals[i] + s)

    def show(self):
        for c in self.deck:
            print (c)
    
    def shuffle(self):
        for i in range(len(self.deck)-1, 0, -1):
            r = random.randint(0, i)
            self.deck[r], self.deck[i] = self.deck[i], self.deck[r]
    
    def drawCard(self):
        return self.deck.pop()
        
class PokerHand(object):
   
    def __init__(self, hand):
        self.name = self
        self.hand = hand
        
        # Establishes card values
        self.face_val = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
        # suit_ranks = {"H":4, "S":3, "D":2, "C":1}
        self.hand_ranks = {"RF":10, "SF":9, "4K":8, "FH":7, "F":6, "S":5, "3K":4, "2P":3, "1P":2, "HC":1}
        
        # sets up list of cards in your hand, separated num and suite
        self.cards = []
        for card in hand.split():
            self.cards.append((card[0], card[1]))
            
        self.nums = [self.face_val[n] for n, s in self.cards]
        total_val = sum(self.nums)
        self.suits = [s for n, s in self.cards]
        
        def of_a_kind(self, nums):
            unique = set(nums)
            self.left_over = []
            self.kind = []
            self.pairs = []

            for u in unique:
                if nums.count(u) > 1:
                    self.kind.append([nums.count(u), u])
                else:
                    self.left_over.append(u)
            
            # for c, s in self.kind:
            #     if 

            return (self.kind) if len(self.kind)> 0 else False
        
        # Checks the suit of the cards for a Flush
        def suited_cards(suits):
            self.suited = set(suits)

            if len(self.suited) == 1:
                return True, self.suited
            
            return False, self.suited
            
        def sequenced_cards(values):
            value_range = max(values) - min(values)
            if value_range == 4:
                return True, max(values)
            else:
                return False, None
        
    
        if isinstance(of_a_kind(self, self.nums), list):
            points = 0
           
            for quan, card in of_a_kind(self, self.nums):
                points += quan
            if points == 2:
                my_rank = self.hand_ranks["1P"]
            elif points == 3:
                my_rank = self.hand_ranks["3K"]
            elif points == 4 and len(of_a_kind(self, self.nums)) == 1:
                my_rank = self.hand_ranks["4K"]
            elif points == 4:
                my_rank = self.hand_ranks["2P"]
            elif points == 5:
                my_rank = self.hand_ranks["FH"]
            
            self.high_set = max(self.kind)[1]
       
        elif sequenced_cards(self.nums)[0] and suited_cards(self.suits)[0]:
            my_rank = self.hand_ranks["SF"]

        elif sequenced_cards(self.nums)[0] and not suited_cards(self.suits)[0]:
            my_rank = self.hand_ranks["S"]

        elif suited_cards(self.suits)[0] and not sequenced_cards(self.nums)[0]:
            my_rank = self.hand_ranks["F"]
        
        else:
            my_rank = self.hand_ranks["HC"]
                    
        self.myscore = [my_rank, total_val]
        
        for h, s, in self.hand_ranks.items():
            if s == self.myscore[0]:
                self.my_hand = h
            
    # Compares Ranks and total values of PokerHand Objects    
    def compare_with(self, other):
        
        if self.myscore[0] == 1 and other.myscore[0] == 1:
            for i in range(5):
                if sorted(self.nums, reverse= True)[i] > sorted(other.nums, reverse= True)[i]:
                    return self
                elif sorted(self.nums, reverse= True)[i] < sorted(other.nums, reverse= True)[i]:
                    return other
                else:
                    continue
                
        if self.myscore[0] == 2 and other.myscore[0] == 2:
            if self.high_set > other.high_set:
                return self
            elif self.high_set == other.high_set:
                if self.myscore[1] > other.myscore[1]:
                    return other
                elif self.myscore[1] < other.myscore[1]:
                    return other
                else:
                    return "Tie"
            else:
                return other
                
        if self.myscore[0] == other.myscore[0]:
            if self.myscore[1] > other.myscore[1]:
                return self
            elif self.myscore[1] < other.myscore[1]:
                return other
            else:
                return "Tie"
                
        if self.myscore[0] > other.myscore[0]:
            return self
        else:
            return other
        
def runGame(name1="Player", name2="Computer"):

    p1 = Player(name1)
    p2 = Player(name2)
    
    print ("\nWelcome", p1.name, "and", p2.name, "!")
    # time.sleep(5)
    print ("\nLet's Play Some Cards!\n")
    cards = Deck()
    cards.shuffle()
    
    p1.dealHand(p2, cards, 5)
    
    p1score, p2score = PokerHand(p1.hand), PokerHand(p2.hand)
    
    print (p1.name, ":", p1.hand)
    # time.sleep(5)
    print (p1score.my_hand)
    print ("\n")
    # time.sleep(5)
    print (p2.name, ":", p2.hand)
    # time.sleep(5)
    print (p2score.my_hand)
    print ("\n")
    # time.sleep(5)
    
    if p1score.compare_with(p2score) == p1score:
        print (p1.name, "Wins")
    elif p1score.compare_with(p2score) == p2score:
        print (p2.name, "Wins")
    else:
        print (p1score.compare_with(p2score))
    

def start():
    try:
        p1 = input("P1 Name: ")
    except EOFError:
        p1 = False
    try:
        p2 = input("P2 Name: ")
    except EOFError:
        p2 = False
        
    if p1:
        if p2:
            runGame(p1, p2)
        else:
            runGame(p1)
    else:
        runGame()

start()
