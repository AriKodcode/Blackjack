from random import randrange


def build_standard_deck() -> list[dict]:
    cards_list = []
    card_number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    types_of_cards = ["H", "C", "D", "S"]
    for num in card_number:
        for type_card in types_of_cards:
            new_card = {"rank": num, "suite": type_card}
            cards_list.append(new_card)
    return cards_list


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    counter = 0
    while counter <= swaps:
        index_i = randrange(len(deck))
        index_j = randrange(len(deck))
        if index_i != index_j:
            if deck[index_i]["suite"] == "H" and index_j % 5 == 0:
                deck[index_i], deck[index_j] = deck[index_j], deck[index_i]
                counter += 1
                continue
            if deck[index_i]["suite"] == "C" and index_j % 3 == 0:
                deck[index_i], deck[index_j] = deck[index_j], deck[index_i]
                counter += 1
                continue
            if deck[index_i]["suite"] == "D" and index_j % 2 == 0:
                deck[index_i], deck[index_j] = deck[index_j], deck[index_i]
                counter += 1
                continue
            if deck[index_i]["suite"] == "S" and index_j % 7 == 0:
                deck[index_i], deck[index_j] = deck[index_j], deck[index_i]
                counter += 1
    return deck

