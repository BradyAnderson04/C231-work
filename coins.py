'''
Generating random values for coins to analyze conditional probability
'''
import random as rn

def flip_coin():
    '''
    A simple coin flip
    '''
    return "Heads" if rn.randint(0, 1) else "Tails"

def flip_n_times(n):
    '''
    flip a coin n times and share frequency results
    '''
    freq_table = {}
    order = []

    for i in range(n):
        temp = flip_coin()

        if(freq_table.get(temp) is not None):
                freq_table[temp] += 1 # increment value
        else:
            freq_table[temp] = 1 # create and init value
        
        order.append(temp)

    return freq_table, order

def display_dict(freq_dict):
    # iterate over keys and print the key value pair -- from last hw
    for key in freq_dict:
        print(key,":",freq_dict[key])

if __name__ == '__main__':

    freq, order = flip_n_times(40)

    print("Flip Frequency:")
    display_dict(freq)

    print("Flip Order:")
    print(order)
