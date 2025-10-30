from core.deck import build_standard_deck, shuffle_by_suit
from core.player_io import ask_player_action


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
        print("dealer card is", deck[-1])
        dealer["hand"].append(deck.pop())
        if calculate_hand_value(dealer["hand"]) > 21:
            dealer = "los"
            break
        elif 17 <= calculate_hand_value(dealer["hand"]) <= 21:
            dealer = 'win'
    if dealer == "los":
        return False
    else:
        return True


def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    print("wellcome to black jack game\ndood luck!")
    print("Press Enter to start")
    input("")
    status_game = ""
    deal_two_each(deck,player,dealer)
    game = True
    while game:
        player_turn = True
        dealer_turn = False
        while player_turn:
            print("player turn")
            user_input = ask_player_action()
            if user_input == "H":
                player["hand"].append(deck.pop())
                check_hand_player = calculate_hand_value(player["hand"])
                print(calculate_hand_value(player["hand"]))
                if check_hand_player > 21:
                    status_game = "dealer won"
                    player_turn = False
                    game = False
                    break
            elif user_input == "S":
                player_turn = False
                dealer_turn = True
                break

        while dealer_turn:
            check_hand_dealer = dealer_play(deck,dealer)
            if not check_hand_dealer:
                dealer_turn = False
                game = False
                status_game = "player won"
                break
            else:
                if calculate_hand_value(dealer["hand"]) > calculate_hand_value(player["hand"]):
                    status_game = "dealer won"
                    dealer_turn = False
                    game = False
                    break
                if calculate_hand_value(dealer["hand"]) < calculate_hand_value(player["hand"]):
                    status_game = "player won"
                    dealer_turn = False
                    game = False
                    break
                if calculate_hand_value(dealer["hand"]) == calculate_hand_value(player["hand"]):
                    status_game = "draw"
                    dealer_turn = False
                    game = False
                    break
    print(f"{status_game} \n player: {player} player hand {calculate_hand_value(player["hand"])} \n dealer: {dealer} dealer hand: {calculate_hand_value(dealer["hand"])}")
