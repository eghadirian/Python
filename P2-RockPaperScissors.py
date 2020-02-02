def rock_paper_scissors():
    """Rock, Paper, Scissors game"""
    user1 = input("What's your name?")
    user2 = input("And your name?")

    while True:
        game_dict = {'rock': 1, 'scissors': 2, 'paper': 3}
        player_a = input("{}, do yo want to choose rock, paper or scissors?".format(user1))
        player_b = input("{}, do you want to choose rock, paper or scissors?".format(user2))
        a = game_dict[player_a.lower()]
        b = game_dict[player_b.lower()]
        dif = a - b

        try:
            if dif in [-1, 2]:
                print('{} wins.'.format(user1))
            elif dif in [-2, 1]:
                print('{} wins.'.format(user2))
            else:
                print('Draw. Please continue.')
                print('')
        except:
            print('Please choose from rock, paper, or scissors only!')
            continue

        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('game over.')
            break

if __name__ == '__main__':
    rock_paper_scissors()