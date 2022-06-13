import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Advinhe um número entre 1 e {x}: '))
        if guess < random_number:
            print('Desculpe, tente novamente. Muito baixo.')
        elif guess > random_number:
            print('Desculpe, tente novamente. Muito alto.') 

    print(f'Isso!!, Parabens. Voçe Adivinhou o Número {random_number} !!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
             guess = random.randint(low, high) 
        else:
             guess = low # Tambem pod ser  high b/c low = high /        
        feedback = input(f'Seria {guess} Muito alto (H), Muito baixo (L) or Correto (C)?? ').lower()
        if feedback =='H':
            high = guess - 1
        elif feedback == 'l':
            low = guess +1

    print(f'Isso!! O computador acertou o número {guess}')        


computer_guess(50)

guess(50)