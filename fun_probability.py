'''fun_probability
Functions to assist in probability tasks.
'''
import random

import numpy as np

def dice_roll(n_sides=6, n_rolls=1):
    ''' Roll an n-sided virtual die a given number of times.
    
    Keyword arguments:
    n_sides -- the number of sides for the virtual die (6 by default, 
        corresponding to a conventional 6-sided die)
    n_rolls -- the number of times to roll the virtual die

    Outputs:
    list_rolls -- a list with the values of the simulated rolls
    '''
    list_rolls = []
    for rolls in np.arange(0, n_rolls):
        roll_value = random.randint(1, n_sides)
        list_rolls.append(roll_value)
        
    return list_rolls

def dice_value_trials(n_rolls=1000, value_oi=None):
    #  QUESTION: Write your own docstring for this function.
    list_rolls = dice_roll(n_sides=6, n_rolls=n_rolls)
    value_counts, _ = np.histogram(list_rolls, bins=6, range=(1, 6))
    dict_perc = {
        1: value_counts[0] / n_rolls * 100,
        2: value_counts[1] / n_rolls * 100,
        3: value_counts[2] / n_rolls * 100,
        4: value_counts[3] / n_rolls * 100,
        5: value_counts[4] / n_rolls * 100,
        6: value_counts[5] / n_rolls * 100
    }
    if value_oi is not None:
        out_value_freq = dict_perc[value_oi]
    else:
        out_value_freq = None
    return dict_perc, out_value_freq