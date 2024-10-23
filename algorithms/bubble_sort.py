'''
Bubble Sort:

Compares two elements and swaps them based on 
whether or not one is greather than another.

If the current index is greater than the index
ahead of it, swap the values.

O(n^2) (poor performance)
'''

def bubble_sort(data):
    print("Initial State: ", data)
    print("-------------------------------------")
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                print("Swapping: ", data[j], data[j+1])
                temp = data[j]
                data[j] = data[j+1]
                data[j+1] = temp
            print("Current State: ", data)



array = [1,4,7,8,2,6,3,0,9]
bubble_sort(array)
