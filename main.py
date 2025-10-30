from core.deck import build_standard_deck,shuffle_by_suit
from core.player_io import ask_player_action
from core.game_logic import calculate_hand_value,deal_two_each,dealer_play,run_full_game

if __name__ == "__main__":
    cards = build_standard_deck()
    cards = shuffle_by_suit(cards)
    player = {"hand": []}
    dealer = {"hand": []}
    run_full_game(cards,player,dealer)