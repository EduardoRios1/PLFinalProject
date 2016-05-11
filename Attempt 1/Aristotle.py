'''
Function: tipCalc
Arguments: takes two functions (func -> evaluate tips, func2 -> divides tab)
Purpose: Divides the tab equally to a certain number of people including tip
'''
def tipCalc(func, func2):

    '''
    Function: wrapper
    Arguments: takes three number parameters (amount of tab, tip rate, number of people)
    Purpose: Distribute arguments to specific functions
    '''
    def wrapper(n,y,z):

        return func2(func(n,y)+n, z)
    return wrapper

'''
Function: tip
Arguments: takes two float numbers (amount of tab, tip rate)
Purpose: Multiply tab amount with the rate
'''
def tip(amount, tipRate): return amount * tipRate

'''
Function: divTab
Arguments: takes one float number and one integer (amount of tab, number of people)
Purpose: Divide tab equally among a certain number of people
'''
def divTab(amount, numOfPeople): return amount / numOfPeople

#print tipCalc(tip, divTab)(100, 0.10, 6) # First 2 params are for tipCalc and the last 3 params are for wrapper