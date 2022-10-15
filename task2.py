from random import randint
count = 0



def main():
    print("Welcome to Recursion Fun")

    # aggienacci calculation
    value = eval(input("Enter a number to find it's aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + str(round(aggienacci(value), 4)))

    print()

    # Recursive search and sort
    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(200000):
        if randint(0, 2) == 0:
            numList.append(i)

    numPos = binarySearch(numList, key)

    if numPos == -1:
        print("Your number, " + str(key) + ", is not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + str(numPos))

    print("Total recursive calls: " + str(count))

# Creating the aggienacci thing
def aggienacci(inputValue):
    if inputValue == 0:  # Base case
        return 0
    elif inputValue == 1:  # Base Case
        return 1
    elif inputValue == 2:  # Base Case
        return 2
    else:
        return (aggienacci(inputValue - 3) + aggienacci(inputValue - 2)) / aggienacci(inputValue - 1)

# Creating binary search
def binarySearch(list, key):
    # Keep track
    low = 0
    high = len(list) - 1
    # Searching
    return binarySearchRecursive(list, key, low, high, count)

# Creating the binary recursive search
def binarySearchRecursive(list, key, low, high, count):
    if low > high:
        return -1
    mid = (low + high) // 2
    if key == list[mid]:
        return mid
    elif key < list[mid]:
        return binarySearchRecursive(list, key, low, mid - 1, count + 1)
    else:
        return binarySearchRecursive(list, key, mid + 1, high, count + 1)


main()
