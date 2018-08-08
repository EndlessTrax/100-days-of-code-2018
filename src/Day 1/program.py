import random 


# Assignment from the Real Python course -- https://realpython.com/products/real-python-course/
# Election between candidates A and B based on majority of three regions.
# Candidate A has the following odds:
#   87% chance of winning region 1
#   65% chance of winning region 2
#   17% chance of winning region 3
# Function to return a number between 0-1
# Simulate 10,000 elections, then based on the average result display the probability that candidate A will win,
# and the probability candidate B will win.

def random_result():
    ''' Generates a random floating point number between 0 and 1 '''
    result = random.random()
    return result


def election_region_1(num):
    if num <= 0.87:
        print('Candidate A won Region 1')
    else: 
        print('Candidate B won Region 1')


def election_region_2(num):
    if num <= 0.65:
        print('Candidate A won Region 2')
    else: 
        print('Candidate B won Region 2')


def election_region_3(num):
    if num <= 0.17:
        print('Candidate A won Region 3')
    else: 
        print('Candidate B won Region 3')


def main():
    vote = random_result()
    election_region_1(vote)
    election_region_2(vote)
    election_region_3(vote)



if __name__ == '__main__':
    main()