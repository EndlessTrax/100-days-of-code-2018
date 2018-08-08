import random 

# ASSIGNMENT
# Assignment from the Real Python course -- https://realpython.com/products/real-python-course/
# Election between candidates A and B based on majority of three regions.
# Candidate A has the following odds:
#   87% chance of winning region 1
#   65% chance of winning region 2
#   17% chance of winning region 3
# Function to return a number between 0-1
# Simulate 10,000 elections, then based on the average result display the probability that candidate A will win,
# and the probability candidate B will win.

# TODO: Refactor the hell outta it!
# TODO: Convert final decimal average into percentage figure

def random_result():
    ''' Generates a random floating point number between 0 and 1 '''
    result = random.random()
    return result


def election_region_1(num):
    if num <= 0.87:
        print('Candidate A won Region 1')
        return 1
    else: 
        print('Candidate B won Region 1')
        return 0


def election_region_2(num):
    if num <= 0.65:
        print('Candidate A won Region 2')
        return 1
    else: 
        print('Candidate B won Region 2')
        return 0


def election_region_3(num):
    if num <= 0.17:
        print('Candidate A won Region 3')
        return 1
    else: 
        print('Candidate B won Region 3')
        return 0


def main():

    election_wins_A = 0
    election_wins_B = 0

    for i in range(0, 10000):
        vote = random_result()
        result1 = election_region_1(vote)
        result2 = election_region_2(vote)
        result3 = election_region_3(vote)
        
        
        candidate_A_wins_region1 = 0    
        candidate_B_wins_region1 = 0
        if result1 == 1:
            candidate_A_wins_region1 += 1
        else: 
            candidate_B_wins_region1 += 1

        
        candidate_A_wins_region2 = 0
        candidate_B_wins_region2 = 0

        if result2 == 1:
            candidate_A_wins_region2 += 1
        else: 
            candidate_B_wins_region2 += 1


        candidate_A_wins_region3 = 0
        candidate_B_wins_region3 = 0

        if result3 == 1:
            candidate_A_wins_region3 += 1
        else: 
            candidate_B_wins_region3 += 1


        candidate_A_total = candidate_A_wins_region1 + candidate_A_wins_region2 + candidate_A_wins_region3
        candidate_B_total = candidate_B_wins_region1 + candidate_B_wins_region2 + candidate_B_wins_region3
        if candidate_A_total > candidate_B_total:
            print('Candidate A wins the election!!')
            election_wins_A += 1
        else:
            print('Candidate B wins the election!!')
            election_wins_B += 1

    
    percentage_A_wins = election_wins_A / 10000
    percentage_B_wins = election_wins_B / 10000

    print('==========================')
    print(f'Candidate A won {election_wins_A} times')
    print(f'Candidate B won {election_wins_B} times')
    print('==========================')
    print(f'Candidate A has {percentage_A_wins} chance of winning')
    print(f'Candidate B has {percentage_B_wins} chance of winning')


if __name__ == '__main__':
    main()