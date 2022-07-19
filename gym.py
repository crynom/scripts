#program for the gym
print('\n')
perform = input('What would you like to do today? (Max, Reps): ')
print('\n')

def max():
    bench = []
    squat = []
    deadlift = []
    #get bench
    print('\n')
    dobench = input('(Y/N) Bench: ')
    if dobench == 'y' or dobench == 'Y':
        print('\n','Doing bench...', '\n')
        bench.append(float(input('What is your bench? ')))
        print('\n')
        bench.append(float(input('For how many reps? ')))
    else:
        print('\n','Skipping bench...')
        bench = [0,0]
    #get squat
    print('\n')
    dosquat = input('(Y/N) Squat: ')
    if dosquat == 'y' or dosquat == 'Y':
        print('\n','Doing squat...', '\n')
        squat.append(float(input('What is your squat? ' )))
        print('\n')
        squat.append(float(input('For how many reps? ')))
    else:
        print('\n','Skipping squat...')
        squat = [0,0]
    #get deadlift
    print('\n')
    dodeadlift = input('(Y/N) Deadlift: ')
    if dodeadlift == 'y' or dodeadlift == 'Y':
        print('\n','Doing deadlift...', '\n')
        deadlift.append(float(input('What is your deadlift? ')))
        print('\n')
        deadlift.append(float(input('For how many reps? ')))
    else:
        print('\n', 'Skipping deadlift...')
        deadlift = [0,0]
    #calculate maxes
    #bench max
    bench.append(bench[0] * (1.028 ** (bench[1]-1)))
    #squat max
    squat.append(squat[0] * (1.036 ** (squat[1]-1)))
    #deadlift max
    deadlift.append(deadlift[0] * (1.040 ** (deadlift[1]-1)))

    #print maxes
    if dobench == 'Y' or dobench == 'y':
        print('\n')
        prb = input('(Y/N) Print estimated max bench: ')
    else:
        prb = 'n'
    if dosquat == 'Y' or dosquat == 'y':
        print('\n')
        prs = input('(Y/N) Print estimated max squat: ')
    else:
        prs = 'n'
    if dodeadlift == 'Y' or dodeadlift == 'y':
        print('\n')
        prd = input('(Y/N) Print estimated max deadlift: ')
    else:
        prd = 'n'
    if prb == 'Y' or prb == 'y':
        print('\n', 'Your bench is', bench[0], 'for', bench[1], "reps. Your estimated 1.0 rep max is:", bench[2])
    if prs == 'Y' or prs == 'y':
        print('\n', 'Your squat is', squat[0], 'for', squat[1], "reps. Your estimated 1.0 rep max is:", squat[2])
    if prd == 'Y' or prd == 'y':
        print('\n', 'Your deadlift is', deadlift[0], 'for', deadlift[1], "reps. Your estimated 1.0 rep max is:", deadlift[2])

    #print total
    print('\n')
    prt = input('(Y/N) Print total? ')
    if prt == 'Y' or prt == 'y':
        print('\n', 'Your total lifted weight is', str((bench[2] + squat[2] + deadlift[2])) + '.', '\n')

if perform == 'max' or perform == 'Max' or perform == 'm' or perform == 'M':
    max()

