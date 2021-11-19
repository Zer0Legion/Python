import random
array = []


#Let user define array
print("""Welome to my simple demonstration of binary search of a sorted list.
Insert an array, key in multiple numbers individually, or enter "r" for a random array of your chosen length to define the array.
Then, enter the number you want to search.\n""")

input_array = input("Enter multiple numbers or 'r' for a random array of numbers from 1-100.\n")

print(type(input_array))
if input_array == 'r':
    array_len = input("Enter your desired length of the random array:\n")
    for i in range(int(array_len)):
        array.append(random.randint(0,100))
else:
    array.append(int(input_array))
    print(array)
    while True:
        adder = input("Enter another number, or press Enter to finalise the array:\n")
        if adder == '':
            break
        else:
            array.append(int(adder))
            print(array)

array.sort() #remove later for merge sort

orig_array = array #for later; find earliest occurence of number for indexing
print(" The array is:\n",array)


#Let user enter number to search
input_search = (input("Enter an integer you want to search for in the array, or 'r' for a random integer:\n"))
if input_search == 'r':
    search = random.randint(0,100)
else:
    search = int(input_search)
print(" The integer to search is:\n",search)



# main function
def binarysort(array, search):
    # print(array)
    ind = 0

    #check if search is outside of array range
    if search > array[-1]:
        inlist = False
    elif search < array[0]:
        inlist = False
    else:
        inlist = True

    #check first number; prevent error later during the location of first occurence
    if array[0] == search:
        return 0


    #main body; splitting up the array
    while len(array) > 1:

        midpoint = array[int(len(array) / 2)]
        # print('index',ind , 'midpt', midpoint)

        if search < midpoint:
            array = array[:int(len(array) / 2)]
            # print(array)
            # print('index',ind , 'midpt', midpoint)
        elif search > midpoint:
            ind = ind + int(len(array) / 2) + 1
            array = array[int(len(array)/ 2)+1:]
            # print(array)
            # print('index',ind , 'midpt', midpoint)
        else: #search = midpoint
            solution = array.index(search)
            # ind = ind + int(len(array) / 2)
            if len(array) == 2:
                ind = ind + 1
            else:
                ind = ind = ind + int(len(array) / 2)
            # print('found')
            break

    #mainly to make sure index is correct for array of even-numbered length
    if len(array) == 1:
        # print('array[0]',array[0] , ', search',search)
        if array[0] == search:
            inlist = True
        else:
            inlist = False
    elif len(array) == 2:
        for i in array:
            if i == search:
                inlist = True

    # print( 'searching for\n',
    # search,'\n',
    # 'in\n',
    # array)
    # print(array)

    #check inlist condition
    if inlist == False:
        return("Not in list")
    else: #inlist = True

        #return first occurence of searched number
        while orig_array[ind] == orig_array[ind-1]:
            ind = ind - 1

        return ind

print(binarysort(array,search))
