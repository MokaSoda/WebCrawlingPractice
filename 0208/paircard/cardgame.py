from player import Player
from card import Card
from gamedealer import Gamedealer

def main():

    gameDealer = Gamedealer()
    player1 = Player('흥부')
    player2 = Player('놀부')
    # player3 = Player('타인')
    players = [player1, player2]


    gameEnd = False
    first = True
    i = 1
    gameDealer.make_deck()
    gameDealer.shuffle_card()
    while not gameEnd:
        print(f"[{i}] 단계: 다음 단계 진행을 위해 Enter 키를 누르세요!")
        # print("")
        if first:
            pass
        given = gameDealer.give_card(first, len(players)) if i != 2 else None
        if given:
            [person.getCard(given[idx]) for idx, person in enumerate(players)]
        for person in players:
            person.moveToOpenCard() if not first else ""
            person.showOpenHoldingCards()

        first = False
        if sum([person.holding_card_list == 0 for person in players]) or int(len(gameDealer.deck) == 0) > 0:
            gameEnd = True
        if gameEnd:
            print("게임 종료")
            break

        i += 1


if __name__ == '__main__':
    main()