#calculate rep range inputs exercise and goal, outputs sets, weights, and reps
def reps(exercise, goal):
    if goal == 0:
        working_sets=[8,5,5,5,3]
    elif goal == 1:
        working_sets=[15,12,10]
    #number of sets
    sets = len(working_sets)
    bias = [[.028, 'BENCH'], [.036, 'SQUAT'], [.040, 'DEADLIFT'], [.025, 'INCLINE BENCH']]
    e = 0
    if exercise == 'bench' or exercise == 'Bench':
        e = 0
    elif exercise == 'squat' or exercise == 'Squat':
        e = 1
    elif exercise == 'deadlift' or exercise == 'Deadlift' or exercise == 'dl':
        e = 2
    elif exercise == 'Incline Bench' or exercise == 'incline bench' or exercise == 'Incline bench' or exercise == 'incline':
        e = 3  
    user_weight = float(input(('How much can you ' + bias[e][1] + '? ')))
    print('\n')
    user_reps = float(input('For how many reps? '))
    print('\n')

    max_weight = user_weight * ((1 + bias[e][0]) ** (user_reps - 1))
    ws = [0,0,0,0,0]
    ws[0] = 5 * round((max_weight * 0.575) / 5)
    ws[1] = 5 * round((max_weight * 0.75) / 5)
    ws[2] = 5 * round((max_weight * 0.825) / 5)
    ws[3] = 5 * round((max_weight * 0.85) / 5)
    ws[4] = 5 * round((max_weight * 0.9) / 5)

    wh = [0,0,0]
    wh[0] = 5 * round((max_weight * 0.6) / 5)
    wh[1] = 5 * round((max_weight * 0.65) / 5)
    wh[2] = 5 * round((max_weight * 0.7) / 5)

    setbyset = input('Do you want to go set by set (S) or print all at once (O)?: ')
    print('\n')
    if setbyset == 'S' or setbyset == 's':
        if goal == 0:
            print('\n')
            print('Your weights for', bias[e][1], 'are ready! It will be', sets, 'total sets.')
            null = input('Press any key to continue...') #press to cont
            print('\n')

            print('Set 1 for', bias[e][1], 'will be', working_sets[0], 'reps of', ws[0])
            null = input('Press any key to continue...')
            print('\n')

            print('Set 2 for', bias[e][1], 'will be', working_sets[1], 'reps of', ws[1])
            null = input('Press any key to continue...')
            print('\n')

            print('Set 3 for', bias[e][1], 'will be', working_sets[2], 'reps of', ws[2])
            null = input('Press any key to continue...')
            print('\n')

            print('Set 4 for', bias[e][1], 'will be', working_sets[3], 'reps of', ws[3])
            null = input('Press any key to continue...')
            print('\n')

            print('Set 5 for', bias[e][1], 'will be', working_sets[4], 'reps of', ws[4])
            print('You are done!')
            null = input('Press any key to continue...')
            print('\n')

        elif goal == 1:
            print('\n')
            print('Your weights for', bias[e][1], 'are ready! It will be', sets, 'total sets.')
            null = input('Press any key to continue...')
            print('\n')

            print('Set 1 for', bias[e][1], 'will be', working_sets[0], 'reps of', wh[0])
            null = input('Press any key to continue...')
            print('\n')

            print('Set 2 for', bias[e][1], 'will be', working_sets[1], 'reps of', wh[1])
            null = input('Press any key to continue...')
            print('\n')

            print('Set 3 for', bias[e][1], 'will be', working_sets[2], 'reps of', wh[2])
            print('You are done!')
            null = input('Press any key to continue...')
            print('\n')
    
    elif setbyset == 'O' or setbyset == 'o':
        if goal == 0:
            print('\n')
            print('Your weights for', bias[e][1], 'are ready! It will be', sets, 'total sets.')
            print('\n')
            
            print('Set 1 for', bias[e][1], 'will be', working_sets[0], 'reps of', ws[0])
            
            print('Set 2 for', bias[e][1], 'will be', working_sets[1], 'reps of', ws[1])
            
            print('Set 3 for', bias[e][1], 'will be', working_sets[2], 'reps of', ws[2])
            
            print('Set 4 for', bias[e][1], 'will be', working_sets[3], 'reps of', ws[3])

            print('Set 5 for', bias[e][1], 'will be', working_sets[4], 'reps of', ws[4])
            print('\n')

        elif goal == 1:
            print('\n')
            print('Your weights for', bias[e][1], 'are ready! It will be', sets, 'total sets.')
            print('\n')
            print('Set 1 for', bias[e][1], 'will be', working_sets[0], 'reps of', wh[0])
            
            print('Set 2 for', bias[e][1], 'will be', working_sets[1], 'reps of', wh[1])
            
            print('Set 3 for', bias[e][1], 'will be', working_sets[2], 'reps of', wh[2])
            print('\n')
    

if perform == 'Reps' or perform == 'R' or perform == 'reps' or perform == 'r':
    u_l = input('(U/L) Upper body or lower body?: ')
    print('\n')
    s_h = input('(S/H) Strength or hypertrophy?: ')
    print('\n')
    if s_h == 'S' or s_h == 's' or s_h == 'Strength' or s_h == 'strength':
        goal = 0
    elif s_h == 'H' or s_h == 'h' or s_h == 'Hypertrophy' or s_h == 'hypertrophy':
        goal = 1
    else:
        print('ERROR')
    if u_l == 'U' or u_l == 'u' or u_l == 'Upper' or u_l == 'upper':
        exercise = input('Select Exercise: (Bench/Incline Bench) ')
        print('\n')
    elif u_l == 'L' or u_l == 'l' or u_l == 'Lower' or u_l == 'lower':
        exercise = input('Select Exercise: (Squat/Deadlift) ')
        print('\n')
    else:
        print('ERROR')
    
    reps(exercise, goal)
    

