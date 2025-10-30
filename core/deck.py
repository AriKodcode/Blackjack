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

    return deck

