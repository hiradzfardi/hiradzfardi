per_hour = int (input ('How Much Do You Earn Per Hour :'))
hour = int (input ('How many Hours You Work In A Day :'))
def salary( hour , per_hour ):
    if hour > 8 :
        return 'too much work !!'
    elif per_hour < 6 :
        return 'why you are working ?! '
    else:
        earn = hour * per_hour
    return earn

salary (hour , per_hour)