from card import Card
from gamedealer import Gamedealer
class Player():
    def __init__(self, name):
        self.name = name
        self.holding_card_list = []
        self.open_card_list = []

    def getCard(self, cardList:list):
        self.holding_card_list.extend(cardList)

    def showOpenHoldingCards(self):
        print("============================================================")
        print(f"[{self.name}] Open card list: {len(self.open_card_list)}")
        print(" ".join(map(str, self.open_card_list))) if len(self.open_card_list) > 0 else print("")
        print("")
        print(f"[{self.name}] Holding card list: {len(self.holding_card_list)}")
        print(" ".join(map(str, self.holding_card_list))) if len(self.holding_card_list) > 0 else print("")
        print("")

    def moveToOpenCard(self):
        print("============================================================")
        print(f"[{self.name}: 숫자가 같은 한쌍의 카드 검사]")
        # print("============================================================")
        copyList = self.holding_card_list
        tmp = list()
        for idx, card in enumerate(copyList, 1):
            for i in range(idx, len(copyList)):
                if card.number == copyList[i].number and card not in tmp:
                    tmp.append(copyList[i])
                    tmp.append(card)
        self.open_card_list.extend(tmp)
        [self.holding_card_list.remove(card) for card in tmp]

    def clearOpenCards(self):
        self.open_card_list.clear()



if __name__ == '__main__':
    test = Gamedealer()
    test.make_deck()
    test.shuffle_card()
    result = test.give_card(True, 1)
    play = Player('test')
    play.getCard(*result)

    play.showOpenHoldingCards()
    play.moveToOpenCard()
    play.showOpenHoldingCards()