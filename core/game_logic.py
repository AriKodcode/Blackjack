def calculate_hand_value(hand: list[dict]) -> int:
    sum_value_cards = 0
    for card in hand:
        sum_value_cards += card["rank"]
    return sum_value_cards

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    return None


def dealer_play(deck: list[dict], dealer: dict) -> bool:
    return True


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    return None