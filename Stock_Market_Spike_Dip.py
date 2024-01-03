# Add your solution to the problem "change" here.

# Implement a function print_change that takes in the results of your computation
# and prints them out in a message for the user. For example:
#
# Largest change of 25 from  84  to  59
# occurred between day #6 and day #7.
#
# Must not prompt the user for anything.
def print_change(day1_price, day2_price, day1_num):
    max_change = abs(day2_price - day1_price)
    print(f'Largest change of {max_change} from {day1_price} to {day2_price} occured between day #{day1_num} and day #{day1_num + 1}')

# Implement a function find_change that prompts the user for the
# appropriate number of stock prices and returns a list with the the
# value on the first day, the value on the second day, and the number
# of the first day, in that order.
#
# Takes no parameters.
# Must return a list.
def find_change():

    n_days = 10

    max_change = 0

    price1 = int(input(f'What was the price on day 1? '))

    for i in range(1,n_days):
        price2 = int(input(f'What was the price on day {i+1}? '))

        change = abs(price1 - price2)

        if (change > max_change):
            max_change = change
            day1_price = price1
            day2_price = price2
            day = i

        price1 = price2


    max_change_list = [day1_price, day2_price, day]
    return max_change_list

# Implement a main function that computes the largest change as specified in problem 12,
# by using find_change to find the largest change and print_change to print the final answer.
def main():

    max_list = find_change()
    print_change(max_list[0], max_list[1], max_list[2])

# Runs the main function. Leave as is.
if __name__ == "__main__":
    main()
