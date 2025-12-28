def player(prev_play, opponent_history=[], my_history=[], play_order={}, strategy_scores={}):
    if not prev_play:
        opponent_history.clear()
        my_history.clear()
        play_order.clear()
        strategy_scores.clear()
        strategy_scores.update({"quincy": 0, "kris": 0, "mrugesh": 0, "abbey": 0})
        return "R"
    
    opponent_history.append(prev_play)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    beats = {'S': 'R', 'R': 'P', 'P': 'S'}
    
    # Update play order tracking - track MY move patterns (what abbey sees)
    if len(my_history) >= 2:
        last_two = "".join(my_history[-2:])
        play_order[last_two] = play_order.get(last_two, 0) + 1
    
    # Evaluate previous predictions if we have history
    if len(my_history) >= 1:
        # Check quincy prediction
        if len(opponent_history) >= 2:
            quincy_pattern = ["R", "R", "P", "P", "S"]
            predicted = quincy_pattern[(len(opponent_history) - 1) % 5]
            if predicted == prev_play:
                strategy_scores["quincy"] += 1
        
        # Check kris prediction
        if len(my_history) >= 2:
            predicted = ideal_response[my_history[-2]]
            if predicted == prev_play:
                strategy_scores["kris"] += 1
        
        # Check mrugesh prediction
        if len(my_history) >= 11:
            last_ten = my_history[-11:-1]
            most_freq = max(set(last_ten), key=last_ten.count)
            predicted = ideal_response[most_freq]
            if predicted == prev_play:
                strategy_scores["mrugesh"] += 1
        
        # Check abbey prediction
        if len(my_history) >= 2:
            last_move = my_history[-2]
            potential_plays = [
                last_move + "R",
                last_move + "P",
                last_move + "S",
            ]
            sub_order = {k: play_order.get(k, 0) for k in potential_plays}
            if sum(sub_order.values()) > 0:
                abbey_pred_move = max(sub_order, key=sub_order.get)[-1:]
                predicted = ideal_response[abbey_pred_move]
                if predicted == prev_play:
                    strategy_scores["abbey"] += 1
    
    # Generate predictions for each strategy
    predictions = {}
    
    # Quincy prediction
    if len(opponent_history) >= 1:
        quincy_pattern = ["R", "R", "P", "P", "S"]
        next_quincy = quincy_pattern[len(opponent_history) % 5]
        predictions["quincy"] = ideal_response[next_quincy]
    
    # Kris prediction
    if len(my_history) >= 1:
        kris_will_play = ideal_response[my_history[-1]]
        predictions["kris"] = ideal_response[kris_will_play]
    
    # Mrugesh prediction
    if len(my_history) >= 10:
        last_ten = my_history[-10:]
        most_freq = max(set(last_ten), key=last_ten.count)
        mrugesh_will_play = ideal_response[most_freq]
        predictions["mrugesh"] = ideal_response[mrugesh_will_play]
    
    # Abbey prediction
    if len(my_history) >= 1:
        last_move = my_history[-1]
        potential_plays = [
            last_move + "R",
            last_move + "P",
            last_move + "S",
        ]
        sub_order = {k: play_order.get(k, 0) for k in potential_plays}
        
        if sum(sub_order.values()) > 0:
            abbey_thinks_we_play = max(sub_order, key=sub_order.get)[-1:]
            abbey_will_play = ideal_response[abbey_thinks_we_play]
            predictions["abbey"] = ideal_response[abbey_will_play]
        else:
            predictions["abbey"] = "P"
    
    # Choose best strategy based on scores
    if len(opponent_history) > 20:
        # Find top 2 strategies
        sorted_strategies = sorted(strategy_scores.items(), key=lambda x: x[1], reverse=True)
        
        # If one strategy is clearly winning, use it
        if sorted_strategies[0][1] > sorted_strategies[1][1] + 5:
            best_strategy = sorted_strategies[0][0]
            if best_strategy in predictions:
                guess = predictions[best_strategy]
            else:
                guess = "R"
        else:
            # If scores are close, use weighted voting
            weighted_preds = []
            for strategy, score in strategy_scores.items():
                if strategy in predictions:
                    weighted_preds.extend([predictions[strategy]] * (score + 1))
            
            if weighted_preds:
                guess = max(set(weighted_preds), key=weighted_preds.count)
            else:
                guess = "R"
    else:
        # Early game: use all predictions with voting
        all_preds = list(predictions.values())
        if all_preds:
            guess = max(set(all_preds), key=all_preds.count)
        else:
            guess = "R"
    
    my_history.append(guess)
    return guess
