# Solution to 1.9.2 of the Real Python Course

def starting_data():
    # (a) the name of a university, 
    # (b) the total number of enrolled students, and 
    # (c) the annual tuition fees
    universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]

    return universities


def enrollment_stats(stats):
    ''' Splits the list of lists into separate lists '''
    schools = []
    enrolled_students = []
    tuition_fees = []

    for i in stats:
        schools.append(i[0])
        enrolled_students.append(i[1])
        tuition_fees.append(i[2])

    return enrolled_students, tuition_fees


def mean(data):
    ''' Calculates the mean of the list values '''
    total = 0
    for i in data:
        total = total + i
    
    raw_mean = total / len(data)
    mean = round(raw_mean)

    return mean, total


def median(data):
    ''' Calculates the list mean, knowing there is 7 items in the list. '''
    data.sort()
    median = data[3]
    return median    


def main():
    ''' Main function '''
    data = starting_data()
    enrolled, tuition = enrollment_stats(data)
    enrolled_mean, enrolled_total = mean(enrolled)
    tuition_mean, tuition_total = mean(tuition)
    enrolled_median = median(enrolled)
    tuition_median = median(tuition)

    print(f'Total students: {enrolled_total}')
    print(f'Total tuition: {tuition_total}')
    print(f'Student mean: {enrolled_mean}')
    print(f'Student median: {enrolled_median}')
    print(f'Tuition mean: {tuition_mean}')
    print(f'Tuition median: {tuition_median}')
        

if __name__ == '__main__':
    main()