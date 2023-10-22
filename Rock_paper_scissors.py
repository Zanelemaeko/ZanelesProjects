import random

def computer_move():
    random_move = random.randint(1,3)
    random_answer = ''
    if random_move == 1:
        random_answer ='rock'
    elif random_move == 2:
        random_answer = 'paper'
    elif random_move == 3:
        random_answer = 'scissors'
    return random_answer

def user_answer():
    result = ''
    answer = input('Choose rock, paper, scissors: ')
    comparison = computer_move()
    
    if  answer == 'rock' and comparison == 'rock':
        result = 'Its a tie'
    elif answer == 'rock' and comparison == 'paper':
        result = 'You loose'
    elif answer == 'rock' and comparison == 'scissors':
        result = 'you win'
    elif answer == 'paper' and comparison == 'rock':
        result = 'You win'
    elif answer == 'paper' and comparison == 'paper':
        result = 'Its a tie'
    elif answer == 'paper' and comparison == 'scissors':
        result = 'You loose'
    elif answer == 'scissors' and comparison == 'rock':
        result = 'You loose'
    elif answer == 'scissors' and comparison == 'paper':
        result = 'You win'
    elif answer == 'scissors' and comparison == 'scissors':
        result = 'Its a tie'
    return 'You picked {}. Computer picked {}. {}'.format(answer,comparison,result)

print(user_answer())