#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random as rand


# In[433]:


def run_simulation(switch, verbose):
    doors = [1, 2, 3]
    
    script = ''
    
    script += f'Pick a door from this list: {doors}'
    prize_door = rand.randint(1, 3)
    empty_doors = [d for d in doors if d != prize_door]
    guess_door = rand.randint(1, 3)
    script += f'\nYou picked door {guess_door}'

    notin_door_array = [d for d in empty_doors if d != guess_door]
    if len(notin_door_array) > 1:
        rand_idx = rand.randint(0, 1)
        notin_door = notin_door_array[rand_idx]
    else:
        notin_door = notin_door_array[0]
    script += f'''\nBefore the prize door is revealed, I\'ll tell you that door {notin_door}
    is not the correct choice. Do you want to switch?
        '''
    if switch:
        switch_door = [d for d in doors if d not in [guess_door, notin_door]][0]
        script += f'Yes I am switching from {guess_door} to {switch_door}.\n'
        guess_door = switch_door
    else:
        script += 'No I am not switching.\n'
    
    script += f'The prize is behind door {prize_door}.'
    if guess_door == prize_door:
        script += 'You win the prize. Good shit boy\n'
        if verbose:
            print(script)
        return True
    else:
        script += 'You lost dumbass\n'
        if verbose:
            print(script)
        return False
    
#     print('doors', doors, '\nprize_door', prize_door, '\nguess',  guess_door, '\nempty doors', empty_doors, '\nnotin_door_array', notin_door_array, '\nnotin_door'
#           , notin_door, '\nswitch_door:', switch_door)


# In[ ]:


# switch: boolean
#           True for deciding to switch
#           False for not switching
def run_trials(ntrials, switch, verbose = False):
    ncorrect = 0
    nwrong = 0
    for n in range(ntrials):
        outcome = run_simulation(switch = switch, verbose = verbose)
        if outcome:
            ncorrect += 1
        else:
            nwrong += 1
    percentage = float(ncorrect) / float(ntrials) 
    print(f'Number of times prize was won: {ncorrect}\nNumber of times incorrect: {nwrong}\nPercentage: {percentage}')


# In[454]:


print('10,000 Trials for switching:')
run_trials(10000, True)
print('\n10,000 Trials for not switching:')
run_trials(10000, False)

