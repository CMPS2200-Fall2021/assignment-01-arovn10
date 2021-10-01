"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<=1:
        return x
    else:
        ra = x-1
        rb = x-2
        return foo(ra) + foo(rb)


def longest_run(mylist, key):

    numOfMatches = 0
    maxNumOfMatches = []

    for value in mylist:
        if value == key:
            numOfMatches += 1
        else:
            numOfMatches = 0
        maxNumOfMatches.append(numOfMatches)


    return max(maxNumOfMatches)






class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    


def longest_run_recursive(mylist, key):

    if len(mylist)<=1:
        if mylist[0] == key:
            mainList = Result(1, 1, 1, True)
            return mainList
        else:
            mainList = Result(0, 0, 0, False)
            return mainList
    else:
        length = len(mylist)//2
        halfOne = longest_run_recursive(mylist[:length], key)
        halfTwo = longest_run_recursive(mylist[length:], key)

    return combine(halfOne, halfTwo)






## Feel free to add your own tests here.
def combine(resultObject1, resultObject2):
    if resultObject1.is_entire_range == True and resultObject2.is_entire_range == True:
        return Result((resultObject1.left_size+resultObject2.left_size), (resultObject1.right_size+resultObject2.right_size), (resultObject1.left_size+resultObject2.left_size), True)
#everything after this point is false


    #_______________________________________________________
    #Finding the right and left lengths

    if resultObject1.is_entire_range == True:
        #if its entire range and object 2 left side has the key
        leftside = resultObject1.left_size + resultObject2.left_size

    else:
        #if object 2 does not have the key on the left side
        leftside = resultObject1.left_size



    if resultObject2.is_entire_range == True:
    #if the entire range and object 1 right side has the key
            rightside = resultObject2.right_size + resultObject1.right_size
    else:

            rightside = resultObject2.right_size


    #-------------------------------------------------------------------------------
    #Finding the longest


   #Does it continue down the middle
    if resultObject1.right_size>=1 and resultObject2.left_size>=1:
        continueDownMiddle = True

    #If it continues down the middle

    competitor = resultObject1.right_size + resultObject2.left_size

    if competitor > max(resultObject1.longest_size, resultObject2.longest_size):
        return Result(leftside, rightside, competitor, False)
    else:

        return Result(leftside, rightside, max(resultObject1.longest_size, resultObject2.longest_size), False)












def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


def test_longest_run_recursive():
    assert longest_run_recursive([6, 6, 12, 12], 12).longest_size == 2
    assert longest_run([12, 12, 12, 8, 12, 12, 0, 12, 1], 12) == 3
    assert longest_run([12, 12, 12, 8, 12, 12, 0, 12, 12, 12, 12], 12) == 4




test_longest_run_recursive()
