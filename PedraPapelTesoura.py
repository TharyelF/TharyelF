import random

def play():
    user = input("Qual a sua escolha? 'Pe' para Pedra, 'Pa' para Papel, 'Te' para Tesoura\n")
    computer = random.choice(['Pe', 'Pa', 'Te'])

    if user == computer:
         return 'it\'s a tie'

    # Pe > Te, Te > Pa, Pa > Pe
    if is_win(user, computer):
         return 'Voçe Venceu!'
    
    return 'Voçe Perdeu!'

def is_win(player, Opponent):
    # return true if player wins
    # Pe > Te, Te > Pa, Pa > Pe
    if (player == 'Pe' and Opponent == 'Te') or (player == 'Te' and Opponent == 'Pa') \
        or (player == 'Pa' and Opponent == 'Pe'):
        return True

print(play())