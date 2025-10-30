def ask_player_action() -> str:
    while True:
        user_input = input("Press S or H")
        if not user_input.isdigit():
            if user_input == "S":
                break
            elif user_input == "H":
                break
            else:
                print("Error press S or H only")
                continue
        else:
            print("Error prees H or S only")
    return user_input


print(ask_player_action())