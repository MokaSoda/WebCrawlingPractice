from card import Card
import random


class Gamedealer():
    def __init__(self):
        self.deck = []
        self.player_hand = []

    def showDealerCard(self):
        for idx, x in enumerate(self.deck, 1):
            print(x, end=" " if idx % 13 != 0 else "\n")
        print()
    def currentDealerCard(self, cnt, first = False):
        if not first:
            print('============================================================')
            print(f"카드나누어주기: {cnt}장")
        print("------------------------------------------------------------")
        print("[GameDealer] 게임 딜러가 가진 카드 수: %s" % len(self.deck))
        self.showDealerCard()

    def make_deck(self):
        card_suits = ["♠", "♥", "♣", "◆"]
        card_numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        print("[GameDealer] 초기 카드 생성")
        self.deck = [Card(card_suit, card_number) for card_suit in card_suits for card_number in card_numbers]
        self.currentDealerCard(0, True)

    def shuffle_card(self):
        random.shuffle(self.deck)
        print("[GameDealer] 카드 랜덤하게 섞기")
        print("------------------------------------------------------------")
        self.showDealerCard()

    def give_card(self, start=False, player=1):
        first = 10
        normal = 4
        result = []

        def divideToPlayer(cnt):
            for x in range(cnt):
                tmp = random.sample(self.deck, first if start else normal)
                [self.deck.remove(x) for x in tmp]
                result.append(tmp)

        if start and len(self.deck) // player >= 10:
            divideToPlayer(player)
            self.currentDealerCard(first)
        elif not start and len(self.deck) // player >= 4:
            divideToPlayer(player)
            self.currentDealerCard(normal)
        else:
            self.deck.clear()
            print("게임 진행 불가" if start else "딜러가 나눠줄 카드가 부족하기 때문에 게임 종료")

        return result


if __name__ == '__main__':
    test = Gamedealer()
    test.make_deck()
    test.shuffle_card()
    # print(test.deck)
    print(test.give_card(True, 6))
    print(test.deck)
    print(test.give_card(False, 3))
    print(test.deck)
    print(test.give_card(False, 3))
    print(test.deck)
    print(test.give_card(False, 3))
