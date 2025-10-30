from core.deck import build_standard_deck,shuffle_by_suit

def calculate_hand_value(hand: list[dict]) -> int:
    sum_value_cards = 0
    for card in hand:
        if card["rank"] == "J":
            sum_value_cards += 10
        elif card["rank"] == "Q":
            sum_value_cards += 10
        elif card["rank"] == "K":
            sum_value_cards += 10
        elif card["rank"] == "A":
            sum_value_cards += 1
        else:
            sum_value_cards += int(card["rank"])
    return sum_value_cards


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop())
    player["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())
    dealer["hand"].append(deck.pop())
    print("player value cards: ", calculate_hand_value(player["hand"]))
    print("dealer value cards: ", calculate_hand_value(dealer["hand"]))



def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while True:
        print("dealer card is" ,deck[-1])
        dealer["hand"].append(deck.pop())
        if calculate_hand_value(dealer["hand"]) > 21:
            dealer = "los"
            break
        elif 17 <=calculate_hand_value(dealer["hand"]) <= 21:
            dealer = 'win'
    if dealer == "los":
        return False
    else:
        return True


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    return None
