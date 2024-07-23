# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

#Predictive Strategy:

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    if len(opponent_history) > 1:
        last_move = opponent_history[-1]
        second_last_move = opponent_history[-2]
        
        if last_move == 'R' and second_last_move == 'R':
            return 'P'
        elif last_move == 'P' and second_last_move == 'P':
            return 'S'
        elif last_move == 'S' and second_last_move == 'S':
            return 'R'
        else:
            return 'R'  # Default move if no pattern detected
    return 'R'  # Default move if no history

